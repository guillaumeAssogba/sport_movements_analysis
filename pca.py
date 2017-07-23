import matplotlib.pyplot as plt
import numpy as np
from numpy import mean,cov,cumsum,dot,linalg,size,flipud
from sklearn.utils import check_array
from sklearn.utils.extmath import svd_flip

### PCA Section ###

#Represention of the variance explained by PCs
def explainedVariance(explained_variance_ratio_):
    plt.bar(np.arange(15) + 0.6, explained_variance_ratio_.cumsum())
    plt.ylim((0, 1))
    plt.xlabel('No. of principal components')
    plt.ylabel('Cumulative variance explained')
    plt.grid(axis = 'y', ls = '-', lw = 1, color = 'white')
    plt.show()

#Representation of the loadings
def factorLoadings(components_, i):
    plt.bar(np.arange(15) + 0.6, components_[i])
    plt.xlabel('No. of the kicker')
    plt.ylabel('Factor loadings for the PC No ' + str(i+1))
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

def applyPCA(data):
    data_components_, data_explained_variance_ratio_ = PCA_values(data)
    print(data_components_.shape)
    #represent the percentage of variance explained
    #explainedVariance(data_explained_variance_ratio_)

    #represent the factor loadings for each PCs
    #for i in range(3):
    #    factorLoadings(data_components_, i)

    #Project the data into the new PCs axis
    data_projected = PCA_projection(data, data_components_[:3])
    return data_projected, data_components_[:3]
