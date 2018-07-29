from sklearn.datasets import make_blobs
import numpy as np

def calculateDistance(x,y):
    my_point = [0,0]
    max = 0
    for i in x:
        for j in y:

            dist =  np.linalg.norm(i - j)
            print "X:",i,"Y:",j,"d:",dist
            if max<dist:
                max=dist
                my_point=i
    return my_point
