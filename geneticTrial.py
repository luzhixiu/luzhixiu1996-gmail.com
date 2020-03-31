# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:44:52 2020

@author: lu
"""
import random as rd

luckyN="1100001001"

startingParents=[]

#create a list of size N numbers with swithces of digitt size n_switch to 
#from luckyN

def mutate(seed):
    randIndex=rd.randint(0,len(seed)-1)
    if seed[randIndex]== '0':
        seed=seed[:randIndex]+'1'+seed[randIndex+1:]
    else:
        seed=seed[:randIndex]+'0'+seed[randIndex+1:]
    return seed
    


def creatSeeds(luckyN,N,n_switch):
    resultList=[]
    for i in range(N):
        seed=luckyN
        for k in range(n_switch):
            seed=mutate(seed)
        resultList.append(seed)
    return resultList

def mate(p1,p2,mutationRate=0.1):
    offSpring=""
    for i in range(len(p1)):
        randParent=rd.randint(0,1)
        if randParent==0:
            offSpring+=p1[i]
        else:
            offSpring+=p2[i]
    for i in range(int(100*mutationRate)):
        if rd.randint(0,101)==1:
            offSpring=mutate(offSpring)
    return offSpring

#return the number of mistaches
def match(s1,s2):
    s1=str(s1)
    s2=str(s2)
    cnt=0
    for i in range(len(s1)):
        if not s1[i]==s2[i]:
            cnt+=1
#    print "%d mismatch between %s and %s"%(cnt,s1,s2)
    return cnt



def eliminate(lst,luckyN,threshold=5):
    survivialList=[]
    for s in lst:
        mismatches=match(str(luckyN),str(s))
#        print mismatches
        if int(mismatches) < int(threshold):
#            print "!"
            survivialList.append(s)
#            print s

    return survivialList
    
        
l1=creatSeeds(luckyN,3,2)
b1=creatSeeds(luckyN,3,4)



lList=[]


def populate(l1,l2):
    offSpringList=[]

    for i in (l1):
        randomMate1= l2[rd.randint(0,len(l2)-1)]
        randomMate2= l2[rd.randint(0,len(l2)-1)]
        offSpringList.append(mate(i,randomMate1))
        offSpringList.append(mate(i,randomMate2))
            
#    offSpringList=eliminate(lList,luckyN,5)
    return offSpringList




gList=[]
bList=[]
eliList1=[]
eliList2=[]
for i in range(0,15):
    l1=populate(l1,l1)
    len1=len(l1)
    l1=eliminate(l1,luckyN)
    len2=len(l1)
    eliList1.append(len1-len2)
    gList.append(len(l1))
    b1=populate(b1,b1)
    len1=len(b1)
    b1=eliminate(b1,luckyN)
    len2=len(b1)
    eliList2.append(len1-len2)
    bList.append(len(b1))

import matplotlib.pyplot as plt


print eliList1
print eliList2

plt.figure()

plt.plot(gList,label="More Fitted Population")
plt.plot(bList,label="Less Fitted Population")
plt.legend()
plt.title("Population Growth Graph (mutation rate = 0.1)")
plt.xlabel("Generation")
plt.ylabel("Size of Population")
plt.show()

plt.plot(eliList1,label="More Fitted Population")
plt.plot(eliList2,label="Less Fitted Population")
plt.legend()
plt.title("Numbers of Individuals Eliminated by Selection per Generation")
plt.xlabel("Generation")
plt.ylabel("Size of Population")
plt.show()







