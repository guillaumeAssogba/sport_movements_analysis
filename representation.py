import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats

### REPRESENTATION Section ###

#Function for representing the scores 
def PCArepresentation(data, name, mean, time):
    plt.plot(time, data[:,0],'b', label='1st component')
    plt.plot(time, data[:,1],'g', label='2nd component')
    plt.plot(time, data[:,2],'r', label='3rd component')
    #plt.plot(time, mean,'k', label='mean')
    plt.xlabel('time')
    plt.ylabel('Variable ' + name)
    plt.legend()
    plt.show()

def plot2dRegression(x,y, nameX, nameY):
    model = LinearRegression()
    linearModel = model.fit(x, y)
    predictModel = linearModel.predict(x)
    plt.scatter(x,y, color='g')
    plt.plot(x, predictModel, color='k')
    plt.xlabel(nameX)
    plt.ylabel(nameY)
    test = stats.linregress(predictModel,y)
    print("The squared of the correlation coefficient R^2 is " + str(test.rvalue**2))
    plt.show()

def use2dRegressionPlot( distance, data_components, name):
    for i in range(3):
        plot2dRegression(distance.reshape(15,1),data_components[i], "distance", "loadings of " + name + " for PC" + str(i+1))
    plot2dRegression(data_components[0].reshape(15,1), data_components[1], "PC1 for " + name, "PC2")
    plot2dRegression(data_components[0].reshape(15,1), data_components[2], "PC1 for " + name, "PC2")
    plot2dRegression(data_components[1].reshape(15,1), data_components[2], "PC1 for " + name, "PC2")

#Function for representing the inf and sup arrays on the projected PCs
def infAndSupPCARepresentation(data, data_superior, data_inferior, name, time):
    for i in range(3):
        plt.plot(time, data[:,i],'b', label='all')
        plt.plot(time, data_superior[:,i],'g--', label='sup')
        plt.plot(time, data_inferior[:,i],'r--', label='inf')
        plt.xlabel('time')
        plt.ylabel('Variable ' + name + " PC" + str(i+1))
        plt.legend()
        plt.show()    
