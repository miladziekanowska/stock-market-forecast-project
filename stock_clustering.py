# importing libraries
import pandas as pd
import numpy as np
from tslearn.clustering import TimeSeriesKMeans
from sklearn.preprocessing import StandardScaler

# importing our data
from stock_dataset import stock_data

stock_data_copy = stock_data.copy()

# for scaling the data
scaler = StandardScaler()

# Preparing the data to be clustered
for key in stock_data_copy:
    stock_data_copy[key] = stock_data_copy[key][['close', 'dailychange']]
    stock_data_copy[key] = scaler.fit_transform(stock_data_copy[key])

X = np.array(list(stock_data_copy.values()))


# using the TimeSeriesKMeans model for clustering
kmeans = TimeSeriesKMeans(n_clusters=5,
                         n_init=5)

# Fitting the data
kmeans.fit(X)

# Creating the labels variable
labels = kmeans.labels_

# Creating the clusters dictionary for future use
clusters_dict = {}

for i, firm_name in enumerate(stock_data_copy.keys()):
    if labels[i] == 0:
        if 0 not in clusters_dict.keys():
            clusters_dict[0] = [firm_name]
        else:
            clusters_dict[0].append(firm_name)
    elif labels[i] == 1:
        if 1 not in clusters_dict.keys():
            clusters_dict[1] = [firm_name]
        else:
            clusters_dict[1].append(firm_name)
    elif labels[i] == 0:
        if 2 not in clusters_dict.keys():
            clusters_dict[2] = [firm_name]
        else:
            clusters_dict[2].append(firm_name)
    elif labels[i] == 3:
        if 3 not in clusters_dict.keys():
            clusters_dict[3] = [firm_name]
        else:
            clusters_dict[3].append(firm_name)
    elif labels[i] == 4:
        if 4 not in clusters_dict.keys():
            clusters_dict[4] = [firm_name]
        else:
            clusters_dict[4].append(firm_name)
            
print('Clustering done!')