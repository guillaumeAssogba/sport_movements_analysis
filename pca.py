import matplotlib.pyplot as plt
import numpy as np
from numpy import mean, dot, linalg
from sklearn.utils import check_array
from sklearn.utils.extmath import svd_flip

### PCA Section ###

#Represention of the variance explained by PCs
def explainedVariance(explained_variance_ratio_, varName):
    plt.bar(np.arange(15) + 0.6, explained_variance_ratio_.cumsum())
    plt.ylim((0, 1))
    plt.xlabel('No. of principal components')
    plt.ylabel('Cumulative variance explained')
    plt.grid(axis = 'y', ls = '-', lw = 1, color = 'white')
    plt.savefig("plot/PCA/varianceExplained"+varName, bbox_inches='tight')
    plt.show()

#Representation of the loadings
def factorLoadings(components_, i, varName):
    plt.bar(np.arange(15) + 0.6, components_[i])
    plt.xlabel('No. of the kicker')
    plt.ylabel('Factor loadings for the PC No ' + str(i+1))
    plt.savefig("plot/PCA/"+varName+"PC" +str(i), bbox_inches='tight')
    plt.show()

# Get variance explained by singular values
def varianceExplained(S, n_samples):
    explained_variance_ = (S ** 2) / (n_samples - 1)
    total_var = explained_variance_.sum()
    explained_variance_ratio_ = explained_variance_ / total_var
    return explained_variance_ratio_

def PCA_values(data, centered=True):
    n_samples, n_features = data.shape
    #By default, the data are centered
    if (centered == True):
        data_centered = data - mean(data, axis=0)
    else:
        data_centered = data

    #apply the Single Vector Decomposition 
    U, S, V = linalg.svd(data_centered, full_matrices=False)
    # flip eigenvectors' sign to enforce deterministic output
    U, V = svd_flip(U, V)

    #components
    components_ = V

    #variance explained by PCs
    explained_variance_ratio_ = varianceExplained(S, n_samples)

    return(components_, explained_variance_ratio_)

def PCA_projection(data, components_):
    data = check_array(data)
    data_projected = dot(data, components_.T)

    return data_projected

def constructStdDeviationComponents(data, data_components):
    data = check_array(data)
    stdProjectionPos = []
    stdProjectionNeg = []
    for i in range(len(data_components)):
        intermediatePosVar = []
        intermediateNegVar = []
        stdComponents = np.std(data_components[i])
        
        if i == 0:
            intermediatePosVar =  np.vstack((data_components[0]+ stdComponents, data_components[1::]))
            intermediateNegVar =  np.vstack((data_components[0]- stdComponents, data_components[1::]))
            stdProjectionPos = PCA_projection(data, intermediatePosVar)
            stdProjectionNeg = PCA_projection(data, intermediateNegVar)
        elif i == len(data_components)-1:
            intermediatePosVar =  np.vstack((data_components[:i], data_components[i]+ stdComponents))
            intermediateNegVar =  np.vstack((data_components[:i], data_components[i]- stdComponents))
            stdProjectionPos = np.hstack((stdProjectionPos, PCA_projection(data, intermediatePosVar)))
            stdProjectionNeg = np.hstack((stdProjectionNeg, PCA_projection(data, intermediateNegVar)))
        else:
            intermediatePosVar =  np.vstack((data_components[:i], data_components[i]+ stdComponents, data_components[i+1::]))
            intermediateNegVar =  np.vstack((data_components[:i], data_components[i]- stdComponents, data_components[i+1::]))
            stdProjectionPos = np.hstack((stdProjectionPos, PCA_projection(data, intermediatePosVar)))
            stdProjectionNeg = np.hstack((stdProjectionNeg, PCA_projection(data, intermediateNegVar)))

    return np.array(stdProjectionPos), np.array(stdProjectionNeg)
        
def applyPCA(data, stdDeviation, varName, nb):
    stdProjectionsPos= []
    stdProjectionsNeg= []
    
    for i in range(len(data)):
        intermediateComponentsPCA, data_explained_variance_ratio_ = PCA_values(data[i])
        #represent the percentage of variance explained
        explainedVariance(data_explained_variance_ratio_, varName[i])
    
        #represent the factor loadings for each PCs
        for j in range(nb):
            factorLoadings(intermediateComponentsPCA, j, varName[i])
    
        #Project the data into the new PCs axis
        intermediateProjected = PCA_projection(data[i], intermediateComponentsPCA[:nb])
        
        if i == 0:
            dataProjected = intermediateProjected
            componentsPCA = intermediateComponentsPCA[:nb]
            pcaVariance = np.around(data_explained_variance_ratio_[:nb], decimals=3)*100
            if stdDeviation:
                intermediateStdProjectionsPos, intermediateStdProjectionsNeg = constructStdDeviationComponents(data[i], intermediateComponentsPCA[:nb])
                stdProjectionsPos = intermediateStdProjectionsPos
                stdProjectionsNeg = intermediateStdProjectionsNeg
        else:
            dataProjected = np.hstack((dataProjected, intermediateProjected))
            componentsPCA = np.concatenate((componentsPCA, intermediateComponentsPCA))
            varianceEx = np.around(data_explained_variance_ratio_[:nb], decimals=3)*100
            pcaVariance = np.concatenate((pcaVariance, varianceEx))
            if stdDeviation:
                intermediateStdProjectionsPos, intermediateStdProjectionsNeg = constructStdDeviationComponents(data[i], intermediateComponentsPCA[:nb])
                stdProjectionsPos = np.hstack((stdProjectionsPos, intermediateStdProjectionsPos))
                stdProjectionsNeg = np.hstack((stdProjectionsNeg, intermediateStdProjectionsNeg))

    return dataProjected, componentsPCA[:nb*len(data)], stdProjectionsPos, stdProjectionsNeg, pcaVariance

