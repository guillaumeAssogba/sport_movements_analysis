#import modules
import createVar as load
import createGroups as groups
import pca
import representation as pltVar

### MAIN ###

    
def launchProcess2(name1, name2, groupMethod, algorithm):
    print(algorithm)
    kicks, perf = load.FastRugbyBuild(name1, name2)
    time, varMatrices, meanMatrices, distance, position = load.constructVariables(kicks, perf)
    
    #create groups for best and worst kickers
    if groupMethod:
        perf_data = groups.createGroupsByKmeans(distance)
    else:
        perf_data = groups.createGroupsRandomly(distance)
    
     #Apply the PCA for the first, second and third variable
    var1_reduced, var1_components, stdProjectionsPos1, stdProjectionsNeg1 = pca.applyPCA(varMatrices[0], algorithm[3])
    var2_reduced, var2_components, stdProjectionsPos2, stdProjectionsNeg2 = pca.applyPCA(varMatrices[1], algorithm[3])
    var3_reduced, var3_components, stdProjectionsPos3, stdProjectionsNeg3 = pca.applyPCA(varMatrices[2], algorithm[3])
    
    #Represent the score for each PCs
    if algorithm[1]:
        pltVar.PCArepresentation(var1_reduced, "1", time, "PCsVar1")
        pltVar.PCArepresentation(var2_reduced, "2", time, "PCsVar2")
        pltVar.PCArepresentation(var3_reduced, "3", time, "PCsVar3")
    
    #Regressions between loadings and performance
    if algorithm[0]:
        pltVar.use2dRegressionPlot(distance, var1_components, "var1")
        pltVar.use2dRegressionPlot(distance, var2_components, "var2")
        pltVar.use2dRegressionPlot(distance, var3_components, "var3")
    
    if algorithm[2]:
        components_var1_superior, components_var1_inferior, var1_superior, var1_inferior = groups.constructComponents(var1_components, varMatrices[0], perf_data)
        components_var2_superior, components_var2_inferior, var2_superior, var2_inferior = groups.constructComponents(var2_components, varMatrices[1], perf_data)
        components_var3_superior, components_var3_inferior, var3_superior, var3_inferior = groups.constructComponents(var3_components, varMatrices[2], perf_data)
        
        #project the superior and inferior arrays
        var1_superior_projected = pca.PCA_projection(var1_superior, components_var1_superior)
        var1_inferior_projected = pca.PCA_projection(var1_inferior, components_var1_inferior)
        var2_superior_projected = pca.PCA_projection(var2_superior, components_var2_superior)
        var2_inferior_projected = pca.PCA_projection(var2_inferior, components_var2_inferior)
        var3_superior_projected = pca.PCA_projection(var3_superior, components_var3_superior)
        var3_inferior_projected = pca.PCA_projection(var3_inferior, components_var3_inferior)
        
        pltVar.infAndSupPCARepresentation(var1_reduced, var1_superior_projected, var1_inferior_projected, "1", time, ["var1BestWorstPC1", "var1BestWorstPC2", "var1BestWorstPC3"])
        pltVar.infAndSupPCARepresentation(var2_reduced, var2_superior_projected, var2_inferior_projected, "2", time, ["var2BestWorstPC1", "var2BestWorstPC2", "var2BestWorstPC3"])
        pltVar.infAndSupPCARepresentation(var3_reduced, var3_superior_projected, var3_inferior_projected, "3", time, ["var3BestWorstPC1", "var3BestWorstPC2", "var3BestWorstPC3"])
 
    if algorithm[3]:
        print(stdProjectionsPos1[:,[3,4,5]]-stdProjectionsPos1[:,[6,7,8]])
        print()
        for i in range(3):
            pltVar.stdDeviationsPCARepresentation(var1_reduced, stdProjectionsPos1[:,[3*i,3*i+1,3*i+2]], stdProjectionsNeg1[:,[3*i,3*i+1,3*i+2]], "1" , time, "var1stdDeviationPC" + str(i+1))
            pltVar.stdDeviationsPCARepresentation(var2_reduced, stdProjectionsPos2[:,[3*i,3*i+1,3*i+2]], stdProjectionsNeg2[:,[3*i,3*i+1,3*i+2]], "2", time, "var2stdDeviationPC" + str(i+1))
            pltVar.stdDeviationsPCARepresentation(var3_reduced, stdProjectionsPos3[:,[3*i,3*i+1,3*i+2]], stdProjectionsNeg3[:,[3*i,3*i+1,3*i+2]], "3", time, "var3stdDeviationPC" + str(i+1))
        
#launchProcess2("../bodyData.xlsx", "../performance.xlsx", True, [False, False, False, True, False, False])