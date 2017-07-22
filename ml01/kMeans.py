from numpy import *

def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split("\t")
        fltLine=list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat
def distEclud(vecA,vecB):
    return square(sum(power(vecA-vecB),2))
def randCent(dataSet,k):
    n=shape(dataSet)[1]
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(dataSet[:,j])-minJ)
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    return centroids
def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    centroids=createCent(dataSet,k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(m):
            minDist=inf;minIndex=-1
            for j in range(k):
                distJI=distMeas(centroids[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist=distJI;minIndex=j
            if clusterAssment[i,0]!=minIndex:
                clusterChanged=True
                clusterAssment[i,:]=minIndex,minDist**2
                print(centroids)
                for cent in range(k):
                    ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
                    centroids[cent,:]=mean(ptsInClust,axis=0)
    return centroids,clusterAssment
def bikmeans(dataSet,k,distMeas=distEclud):
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    #以下两行创建一个初始zu
    centroid0=mean(dataSet,axis=0).tolist()[0]
    centList=[centroid0]
    for j in range(m):
        clusterAssment[j,1]=distMeas(mat(centroid0),dataSet[j,:])**2
    while(len(centList)<k):
        lowestSSE=inf
        for i in range(len(centList)):
            ptsInCurrCluster=dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]
            centroidMat,splitClustAss=kMeans(ptsInCurrCluster,2,distMeas)
            sseSplit=sum(splitClustAss[:,1])
            sseBotSplit=sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
            print("")


dataMat=mat(loadDataSet("E:\\testSet.txt"))
print(dataMat)
cent=mean(dataMat,axis=0).tolist()
print("==")
print(cent)
print("==")
#myCentroids,clustAssing=kMeans(dataMat,4)
y=randCent(dataMat,2)
print(y)