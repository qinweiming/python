from math import log


def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    print("[[[[[[[[[[[[[[[[[[[[[[")
    print(numEntries)
    labelCounts={}
    #以下五行为所有可能分类创建字典
    for  featVec in dataSet:
        print(featVec)
        currentLabel=featVec[-1]
        print("=========")
        print(currentLabel)
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=1
        else: labelCounts[currentLabel]+=1
        shannonEnt=0.0
    print("9999999999999999")
    print(labelCounts)
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt
def createDataSet():
    dataSet=[[1,1,"yes"],[1,1,"yes"],[1,0,"no"],[0,1,"no"],[0,1,"no"]]
    labels=["no surfacing","flippers"]
    return dataSet,labels
myDat,labels=createDataSet()
myDat[0][-1]="maybe"
print(myDat)
a=calcShannonEnt(myDat)
print(a)
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
n=splitDataSet(myDat,0,1)
print("pppppppppppppp")
print(n)