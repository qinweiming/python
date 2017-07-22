from numpy import *
import operator
def  createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=["a","a","b","b"]
    return group,labels
group,labels=createDataSet()
#print(group)
def classify0(inX,dataset,labels,k):
    datasetsize=dataset.shape[0]
    #以下三行进行距离计算
    diffmat=tile(inX,(datasetsize,1))
    dataset
    sqdiffmat=diffmat**2
    sqdistances=sqdiffmat.sum(axis=1)
    distances=sqdistances**0.5
    sorteddistindicies=distances.argsort()
    classCount={}
    #以下两行选择距离最小的K个点
    for i in range(k):
        votellabel = labels[sorteddistindicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1
    sortedclasscount=sorted(classCount.iteritems(),
           key=operator.itemgetter(1), reverse=True)
    return sortedclasscount[0][0]
#classify0([0,0],group,labels,3)
def file2matrix(filename):
    fr=open(filename)
    arrayolines=fr.readline()
    numberoflines=len(arrayolines)
    returnmat=zeros((numberoflines,3))
    classlabelvector=[]
    index=0
    #以下三行解析文件数据列表
    for line in arrayolines:
        line=line.strip()
        listfromline=line.split("\t")
        returnmat[index,:]=listfromline[0:3]
        classlabelvector.append(int(listfromline[-1]))
        index+=1
    return  returnmat,classlabelvector
file2matrix("E:\\3.txt")