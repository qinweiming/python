from math  import  *

import os

from numpy import *


def  loadDataSet():
    dataMat=[];labelMat=[]
    fr=open("E:\\testSet.txt")
    for  line in  fr.readlines():
      #  print("line")
       # print(line)
        lineArr=line.strip().split()

        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])

        labelMat.append(int(lineArr[2]))
    return  dataMat,labelMat
def sigmoid(inX):
    return 1.0/(1+exp(-inX))
def gradAscent(dataMatIn,classlabels):
    datamatrix=mat(dataMatIn)
    labelmat=mat(classlabels).transpose()
    m,n=shape(datamatrix)
    alpha=0.001
    maxCycles=500
    weights=ones((n,1))
    for  k in  range(maxCycles):
        h=sigmoid(datamatrix*weights)
        error=(labelmat-h)
        weights=weights+alpha*datamatrix.transpose()*error
    return  weights
def plotBestFit(wei):
    import matplotlib.pyplot as plt
    weights=wei.getA()
    dataMat,labelmat=loadDataSet()
    dataArr=array(dataMat)
    n=shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if  int(labelmat[i])==1:
            xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,2]);ycord2.append(dataArr[i,2])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c="red")
    ax.scatter(xcord2,ycord2,s=30,c="green")
    x=arange(-3.0,3.0,0.1)
    y=(-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel("x1");plt.ylabel("x2");
    plt.show()

def stocGradAscent0(datamatrix,classLabels):
    m,n=shape(datamatrix)
    alpha=0.01
    weights=ones(n)
    for i in range(m):
        h=sigmoid(sum(datamatrix[i]*weights))
        error=classLabels[i]-h
        weights=weights+alpha*error*datamatrix[i]
    return weights
def stocGradAsecnt1(dataMatrix,classLabels,numIter=150):
    m,n=shape(dataMatrix)
    weights=ones(n)
    for j in range(numIter):
        dataIndex=range(m)
        for i in range(m):
            alpha=4/(1.0+j+i)+0.01
            randIndex=int(random.uniform(0,len(dataIndex)))
            h=sigmoid(sum(dataMatrix[randIndex]*weights))
            error=classLabels[randIndex]-h
            weights=weights+alpha*error*dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

def classifyVector(inX,weights):
    prob=sigmoid(sum(inX*weights))
    if prob>0.5:return 1.0
    else:return 0.0
def colicTest():
    frTrain=open("E:\\horseColicTraining.txt")
    frTest=open("E:\\horseColicTest.txt")
    trainingSet=[];trainingLabels=[]
    for  line  in frTrain.readlines():
        currLine=line.strip().split("\t")
        lineArr=[]
        for  i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights=stocGradAsecnt1(array(trainingSet),trainingLabels,500)
    errorCount=0;numtestVec=0.0
    for line in frTest.readlines():
        numtestVec+=1.0
        currLine=line.strip().split("\t")
        lineArr=[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr),trainWeights))!=int(currLine[21]):
            errorCount+=1
    errorRate=(float(errorCount)/numtestVec)
    print()
    return errorRate
def multiTest():
    numTests=10;errorSum=0.0
    for k in range(numTests):
        errorSum+=colicTest()


dataArr,labelmat=loadDataSet()
w=gradAscent(dataArr,labelmat)
#plotBestFit(w)
b=mat(w)
c=b.getA()
print(w)
print(b.getA())
plotBestFit(b)