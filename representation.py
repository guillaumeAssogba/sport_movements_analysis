import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats

### REPRESENTATION Section ###

#Function for representing the scores 
def PCArepresentation(data, name, time, namePlot, nb):
    for i in range(nb):
        plt.plot(time, data[:,i], label=str(i+1)+'st component')
    plt.xlabel('time')
    plt.ylabel('Variable ' + name)
    plt.legend()
    plt.savefig("plot/PCArepresentation/"+namePlot, bbox_inches='tight')
    plt.show()

def plot2dRegression(x,y, nameX, nameY, namePlot):
    model = LinearRegression()
    linearModel = model.fit(x, y)
    predictModel = linearModel.predict(x)
    plt.scatter(x,y, color='g')
    plt.plot(x, predictModel, color='k')
    plt.xlabel(nameX)
    plt.ylabel(nameY)
    test = stats.linregress(predictModel,y)
    print("The squared of the correlation coefficient R^2 is " + str(test.rvalue**2))
    plt.savefig("plot/loadings/"+namePlot, bbox_inches='tight')
    plt.show()
    return test.rvalue**2

def use2dRegressionPlot( distance, data_components, name, nb):
    correlationCoeff = []
    for i in range(nb):
        correl = plot2dRegression(distance.reshape(15,1),data_components[i], "distance", "loadings of " + name + " for PC" + str(i+1), "RegressionDistLoading"+ name +"PC"+str(i+1))
        correlationCoeff.append(correl)
        
        for j in range(i+1, nb):
            correl = plot2dRegression(data_components[i].reshape(15,1), data_components[j], "PC" + str(i+1) + " for " + name, "PC"+ str(j+1), "RegressionLoadingsPC"+ str(i+1) +"-" + str(j+1))
            correlationCoeff.append(correl)
    return correlationCoeff

#Function for representing the inf and sup arrays on the projected PCs
def infAndSupPCARepresentation(data, data_superior, data_inferior, name, time, nbVar, nb):
    for i in range(nb):
        plt.plot(time, data[:,i],'b', label='all')
        plt.plot(time, data_superior[:,i],'g--', label='sup')
        plt.plot(time, data_inferior[:,i],'r--', label='inf')
        plt.xlabel('time')
        plt.ylabel('Variable ' + name + " PC" + str(i+1))
        plt.legend()
        plt.savefig("plot/best&worst/"+"Var" + nbVar +"PC"+ str(i+1), bbox_inches='tight')
        plt.show()    

#Function for representing the inf and sup arrays on the projected PCs
def stdDeviationsPCARepresentation(data, data_superior, data_inferior, name, time, namePlot, nb):
    transposeData = data[:,:nb].T
    sumData = np.sum(transposeData, axis=0).T
    
    for i in range(nb):
        transposeDataSup = data_superior[:,nb*i:nb*i+nb].T
        sumDataSup = np.sum(transposeDataSup, axis=0).T
        transposeDataInf = data_inferior[:,nb*i:nb*i+nb].T
        sumDataInf = np.sum(transposeDataInf, axis=0).T
        plt.plot(time, sumData,'b', label='all')
        plt.plot(time, sumDataSup,'g--', label='sup')
        plt.plot(time, sumDataInf,'r--', label='inf')
        plt.xlabel('time')
        plt.ylabel('Variable ' + name)
        plt.legend()
        plt.savefig("plot/PCAstdDeviation/"+namePlot+str(i+1), bbox_inches='tight')
        plt.show() 