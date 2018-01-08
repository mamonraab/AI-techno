# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:09:41 2017

@author: devops
"""

import numpy as np

A0 = [1,1,0,0]
A1 = [1,0,1,0]
A2 = [1,0,0,1]

B0 = [0,0,1]
B1 = [0,1,1]
B2 = [0,1,0]

def conv(inp):
    return np.array([x if x == 1 else -1 for x in inp])
def activation(inp):
    return np.array([0 if x <=0 else 1 for x in inp])
    
tmpA = np.array([conv(A0),conv(A1),conv(A2)])
tmpB = np.array([conv(B0),conv(B1),conv(B2)])
W = tmpA.T.dot(tmpB)


imax=100
test_index=1
for i in range(imax):
    testB = np.array(activation(tmpA[test_index].dot(W)))
    testA = np.array(activation(conv(testB).dot(W.T)))
    tmpA[test_index] = conv(testA)
    if False in(testB == B1) or  False in(testA == A1):
        tmpA[test_index] = conv(testA)
        #print("pair is ",testA , " ",testB)
    else:
        print("seccess to remmber in itration %d"%i)
        print("pair from BAM is ",testA , " ",testB)
        print("desired pair is ",A1 , " ",B1)
        break