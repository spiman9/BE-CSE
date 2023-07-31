# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:10:29 2023

@author: PRITHAM
"""

xlist = [[1 , 1] , [1 , -1] , [-1 , 1] , [-1 , -1]]
Y = [1 , -1 , -1 , -1]
w1 , w2 , bw = 0 , 0 , 0
b = 1

def hebb():
    global w1 , w2 , bw
    print("dw1\tdb2\tdb\tw1\tw2\bw")
    i = 0
    for x in xlist:
        dw1 = x[0] * Y[i]
        dw2 = x[1] * Y[i]
        db = Y[i]
        w1 += dw1
        w2 += dw2
        bw += db
        i+=1
        print(dw1 , dw2 , db , w1 , w2 , bw , sep="\t")
print("Learning.......")
hebb()
print("Learning Completed")


print("Output from and gate is")

print("x1\tx2\ty")

for x in xlist:
    print(x[0] , x[1] , 1 if (w1 * x[0] + w2 * x[1] + b * bw) > 0 else -1 , sep="\t")


print("The weights are  w1 = {} , w2 = {}  ".format(w1 , w2))
        