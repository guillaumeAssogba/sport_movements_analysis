import pandas as pd
import numpy as np

#load the data files
def dataLoading(file, firstFile=True):
    numberSheets = 1
    try:
        bodyData = pd.ExcelFile(str(file))
        if(firstFile == True):
            numberSheets = input("How many sheets do you have in this file? ")
    except:
        try:
           bodyData = pd.read_csv(str(file))
        except:
            print("Please provide an excel or csv file")
    return bodyData, numberSheets

def importData():
    file1 = input("What is the name of the data file with body movements variables? ")
    bodyData, numberSheets = dataLoading(file1)
    file2 = input("What is the name of the second data file with performance? ")
    performanceData, numberSheets2 = dataLoading(file2, False)
    return bodyData, numberSheets, performanceData


#Loading the excel files as a dataframe and transform them in arrays
def constructMatrices(numberSheets, kicking_data, performance_data):
    bodyMatrices = []
    for i in range(int(numberSheets)):
        name =input("What is the name of the sheet number " + str(i+1) + "?")
        bodyMatrices.append(kicking_data.parse(name).as_matrix())
    namePerf =input("What is the sheet's name of the performance file?")
    perf = performance_data.parse(namePerf).as_matrix()

    return bodyMatrices, perf

#Load for not writing all the time
def FastRugbyBuild(name1, name2):
    sportData = pd.ExcelFile(name1)
    perfData = pd.ExcelFile(name2)
    bodyMatrices = []
    varName = []
    for i in range(len(sportData.sheet_names)):
        bodyMatrices.append(sportData.parse(sportData.sheet_names[i]).as_matrix())
        varName.append(sportData.sheet_names[i])
    perf = perfData.parse(perfData.sheet_names[0]).as_matrix()
    return bodyMatrices, perf, varName

#Create adapted variables for future processing and their mean.
def constructVariables(bodyMatrices, performance):
    #The time is the same for every data and correspond to the first column
    time = bodyMatrices[1][:,0]
    #Variables sheet 1
    varMatrices = []
    meanMatrices = []
    
    for i in range(len(bodyMatrices)):
        varMatrices.append(bodyMatrices[i][:, 1:len(bodyMatrices[i].T)])
        meanMatrices.append(np.mean(varMatrices[i], axis=1))
    
    #performances
    distance = performance[:,0]
    position = performance[:,1]

    return time, varMatrices, meanMatrices, distance, position
