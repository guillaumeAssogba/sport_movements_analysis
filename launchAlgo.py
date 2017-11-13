#import modules
import createVar as load
import createGroups as groups
import pca
import representation as pltVar
import latexRendering as ltx

def launchProcess2(name1, name2, groupMethod, algorithm, nbPca, nbKmeans, nbPerf, report):
    """ launch the different algorithms to perform

    Parameters
    ----------
    name1 : string - name of the body movements file.
    name2 : string - name of the performance file.
    groupMethod: boolean - method to pick for the separation (true: K-means / false: standard method)
    algorithm : array of booleans. each element corresponds to an algorithm to perform.
    nbPca : int - number of Principle Components to render
    nbKmeans : int - number of of performance elements to analyze.
    report : boolean - saving or not the report
    """

    kicks, perf, varName = load.FastRugbyBuild(name1, name2)

    if nbPerf > perf.shape[1]:
        nbPerf = perf.shape[1]

    time, varMatrices, meanMatrices, performance = load.constructVariables(kicks, perf, nbPerf)
    correlationCoeff = []
    #create groups for best and worst players
    if nbKmeans > nbPerf:
        nbKmeans = nbPerf
    if groupMethod:
        perf_data = groups.createGroupsByKmeans(performance, nbKmeans)
    else:
        perf_data = groups.createHalfGroups(performance)

    #Apply the PCA for all the variables
    data_projected, data_components, stdProjectionsPos, stdProjectionsNeg, pcaVariance = pca.applyPCA(varMatrices, algorithm[3], varName, nbPca)
    
    pltVar.regressionBetweenVariables(data_components, nbPca, len(varMatrices))
    #Create the std deviation variables
    if algorithm[2]:
        components_superior, components_inferior, var_superior, var_inferior, nbSup, nbInf = groups.constructCompts(data_components, varMatrices, perf_data, nbPca)

    for k in range(len(varMatrices)):

        
        #Represent the PC scores for each PCs
        if algorithm[0]:
            pltVar.PCArepresentation(data_projected[:,nbPca*k:nbPca*(k+1)], str(k+1), time, "PCsVar"+ str(k+1), nbPca)

        #2D Regressions between loadings and performance
        if algorithm[1]:
            correlationValue = pltVar.use2dRegressionPlot(performance, data_components[nbPca*k:nbPca*(k+1)], "var" + str(k+1), nbPca)
            correlationCoeff.append(correlationValue)

        #distinguish and project the best and worst players accordingto the groupperformance
        if algorithm[2]:

            var_superior_projected = pca.PCA_projection(var_superior[k], components_superior[k])
            var_inferior_projected = pca.PCA_projection(var_inferior[k], components_inferior[k])
            pltVar.infAndSupPCARepresentation(data_projected[:,nbPca*k:nbPca*(k+1)], var_superior_projected, var_inferior_projected, str(k+1), time, str(k+1), nbPca)

        #represent the standard deviation of loadings     
        if algorithm[3]:
            pltVar.stdDeviationsPCARepresentation(data_projected[:,nbPca*k:nbPca*(k+1)], stdProjectionsPos[:,nbPca*nbPca*(k):nbPca*nbPca*(k+1)], stdProjectionsNeg[:,nbPca*nbPca*(k):nbPca*nbPca*(k+1)], str(k+1) , time, "var" + str(k+1)+ "stdDeviationPC", nbPca)

    #latex and pdf files to render
    if report:
        ltx.launchReport(len(varMatrices), nbPca, nbPerf, varName, pcaVariance, correlationCoeff, algorithm)
