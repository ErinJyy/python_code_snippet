def p(*c):
    print(*c)
# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])

    # C1.sort()
    return list(map(frozenset, C1))#use frozen set so we
                            #can use it as a key in a dict

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can]=1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1==L2:
                retList.append(Lk[i] | Lk[j])
    return retList

def apriori(dataSet, minSupport = 0.05):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        # p('CK=',Ck)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
        # p('Lk=',Lk)
        supportData.update(supK)
        L.append(Lk)
        # p("L=",L)
        k += 1
    return L, supportData


# L是已经去掉非频繁项集   C是没有去掉，全部的

# dataSet = loadDataSet()
# # p(dataSet)
# C1 = createC1(dataSet)
# # p(C1)
# D = list(map(set,dataSet))
# # p(D)
# L1,suppData0 = scanD(D, C1, 0.5)




def generateRules(L, supportData, minConf=0.5):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

def calcConf(freqSet, H, supportData, brl, minConf=0.5):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf:
            print(freqSet-conseq,'-->',conseq,'conf:',conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.5):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
p('----------------')

# L, supportData = apriori(dataSet)

# rules = generateRules(L, supportData, minConf=0.5)


import xlrd
file1 = pd.read_excel(r'D:\pythonPractice\test_data\OnlineRetail.xlsx')
resDict = dict()
lastItem = -1
index = 0
for i, v1 in file1[['CustomerID','StockCode']].iterrows():
    for j, v2 in v1.iteritems():
        if index % 2 == 0:
            lastItem = v2
        else:
            if lastItem not in resDict:
                resDict[lastItem] = []
            resDict[lastItem].append(v2)
        index += 1


dataSet = list(resDict.values())
p('----------c1')
C1 = createC1(dataSet)

L, supportData = apriori(dataSet)

rules = generateRules(L, supportData, minConf=0.7)
p(rules)

















