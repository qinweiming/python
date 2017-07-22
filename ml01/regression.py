import numpy
from numpy  import *
def loadDataSet(fileName):
    numFeat=len(open(fileName).readline().split("\t"))-1
    dataMat=[];labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split("\t")

        lineArr.append(float(curLine[0]))
        dataMat.append([float(curLine[0]),float(curLine[1])])
        labelMat.append([float(curLine[-1])])
    return  dataMat,labelMat
def standRegres(xArr,yArr):
    xMat=mat(xArr);yMat=mat(yArr).T
    xTx=xMat.T*xMat
    print("=========")
    print(xTx)
    if linalg.det(xTx)==0.0:
        print("")
        return
    ws=linalg.solve(xTx,xMat.T*yMat.T)
    return ws
xArr,yArr=loadDataSet("E:\\ex0.txt")
print(xArr)
print(yArr)
ws=standRegres(xArr,yArr)
print(ws)
import matplotlib.pyplot as plt
xMat=mat(xArr)
yMat=mat(yArr)
print("0000000")
print(yMat.T)
yHat=xMat*ws
fig=plt.figure()
ax=fig.add_subplot(111)
b=xMat[:,1].flatten().A[0]
print(b)
j=yMat.T[:,:].flatten().A[0]
print(j)
ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,:].flatten().A[0])
xCopy=xMat.copy()
xCopy.sort(0)
yHat=xCopy*ws
ax.plot(xCopy[:,1],yHat)
plt.show()


def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat=mat(xArr);yMat=mat(yArr).T
    m=shape(xMat)[0]
