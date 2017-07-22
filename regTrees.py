from numpy import *
def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in  fr.readlines():
        curLine=line.strip().split("\t")
        fltLine=map(float,curLine)
        dataMat.append(fltLine)
    return dataMat
def binSplitDataSet(dataSet,feature,value):
    mat0=dataSet[nonzero(dataSet[:,feature]>value)[0],:][0]
    mat1=dataSet[nonzero(dataSet[:,feature]<=value)[0],:][0]
    return mat0,mat1
def regLeaf(dataSet):
    return mean(dataSet[:,-1])
def regErr(dataSet):
    return var(dataSet[:,-1])*shape(dataSet)[0]
def chooseBestSplit(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    tolS=ops[0];tolN=ops[1]
    if len(set(dataSet[:,-1].T.tolist()[0]))==1:
        return None,leafType(dataSet)
    m,n=shape(dataSet)
    S=errType(dataSet)
    bestS=inf;bestIndex=0;bestValue=0
    for featIndex in range(n-1):
        for splitVal in set(dataSet[:,featIndex]):
            mat0,mat1=binSplitDataSet(dataSet,featIndex,splitVal)
            if (shape(mat0)[0]<tolN)or(shape(mat1)[0]<tolN):continue
            news=errType(mat0)+errType(mat1)
            if news<bestS:
                bestIndex=featIndex
                bestValue=splitVal
                bestS=news
    if (S-bestS)<tolS:
        return None,leafType(dataSet)
    mat0,mat1=binSplitDataSet(dataSet,bestIndex,bestValue)
    if (shape(mat0)[0]<tolN)or(shape(mat1)[0]<tolN):
        return  None,leafType(dataSet)
    return bestIndex,bestValue
def regTreeEval(model,inDat):
    return float(model)
def modelTreeEval(model,inDat):
    n=shape(inDat)[1]
    X=mat(ones((1,n+1)))
    X[:,1:n+1]=inDat
    return float(X*model)



