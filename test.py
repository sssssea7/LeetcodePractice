# from sortedcontainers import SortedList

# A = SortedList(key=lambda x: (x[0], -x[1]))
# A.add((5,6))
# A.add((1,2))
# A.add((2,2))
# A.add((1,1))
# print(A)


import numpy as np
from scipy.spatial.distance import cdist 
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

#Function to implement steps given in previous section
def K_means(x, k, no_of_iterations):
    idx = np.random.choice(len(x), k)
    # Randomly choosing Centroids 
    centroids = x[idx, :] #Step 1
    # Finding the distance between centroids and all the data points
    distances = cdist(x, centroids ,'euclidean') #Step 2
    #Centroid with the minimum Distance
    points = np.array([np.argmin(i) for i in distances]) #Step 3
     
    #Repeating the above steps for a defined number of iterations
    #Step 4
    for _ in range(no_of_iterations): 
        centroids = []
        for idx in range(k):
            #Updating Centroids by taking mean of Cluster it belongs to
            temp_cent = x[points==idx].mean(axis=0) 
            centroids.append(temp_cent)
 
        centroids = np.vstack(centroids) #Updated Centroids 
         
        distances = cdist(x, centroids ,'euclidean')
        points = np.array([np.argmin(i) for i in distances])
         
    return points 

#Load Data
data = load_digits().data
pca = PCA(2)
  
#Transform the data
df = pca.fit_transform(data)
label = K_means(df, 10,10)
print(label)

# reference: https://www.askpython.com/python/examples/k-means-clustering-from-scratch