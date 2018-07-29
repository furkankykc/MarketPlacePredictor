from sklearn.datasets import make_blobs
import models
from meanShift import Mean_Shift
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

X= make_blobs(n_features=2, centers=20,n_samples=520)[0]

Market = make_blobs(n_features=2,centers=10,n_samples=10)[0]

#plt.scatter(X[:,0], X[:,1], s=150)
#plt.show()

colors = 10*["g","r","c","b","k"]
clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids
ccc = []
for c in centroids:
    ccc.append(centroids[c])


new_market = models.calculateDistance(ccc,Market)
print new_market
plt.scatter(X[:,0], X[:,1], s=150,marker=".",color="k")
plt.scatter(Market[:,0], Market[:,1], s=150,color="b")

plt.scatter(new_market[0],new_market[1],s=1505,color='r',marker='+')
# for c in centroids:
#      plt.scatter(centroids[c][0], centroids[c][1], color='k', marker='*', s=150)

plt.show()