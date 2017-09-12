from sklearn.cluster import KMeans
import numpy as np

#Function to associate bigger distance value with a 1 and other with a 0
def transformPerfArray(perf_data, distance):
    j=1
    print(distance)
    print(perf_data)
    while perf_data[0] == perf_data[j]:
        j += 1
    if distance[j] < distance[0] and perf_data[0] == 0:
        for i in range(len(perf_data)):
            if perf_data[i] == 0:
                perf_data[i]=1
            else:
                perf_data[i]=0
    return perf_data

#Distinguish the good and bad kicker by applying the k-means method on the distance matrix.
#As it is a 1D-array, we reshape it to [-1,1] for using the k-means algorithm which need a multi-dimensional array
def createGroupsByKmeans(distance):
    kmeans = KMeans(n_clusters=2)
    perf_fit = kmeans.fit_predict(distance.reshape(-1,1))
    perf_data = transformPerfArray(perf_fit, distance)
    perf_data = perf_data.reshape(1,15)
    print(perf_data)
    return perf_data

#Create a per_data array with a 1 for the column of the 33% best kickers,
#a 0 for the 33% worst kickers and -1 otherwise
#This function could be improve and seems too complicated but produce the correct perf_data array
def createGroupsRandomly(distance):
    sorted_distance = distance.argsort()
    perf_data = np.zeros((1, len(distance)))
    for i in range(int(len(distance)/3)):
        perf_data[0,sorted_distance[-5:][::-1][i]] = 1
    for i in range(len(distance)):
        if(perf_data[0,i] == 0):
            perf_data[0,i] = -1
    for i in range(int(len(distance)/3)):
        perf_data[0,sorted_distance[0:5][i]] = 0
    return perf_data

def constructCompts(components_, data, perf_data):
    for i in range(len(data)):
        
        inter_pos, inter_neg, inter_superior, inter_inferior, delete_pos, delete_neg = constructComponents(components_[3*i:3*(i+1)], data[i], perf_data)
        if i == 0:
            components_pos = [inter_pos]
            components_neg = [inter_neg]
            data_superior = [inter_superior]
            data_inferior = [inter_inferior]
        else:
            components_pos = np.concatenate((components_pos, [inter_pos]))
            components_neg = np.concatenate((components_neg, [inter_neg]))
            data_superior = np.concatenate((data_superior, [inter_superior]))
            data_inferior = np.concatenate((data_inferior, [inter_inferior]))
    return components_pos, components_neg, data_superior, data_inferior, delete_pos, delete_neg
#Construction of the superior and inferior arrays and the corresponding components_array
def constructComponents(components_, data, perf_data):
    
    components_pos = components_
    data_superior = data
    delete_pos = 0
    components_neg = components_
    data_inferior = data
    delete_neg = 0
    
    for i in range(len(data[0])):
        if(perf_data[0, i] != 1):
            components_pos = np.delete(components_pos, i-delete_pos, 1)
            data_superior = np.delete(data_superior, i-delete_pos, 1)
            delete_pos += 1
        elif (perf_data[0, i] != 0):
            components_neg = np.delete(components_neg, i-delete_neg, 1)
            data_inferior = np.delete(data_inferior, i-delete_neg, 1)
            delete_neg += 1
    return components_pos, components_neg, data_superior, data_inferior, delete_pos, delete_neg