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

#plot the 2D regression between the performance values and the loadings.
#return the correlation factor: R squared
def use2dRegressionPlot( performance, data_components, name, nbPca):
    correlationCoeff = []

    for i in range(nbPca):
        for k in range(performance.shape[1]):
             correl = plot2dRegression(performance[:,k].reshape(15,1),data_components[i], "performance"+ str(k), "loadings of " + name + " for PC" + str(i+1), "perf" + str(k) + name +"PC"+str(i+1))
             correl = np.around(correl, decimals=3)
             correlationCoeff.append(correl*100)

    return correlationCoeff

#plot the 2D regression between the variables' loadings.
def regressionBetweenVariables(data_components, nbPca, nb):
    for i in range(nb-1):
        for k in range(nb):
            for j in range(i+1, nb):
                for l in range(nb):
                    plot2dRegression(data_components[3*i+k].reshape(15,1), data_components[3*j+l], "PC" + str(k+1) + " var " + str(i+1), "PC" + str(l+1) + " var " + str(j+1), "RegressionLoadingsvar"+ str(i+1) + "PC"+ str(k+1) + "var" + str(j+1)+ "PC"+ str(l+1))

#Function for representing the inf and sup arrays on the projected PCs
def infAndSupPCARepresentation(data, data_superior, data_inferior, name, time, nbVar, nb):
    for i in range(nb):
        plt.plot(time, data[:,i],'b', label='all')
        plt.plot(time, data_superior[:,i],'g--', label='sup')
        plt.plot(time, data_inferior[:,i],'r--', label='inf')
        plt.xlabel('time')
        plt.ylabel('Variable ' + name + " PC" + str(i+1))
        plt.legend()
        plt.savefig("plot/PcaBestworst/"+"Var" + nbVar +"PC"+ str(i+1), bbox_inches='tight')
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