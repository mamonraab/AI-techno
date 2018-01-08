# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:59:05 2017

@author: devops
"""
stance = input("please enter your stance ?")
#stance = "the man like the dog"
dic = {"the":"det","man":"noun","a":"det", "dog":"noun","like":"verb","play":"verb"}
NP = ["det", "noun"]
VP = ["verb"] + NP
seq = NP + VP
S = ["NP", "VP"]

ary_words = stance.split(" ")
check_seq = [dic[word] for word in ary_words]

if check_seq == seq:
    print("S CFG is " , S)
    for word in ary_words:
        print(word , "is ", dic[word])