#import modules
import createVar as load
import createGroups as groups
import pca
import representation as pltVar

### MAIN ###

    
def launchProcess2(name1, name2, groupMethod, algorithm):
    nb = 3
    kicks, perf, varName = load.FastRugbyBuild(name1, name2)
    time, varMatrices, meanMatrices, distance, position = load.constructVariables(kicks, perf)
    #create groups for best and worst players
    if groupMethod:
        perf_data = groups.createGroupsByKmeans(distance)
    else:
        perf_data = groups.createGroupsRandomly(distance)
    
    #Apply the PCA for all the variables
    data_projected, data_components, stdProjectionsPos, stdProjectionsNeg = pca.applyPCA(varMatrices, algorithm[3], varName)
    
    #Create the std deviation variables
    if algorithm[2]:
        components_superior, components_inferior, var_superior, var_inferior, nbSup, nbInf = groups.constructCompts(data_components, varMatrices, perf_data)
    
    for k in range(len(varMatrices)):

        #Represent the PC scores for each PCs
        if algorithm[1]:
            pltVar.PCArepresentation(data_projected[:,nb*k:nb*(k+1)], "1", time, "PCsVar"+ str(k+1))
        
        #2D Regressions between loadings and performance
        if algorithm[0]:
            pltVar.use2dRegressionPlot(distance, data_components[nb*k:nb*(k+1)], "var" + str(k+1))
    
        #distinguish and project the best and worst players accordingto the groupperformance
        if algorithm[2]:
        
            var_superior_projected = pca.PCA_projection(var_superior[k], components_superior[k])
            var_inferior_projected = pca.PCA_projection(var_inferior[k], components_inferior[k])
            
            pltVar.infAndSupPCARepresentation(data_projected[:,nb*k:3*(k+1)], var_superior_projected, var_inferior_projected, str(k+1), time, ["var1BestWorstPC1", "var1BestWorstPC2", "var1BestWorstPC3"])
        
        #represent the standard deviation of loadings     
        if algorithm[3]:
                pltVar.stdDeviationsPCARepresentation(data_projected[:,nb*k:nb*(k+1)], stdProjectionsPos[:,nb*nb*(k):nb*nb*(k+1)], stdProjectionsNeg[:,nb*nb*(k):nb*nb*(k+1)], str(k+1) , time, "var" + str(k+1)+ "stdDeviationPC1")
#For testing without the interface 
launchProcess2("../bodyData.xlsx", "../performance.xlsx", True, [True, True, True, True, False, False])