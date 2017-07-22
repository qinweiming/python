from numpy import *
import operator

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=["A","A","B","B"]
    return group,labels
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    print(str(dataSetSize)+"iii")
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    #print(tile(inX,(dataSetSize,1)))
    print(diffMat)
    sqDiffmat=diffMat**2
    print(sqDiffmat)
    sqDistances=sqDiffmat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    classCount={}
    ###########################
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount= sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount

def file2matrix(filename):
    fr=open(filename)
    arrayOlines=fr.readlines()
    print(arrayOlines)
    numberOfLines=len(arrayOlines)
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOlines:
        line=line.strip()
        listFormLine=line.split("\t")
        returnMat[index,:]=listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1]))
        index+=1
    return  returnMat,classLabelVector
dataingDatamat,datinglabels=file2matrix("E:\\datingTestSet2.txt")
print(dataingDatamat)
print("=========================================")
print(datinglabels)
import matplotlib
import  matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(dataingDatamat[:,1],
dataingDatamat[:,2])
plt.show()

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    rangs=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(rangs,(m,1))
    return normDataSet,rangs,minVals
def datingClassTest():
    hoRatio=0.10
    datingDataMat,datingLabels=file2matrix("")


