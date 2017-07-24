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
    var1_reduced, var1_components, stdProjections1 = pca.applyPCA(varMatrices[0])
    var2_reduced, var2_components, stdProjections2 = pca.applyPCA(varMatrices[1])
    var3_reduced, var3_components, stdProjections3 = pca.applyPCA(varMatrices[2])
    
    #Represent the score for each PCs
    if algorithm[1]:
        pltVar.PCArepresentation(var1_reduced, "1", time)
        pltVar.PCArepresentation(var2_reduced, "2", time)
        pltVar.PCArepresentation(var3_reduced, "3", time)
    
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
        
        pltVar.infAndSupPCARepresentation(var1_reduced, var1_superior_projected, var1_inferior_projected, "1", time)
        pltVar.infAndSupPCARepresentation(var2_reduced, var2_superior_projected, var2_inferior_projected, "2", time)
        pltVar.infAndSupPCARepresentation(var3_reduced, var3_superior_projected, var3_inferior_projected, "3", time)
 
    if algorithm[3]:
        pltVar.infAndSupPCARepresentation(var1_reduced, stdProjections1[:,[0,2,4]], stdProjections1[:,[1,3,5]], "1", time)
        pltVar.infAndSupPCARepresentation(var2_reduced, stdProjections2[:,[0,2,4]], stdProjections2[:,[1,3,5]], "2", time)
        pltVar.infAndSupPCARepresentation(var3_reduced, stdProjections3[:,[0,2,4]], stdProjections3[:,[1,3,5]], "3", time)
        
launchProcess2("../bodyData.xlsx", "../performance.xlsx", True, [False, False, False, True, False, False])