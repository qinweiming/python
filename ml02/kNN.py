from  numpy import *
import operator

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=["a","a","b","b"]
    return  group,labels
group,labels=createDataSet()
print(group)
print(labels)

def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    print("dataSet")
    print(dataSetSize)
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    print("diffmat")
    print(diffMat)
    sqDiffMat=diffMat**2
    print("sqdiffnat")
    print(sqDiffMat)
    sqDistances=sqDiffMat.sum(axis=1)
    print("sqdistance")
    print(sqDistances)
    distances=sqDistances**0.5
    print(distances)
    sortedDistIndicied=distances.argsort()
    print("sortedistanceIndi")
    print(sortedDistIndicied)
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicied[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
#inX用与分类的输入向量，输入的训练样本集dataSet,标签向量为labels,最后的参数k表示用于选择最近令法数目

a=classify0([0,0],group,labels,3)
print(a)

def file2matrix(filename):
    fr=open(filename)
    arrayolines=fr.readlines()
    numberOfLines=len(arrayolines)
    returnMat=zeros((numberOfLines,3))
    classlabelVector=[]
    index=0
    for line in arrayolines:
        line=line.strip()
        listFromLine=line.split("\t")
        returnMat[index,:]=list(listFromLine[0:3])
        classlabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classlabelVector
datingDataMat,datinglabels=file2matrix("E:\\datingTestSet2.txt")
print(datingDataMat)

def autoNorm(dataSet):
    minvals=dataSet.min(0)
    print(minvals)
    maxVals=dataSet.max(0)
    print(maxVals)
    ranges=minvals-minvals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minvals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return  normDataSet,ranges,minvals

normMat,ranges,minVals=autoNorm(datingDataMat)





import  matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datinglabels),15.0*array(datinglabels))
plt.show()



def img2vector(filename):
    returnVect=zeros((1,1024))
    fr=open(filename)
    for  i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect

