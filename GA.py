# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:28:08 2017

@author: devops
"""

G = []
G0 =["01110","00011","11001","10101" ]
Goal = "11111"
G.append(G0)

def cross_over(best_2,k):
    tmp1 = best_2[0][0:k] + best_2[1][k:]
    tmp2 = best_2[1][0:k]+best_2[0][k:]
    return tmp1 , tmp2

def fitnes(d):
    return int(d  , 2)

def need_mut(son1,son2,best_2):
    if fitnes(son1) > int(best_2[0]) and fitnes(son1) > int(best_2[1]) or fitnes(son2) > int(best_2[0]) and fitnes(son2) > int(best_2[1]):
        return False
    else:
        return True
def best(size , data):
    best = []
    for i in range(size):
        X = [ fitnes(d) for d in data]
        x = X.index(max(X))
        best.append(data[x])
        X.remove(X[x])
        data.remove(data[x])
    return best , data

def main(Gi,k):
    tmp_G = Gi[:]
    mutation = False
    G_new = []   
    while tmp_G:
        best_2 = []
        best_2 , tmp_G = best(2 , tmp_G)
        son1 , son2 = cross_over(best_2,k)
        G_new.append(son1)
        G_new.append(son2)
        if need_mut(son1,son2,best_2):
            mutation=True
    return G_new , mutation
    
import random

for i in range(15):
    print("current itration is ",i , "current parent is", G[i])
    G_new , mutation = main(G[i],2)
    print("after crossover we get ",G_new )
    if mutation:
        print("doing mution  to enhance pupolation ")
        j = random.randint(0,len(G0)-1)
        pos = random.randint(0,len(G0)-1)
        print(j , pos)
        print("selected cromosom is ",G_new[j] , "eslected elee is ",G_new[j][pos] ,"Postion in cromosme is ",pos)
        if G_new[j][pos] == "1":
            tmpn = G_new[j][:pos] + "0" + G_new[j][pos+1:]
        else:
            tmpn = G_new[j][:pos] + "1" + G_new[j][pos+1:]
        G_new[j] = tmpn
        print(tmpn)
        print("new cromosom after mution is ",G_new[j] )
        reprocation = G_new +  G[i]
        print("doing reproduction ")
        G_new , _ = best(len(G_new) , reprocation)
        G.append(G_new)
    else:
        G.append(G_new)

    print("current childs now is " , G_new)
    if Goal in G_new:
        print("exits in itration ",i,"goal founded")
        break