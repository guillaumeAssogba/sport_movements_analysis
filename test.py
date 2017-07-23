#import modules
import createVar as load
import createGroups as groups
import pca
import representation as pltVar

### MAIN ###

def launchProcess(self):
    print(self)
    #load variables
    #kicking_data, numberSheets, performance_data = load.importData()
    
    #construct variables
    #kicks, perf = load.constructMatrices(numberSheets, kicking_data, performance_data)
    
    #For not writting all the information about the data all the time 
    kicks, perf = load.FastRugbyBuild()
    time, var1, var1_mean, var2, var2_mean, var3, var3_mean, distance, position = load.constructVariables(kicks[0], kicks[1], kicks[2], perf)
    
    #create groups for best and worst kickers
    perf_data = groups.createGroupsByKmeans(distance)
    
    #Apply the PCA for the first, second and third variable
    var1_reduced, var1_components = pca.applyPCA(var1)
    var2_reduced, var2_components = pca.applyPCA(var2)
    var3_reduced, var3_components = pca.applyPCA(var3)
    
    #Represent the score for each PCs
    pltVar.PCArepresentation(var1_reduced, "1", var1_mean, time)
    pltVar.PCArepresentation(var2_reduced, "2", var2_mean, time)
    pltVar.PCArepresentation(var3_reduced, "3", var3_mean, time)
    
    #Regressions between loadings and performance
    pltVar.use2dRegressionPlot(distance, var1_components, "var1")
    pltVar.use2dRegressionPlot(distance, var2_components, "var2")
    pltVar.use2dRegressionPlot(distance, var3_components, "var3")
    
    components_var1_superior, components_var1_inferior, var1_superior, var1_inferior = groups.constructComponents(var1_components, var1, perf_data)
    components_var2_superior, components_var2_inferior, var2_superior, var2_inferior = groups.constructComponents(var2_components, var2, perf_data)
    components_var3_superior, components_var3_inferior, var3_superior, var3_inferior = groups.constructComponents(var3_components, var3, perf_data)
    
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

def launchProcess2(name1, name2):
    kicks, perf = load.FastRugbyBuild(name1, name2)
    time, var1, var1_mean, var2, var2_mean, var3, var3_mean, distance, position = load.constructVariables(kicks[0], kicks[1], kicks[2], perf)
    
    #create groups for best and worst kickers
    perf_data = groups.createGroupsByKmeans(distance)
    
    #Apply the PCA for the first, second and third variable
    var1_reduced, var1_components = pca.applyPCA(var1)
    var2_reduced, var2_components = pca.applyPCA(var2)
    var3_reduced, var3_components = pca.applyPCA(var3)
    
    #Represent the score for each PCs
    pltVar.PCArepresentation(var1_reduced, "1", var1_mean, time)
    pltVar.PCArepresentation(var2_reduced, "2", var2_mean, time)
    pltVar.PCArepresentation(var3_reduced, "3", var3_mean, time)
    
    #Regressions between loadings and performance
    pltVar.use2dRegressionPlot(distance, var1_components, "var1")
    pltVar.use2dRegressionPlot(distance, var2_components, "var2")
    pltVar.use2dRegressionPlot(distance, var3_components, "var3")
    
    components_var1_superior, components_var1_inferior, var1_superior, var1_inferior = groups.constructComponents(var1_components, var1, perf_data)
    components_var2_superior, components_var2_inferior, var2_superior, var2_inferior = groups.constructComponents(var2_components, var2, perf_data)
    components_var3_superior, components_var3_inferior, var3_superior, var3_inferior = groups.constructComponents(var3_components, var3, perf_data)
    
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