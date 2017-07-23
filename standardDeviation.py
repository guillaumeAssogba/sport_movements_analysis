#import modules
import numpy as np
import createVar as load
import createGroups as groups
import pca
import representation as pltVar
import matplotlib.pyplot as plt

#For not writting all the information about the data all the time 
kicks, perf = load.FastRugbyBuild()
time, var1, var1_mean, var2, var2_mean, var3, var3_mean, distance, position = load.constructVariables(kicks[0], kicks[1], kicks[2], perf)

#create groups for best and worst kickers
perf_data = groups.createGroupsByKmeans(distance)

#Apply the PCA for the first, second and third variable
var1_reduced, var1_components = pca.applyPCA(var1)

print(var1_reduced.shape)

### STANDARD DEVIATION ###

def construct(dataReduced, dataComponents, i):

if i == 0:
    var1_stdPos = np.vstack([np.array([var1_components[0,:]+ np.std(var1_components[i,:])]),\
                         var1_components[i:]])

    var1_stdNeg = np.vstack([np.array([var1_components[0,:]- np.std(var1_components[0,:])]),\
                         var1_components[1:]])
else:
    var1_stdPos = np.vstack([var1_components[:i-1], np.array([var1_components[0,:]+ np.std(var1_components[i,:])]),\
                         var1_components[i+1:]])

    var1_stdNeg = np.vstack([np.array([var1_components[0,:]- np.std(var1_components[0,:])]),\
                         var1_components[1:]])
dataOriginalSpace = np.dot(var1_reduced, var1_components)
MeanOriginalSpace = np.mean(dataOriginalSpace, axis=1)

dataPosOriginalSpace = np.dot(var1_reduced, var1_stdPos)
MeanPosOriginalSpace = np.mean(dataPosOriginalSpace, axis=1)

dataNegOriginalSpace = np.dot(var1_reduced, var1_stdNeg)
MeanNegOriginalSpace = np.mean(dataNegOriginalSpace, axis=1)


plt.plot(time, MeanOriginalSpace,'b', label='original space data reduced')
plt.plot(time, MeanPosOriginalSpace,'g--', label='original space data reduced + std first loadings')
plt.plot(time, MeanNegOriginalSpace,'r--', label='original space data reduced - std first loadings')
plt.show()
    #return 
    
