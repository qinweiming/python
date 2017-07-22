from  math  import  log
import operator
def calcShannonEnt(dataSet):
    numEntries=len(dataSet);
    labelCounts={}
   #以下五行为所有可能分类创建字典
    for festVec in  dataSet:
        currentlabel=festVec[-1]
        if currentlabel not in labelCounts.keys():
            labelCounts[currentlabel]=0
            labelCounts[currentlabel]+=1
        shannonEnt=0.0
    for  key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        #以2为低求对数
        shannonEnt-=prob*log(prob,2)
    return shannonEnt
def createDataSet():
    dataset=[[1,1,"yes"],[1,1,"yes"],[1,0,"no"],[0,1,"no"],[0,1,"no"]]
    labels=["no surfacing","flippers"]
    return dataset,labels
mydat,labels=createDataSet()
shang=calcShannonEnt(mydat)
print(shang)


def splitDataSet(dataSet, axis, value):
    # 创建新的List对象
    retDataSet = []


    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return  retDataSet
def chooseBestFeatureToSplit(dataset):
    numFeatures=len(dataset[0])-1
    baseEntropy=calcShannonEnt(dataset)
    bestInfoGain=0.0;bestFeature=-1
    for i in range(numFeatures):
        #以下两行创建唯一的分类标签
        featList=[example[i] for  example in dataset]
        uniquevals=set(featList)
        newEntropy=0.0
        #以下五行计算每种hue分方式的信息熵
        for value in uniquevals:
            subDataSet=splitDataSet(dataset,i,value)
            prob=len(subDataSet)/float(len(dataset))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if (infoGain>bestInfoGain):
            #计算最好的信息熵
            bestInfoGain=infoGain
            bestInfoGain=i
    return  bestInfoGain
def majorityCnt(classList):
    classCount={}
    for  vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
            classCount[vote]+=1
    sortedClasscount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClasscount[0][0]
def createTree(dataset,labels):
    classlist=[example[-1] for example in dataset]
    #以下两行类别完全相同测停止继续划分
    if classlist.count(classlist[0])==len(classlist):
        return  classlist[0]
    #以下两行遍历完所有特征返回出现次数最多的
    if len(dataset[0])==1:
        return  majorityCnt(classlist)
    bestFeat=chooseBestFeatureToSplit(dataset)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    #得到所有列表的包含的所有属性值
    del (labels[bestFeat])
    featValues=[example[bestFeat] for example in dataset]
    uniquevals=set(featValues)
    for value in uniquevals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataset,bestFeat,value),subLabels)
    return myTree



