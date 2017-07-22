import random

from numpy import *
#http://www.cnblogs.com/berkeleysong/articles/3251245.html

def  loadDataSet(fileName):
    dataMat=[];labelmat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split("\t")
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelmat.append(float(lineArr[2]))
    return  dataMat,labelmat
def selectJrand(i,m):
    j=i
    while(j==i):
        j=int(random.uniform(0,m))
    return j
def  clipAlpha(aj,H,L):
    if aj>H:
        aj=H
        if  L>aj:
            aj=L
    return   aj
def smoSimple(dataMatIn,classLabels,c,toler,maxIter):
    dataMatrix=mat(dataMatIn);labelMat=mat(classLabels).transpose()
    b=0;m,n=shape(dataMatrix)
    alphas=mat(zeros((m,1)))
    iter=0
    while (iter<maxIter):
        alphaPairsChanged=0
        for i in range(m):
            fXi=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T))+b
            Ei=fXi-float(labelMat[i])
            #如果alpha可以更新进入优化过程
            if ((labelMat[i]*Ei<-toler) and(alphas[i]<c))or((labelMat[i]*Ei>toler)and(alphas[i]>0)):
                #随机选择第二个alpha
                j=selectJrand(i,m)
                fXj=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T))+b
                Ej=fXj-float(labelMat[j])
                alphaIold=alphas[i].copy();
                alphaJold=alphas[j].copy();
                #以下六行保证alpha在0与c之间
                if (labelMat[i]!=labelMat[j]):
                    L=max(0,alphas[j]-alphas[i])
                    H=min(c,c+alphas[j]-alphas[i])
                else:
                    L=max(0,alphas[j]+alphas[i]-c)
                    H=min(c,alphas[j]+alphas[i])
                if L==H: print("L==H");continue
                eta=2.0*dataMatrix[i,:]*dataMatrix[j,:].T-dataMatrix[i,:]*dataMatrix[i,:].T-dataMatrix[j,:]*dataMatrix[j,:].T
                if eta>=0:print()
                alphas[j]-=labelMat[j]*(Ei-Ej)/eta
                alphas[j]=clipAlpha(alphas[j],H,L)
                if (abs(alphas[j]-alphaJold)<0.00001):print("j")
                #对i进行修改，修改量与j相同，但方向相反
                alphas[i]+=labelMat[j]*labelMat[i]*(alphaJold-alphas[j])
                b1=b-Ei-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*(alphas[j]-alphaJold)*dataMatrix[j,:].T-labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                b2=b-Ej-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T-labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0<alphas[i]) and (c>alphas[i]):b=b1
                elif(0<alphas[j])and(c>alphas[j]):b=b2
                else:b=(b1+b2)/2.0
                alphaPairsChanged+=1
                print("")
            if(alphaPairsChanged==0):iter+=1
            else:iter=0
            print("")
        return   b,alphas
class optStruct:
    def __init__(self,dataMatIn,classLabels,C,toler):
        self.X=dataMatIn
        self.labelMat=classLabels
        self.c=C
        self.tol=toler
        self.m=shape(dataMatIn)[0]
        self.alphas=mat(zeros((self.m,1)))
        self.b=0
        #误差缓存
        self.eCache=mat(zeros((self.m,2)))
    def calcEk(oS,k):
        fXk=float(multiply(oS.alphas,oS.labelMat).T*(oS.X*oS.X[k,:].T))+oS.b
        Ek=fXk-float(oS.labelMat[k])
        return  Ek
    def  selectJ(i,oS,Ei):
        #内循环中的启发试fangfa
        maxk=-1;maxDeltaE=0;Ej=0
        oS.eCache[i]=[1,Ei]
        validEcacheList=nonzero(oS.eCache[:,0].A)[0]
        if (len(validEcacheList))>1:
            for k in validEcacheList:
                if k==i:continue
                Ek=optStruct.calcEk(oS,k)
                deltaE=abs(Ei-Ek)
                if (deltaE>maxDeltaE):
                    maxk=k;maxDeltaE=deltaE;Ej=Ek
            return maxk,Ej
        else:
            j=selectJrand(i,oS.m)
            Ej=optStruct.calcEk(oS,j)
        return j,Ej
    def updateEk(oS,k):
        Ek=optStruct.calcEk(oS,k)
        oS.eCache[k]=[1,Ek]
    def innerL(i,oS):
        Ei=optStruct.calcEk(oS,i)
        if ((oS.labelMat[i]*Ei<-oS.tol)and(oS.alphas[i]<oS.C) )or((oS.labelMat[i]*Ei>oS.tol)and(oS.alphas[i]>0)):
            j,Ej=selectJrand(i,oS,Ei)
            alphaIold=oS.alphas[i].copy();alphaJold=oS.alphas[j].copy();
            if (oS.labelMat[i]!=oS.labelMat[j]):
                L=max(0,oS.alphas[j]-oS.alphas[i])
                H=min(oS.C,oS.C+oS.alphas[j]-oS.alphas[i])
            else:
                L=max(0,oS.alphas[j]+oS.alphas[i]-oS.C)
                H=min(oS.C,oS.alphas[j]+oS.alphas[i])
            if L==H:return 0
            eta=2.0*oS.X[i,:]*oS.X[j,:].T-oS.X[i,:]*oS.X[i,:].T-oS.X[j,:]*oS.X[j,:].T
            if eta>=0:print("")
            oS.alphas[j]-=oS.labelMat[j]*(Ei-Ej)/eta
            oS.alphas[j]=clipAlpha(oS.alphas[j],H,L)
            optStruct.updateEk(oS,j)
            if (abs(oS.alphas[j]-alphaJold)<0.0001):
                print("");return 0
            oS.alphas[i]+=oS.labelMat[j]*oS.labelMat[i]*(alphaJold-oS.alphas[j])
            optStruct.updateEk(oS,i)
            b1=oS.b-Ei-oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.X[i,:]*oS.X[i,:].T-oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.X[i,:]*oS.X[j,:].T
            b2=oS.b-Ej-oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.X[i,:]*oS.X[i,:].T-oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.X[i,:]*oS.X[j,:].T
            if (0<oS.alphas[i])and (oS.C>oS.alphas[i]):oS.b=b1
            elif(0<oS.alphas[j])and(oS.C>oS.alphas[j]):oS.b=b2
            else:oS.b=(b1+b2)/2.0
            return 1
        else:return 0
def smoP(dataMatIn,classLabels,C,toler,maxIter,kTup=("lin",0)):
    oS=optStruct(mat(dataMatIn),mat(classLabels).transpose(),C,toler)
    iter=0
    entireSet=True;alphaPairsChanged=0
    while(iter<maxIter)and((alphaPairsChanged>0)or(entireSet)):
        alphaPairsChanged=0
        if entireSet:
            for i in range(oS.m):
                alphaPairsChanged+=optStruct.innerL(i,oS)
            print()
            iter+=1
        else:
            nonBoundIs=nonzero((oS.alphas.A>0)*(oS.alphas.A<C))[0]
            for i in nonBoundIs:
                alphaPairsChanged+=optStruct.innerL(i,oS)
                iter+=1
            if entireSet:entireSet=False
            elif(alphaPairsChanged==0):
                entireSet=True
        return oS.b,oS.alphas
def loadImages(dirName):
    from os import listdir
    hwLabels=[]
    trainingFileList=listdir(dirName)
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split(".")[0]
        classNumStr=int(fileStr.split("_")[0])
        if classNumStr==9:hwLabels.append(-1)
        else:hwLabels.append(1)
        trainingMat[i,:]
        return   trainingMat,hwLabels
def testDigits(kTup=("rbf",10)):
    dataArr,labelArr=loadDataSet("train")
    b,alphas=smoP(dataArr,labelArr,200,0.0001,10000,kTup)
    datMat=mat(dataArr);labelMat=mat(labelArr).transpose()
    svInd=nonzero(alphas.A>0)[0]
    sVs=datMat[svInd]
    labelSV=labelMat[svInd]
    shape(sVs)[0]
    m,n=shape(datMat)
    errorCount=0
   # for i in range(m):


