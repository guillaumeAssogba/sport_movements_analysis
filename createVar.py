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
    kicking_data = pd.ExcelFile(name1)
    perfData = pd.ExcelFile(name2)
    bodyMatrices = []
    for i in range(len(kicking_data.sheet_names)):
        bodyMatrices.append(kicking_data.parse(kicking_data.sheet_names[i]).as_matrix())
    perf = perfData.parse(kicking_data.sheet_names[0]).as_matrix()
    return bodyMatrices, perf

#Create adapted variables for future processing and their mean.
def constructVariables(data1, data2, data3, performance):
    #The time is the same for every data and correspond to the first column
    time = data1[:,0]
    print(len(data1.T))
    #Variables sheet 1
    var1 = data1[:, 1:len(data1.T)]
    var1_mean = np.mean(var1, axis=1)

    #Variables sheet 2
    var2 = data2[:, 1:len(data2.T)]
    var2_mean = np.mean(var2, axis=1)
    
    #Variables sheet 3
    var3 = data3[:, 1:len(data3.T)]
    var3_mean = np.mean(var3, axis=1)

    #performances
    distance = performance[:,0]
    position = performance[:,1]

    return time, var1, var1_mean, var2, var2_mean, var3, var3_mean, distance, position
