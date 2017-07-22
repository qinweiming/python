class treeNode():
    def __init__(self,feat,val,right,left):
        featureToSplitOn=feat
        valueOfSplit=val
        rightBranch=right
        leftBranch=left
from numpy import *
def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split("\t")
        fltLine=map(float,curLine)
        dataMat.append(fltLine)
    return dataMat
def binSplitDataSet(dataSet,feature,value):
    mat0=dataSet[nonzero(dataSet[:,feature]>value)[0],:][0]
    mat1=dataSet[nonzero(dataSet[:,feature]<=value)[0],:][0]
    return mat0,mat1
#def createTree(dataSet,regLeaf,regErr,ops=(1,4)):
    #feat,val=chooseBestSplit(dataSet,leafType,errType,ops)
    #if feat==None:return val
    #retTree={}
    #retTree["spInd"]=feat
    #retTree["spVal"]=val
    #lSet,rSet=binSplitDataSet(dataSet,feat,val)
    #retTree["left"]=createTree(lSet,regLeaf,regErr,ops)
    #retTree["right"]=createTree(rSet,regLeaf,regErr,ops)
    #return  retTree
def regLeaf(dataSet):
    return mean(dataSet[:-1])
def  regErr(dataSet):
    return  var(dataSet[:,-1])*shape(dataSet)[0]





testmat=mat(eye(4))
print(testmat)
mat0,mat1=binSplitDataSet(testmat,1,0.5)
print(mat0)
print(mat1)