#!/usr/bin/env python

import numpy as np
import pandas as pd
import sys
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def hierch_cluster(data_df_oi,labels):
    flipped = np.transpose(data_df_oi.values)
    linkx,linky = linkage(data_df_oi.values,method='average'),linkage(flipped,method='average')
    leavesx,leavesy = leaves_list(linkx),leaves_list(linky)
    transformed = data_df_oi.values[leavesx,:][:,leavesy]
    labels_tr = np.array(labels)[leavesy]
    return transformed,labels_tr,linky,leavesy
    
def k_means_cluster(X):
    kmeans = KMeans(n_clusters=5,random_state=0)
    kmeans.fit(X)
    labels = kmeans.predict(X)
    X = pd.merge(pd.DataFrame(X),pd.DataFrame(labels,columns=['cluster']),left_index=True,right_index=True)
    return X.sort_values('cluster')[['CFU','poly','unk','int','mys','mid']].values,labels
    
def heatmap(title,labels,tr_intensities,out_nm):
    plt.figure()
    plt.imshow(tr_intensities,aspect='auto',interpolation='nearest',cmap='gnuplot2')
    plt.grid(False)
    plt.colorbar()
    plt.title(title)
    plt.yticks([])
    plt.xticks([x for x in range(6)],labels)
    plt.savefig(out_nm)
    plt.close()
    
def dendrogram(linky,labels,out_nm):
    plt.figure()
    dendrogram(linky,labels=labels)
    plt.savefig(out_nm)
    plt.close()
    
def main():
    data_df = pd.read_csv(sys.argv[1],sep='\t')
    labels = ['CFU','poly','unk','int','mys','mid']
    data_df_oi = data_df[labels]
    h_transformed, labels_tr,linky,leavesy = hierch_cluster(data_df_oi,labels)
    heatmap('hierarchical clustered gene expression',labels_tr,h_transformed,'hierch_heatmap.png')
    dendrogram(linky,labels,'dendrogram.png')
    k_transformed,k_labels = k_means_cluster(data_df_oi)
    k_transformed = k_transformed[:,leavesy]
    plot_heatmap('k-means clustered gene expression, k=5',labels_tr,k_transformed,'kmeans_heatmap.png')

main()