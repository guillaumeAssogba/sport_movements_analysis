import pandas as pd
import numpy as np

#load the data files
def importData(file):
    try:
        fileData = pd.ExcelFile(file)
    except:
        try:
           fileData = pd.read_csv(file)
        except:
            print("Please provide an excel or csv file")
    return fileData

#Load for not writing all the time
def FastRugbyBuild(name1, name2):
    sportData = importData(name1)
    perfData = importData(name2)
    bodyMatrices = []
    varName = []
    for i in range(len(sportData.sheet_names)):
        bodyMatrices.append(sportData.parse(sportData.sheet_names[i]).as_matrix())
        varName.append(sportData.sheet_names[i])
    perf = perfData.parse(perfData.sheet_names[0]).as_matrix()
    return bodyMatrices, perf, varName

#Create adapted variables for future processing and their mean.
def constructVariables(bodyMatrices, performance, nbPerf):
    #The time is the same for every data and correspond to the first column
    time = bodyMatrices[1][:,0]
    #Variables sheet 1
    varMatrices = []
    meanMatrices = []
    
    for i in range(len(bodyMatrices)):
        varMatrices.append(bodyMatrices[i][:, 1:len(bodyMatrices[i].T)])
        meanMatrices.append(np.mean(varMatrices[i], axis=1))
    
    #performances
    performance = performance[:,:nbPerf]

    return time, varMatrices, meanMatrices, performance