import numpy as np
from  numpy import *
import random
def loadDataSet(fileName):
    dataMat=[];labelmat=[]
    fr=open(fileName)
    for  line in fr.readlines():
        lineArr=line.strip().split( "\t")
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelmat.append(float(lineArr[2]))
    return dataMat,labelmat
def  selectJrand(i,m):
    j=i
    while(j==i):
        j=int(random.uniform(0,m))
    return j
def clipAlpha(aj,H,L):
    if aj>H:
        aj=H
    if L>aj:
        aj=L
    return aj
dataArr,labelArr=loadDataSet("E:\\testSet.txt")
print(dataArr)
print(labelArr)
def smoSimple(dataMatIn,classlabels,c,toler,maxIter):
    dataMatrix=np.mat(dataMatIn);labelMat=np.mat(classlabels).transpose()
    b=0;m,n=shape(dataMatrix)
    alphas=mat(zeros((m,1)))
    iter=0
    while (iter<maxIter):
        alphaPairsChanged=0
        for i in range(m):
            fXi=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T))+b
            Ei=fXi-float(labelMat[i])
            



