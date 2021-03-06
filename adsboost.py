from  numpy import *

def loadSimData():
    datMat=matrix([[1.,2.1],[2.,1.1],[1.3,1.],[1.,1.],[2.,1.]])
    classLabels=[1.0,1.0,-1.0,-1.0,1.0]
    return datMat,classLabels
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArry=ones((shape(dataMatrix)[0],1))
    if threshIneq=="lt":
        retArry[dataMatrix[:,dimen]<=threshVal]=-1.0
    else:
        retArry[dataMatrix[:,dimen]>threshVal]=-1.0
    return retArry
def buildStump(dataArr,classLabels,D):
    dataMatrix=mat(dataArr);labelMat=mat(classLabels).T
    m,n=shape(dataMatrix)
    numSteps=10.0;bestStump={};bestClasEst=mat(zeros((m,1)))
    for i in range(n):
        rangeMin=dataMatrix[:,i].min();rangeMax=dataMatrix[:,i].max();
        stepSize=(rangeMax-rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):
            for inequal in ["lt","gt"]:
                threshVal=(rangeMin+float(j)*stepSize)
                predictedVals=stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr=mat(ones((m,1)))
                errArr[predictedVals==labelMat]=0
                weightedErroe=D.T*errArr
def  adaBoostTrainDS(dataArr,classLabels,numIt=40):
     weakClassArr=[]
     m=shape(dataArr)[0]
     D=mat(ones((m,1))/m)
     aggClassEst=mat(zeros((m,1)))
     for i in range(numIt):
         bestStump,error,classEst=buildStump(dataArr,classLabels,D)
         print("D",D.T)
         alpha=float(0.5*log((1.0-error)/max(error,1e-16)))
         bestStump["alpha"]=alpha
         weakClassArr.append(bestStump)
         print("classEst",classEst.T)
         #以下两行为下一次迭代计算d
         expon=multiply(-1*alpha*mat(classLabels).T,classEst)
         D=multiply(D,exp(expon))
         D=D/D.sum()
         #以下五行错误率累加计算
         aggClassEst+=alpha*classEst
         print("aggClassEst",aggClassEst.T)
         aggErrors=multiply(sign(aggClassEst))!=mat(classLabels).T,ones((m,1))
         errorRate=aggErrors.sum()/m
         print("total error",errorRate,"\n")
         if errorRate==0.0:break
     return   weakClassArr
def adaClassify(datToClass,classifierArr):
    dataMatrix=mat(datToClass)
    m=shape(dataMatrix)[0]
    aggClassEst=mat(zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst=stumpClassify(dataMatrix,classifierArr[i]["dim"],classifierArr[i]["thresh"],classifierArr[i]["ineq"])
        aggClassEst+=classifierArr[i]
        ["alpha"]*classEst
        print(aggClassEst)
    return sign(aggClassEst)
def loadDataSet(fileName):
    numFeat=len(open(fileName).readline().split("\t"))
    dataMat=[];labelMat=[]
    fr=open(fileName)
    for line in fr.readline():
        lineArr=[]
        curLine=line.strip().split("\t")
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat
def plotROC(presStrengths,classLabels):
    import matplotlib.pyplot as plt
    cur=(1.0,1.0)
    ySum=0.0
    numPosClas=sum(array(classLabels)==1.0)
    yStep=1/float(numPosClas)
    xStep=1/float(len(classLabels)-numPosClas)
    #获取排好寻的索引
    sortedIndicies=presStrengths.argsort()
    fig=plt.figure()
    fig.clt()
    ax=plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index]==1.0:
            delX=0;delY=yStep;
        else:
            delX=xStep;delY=0;
            ySum+=cur[1]
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],C="b")
        cur=(cur[0]-delX,cur[1]-delY)
