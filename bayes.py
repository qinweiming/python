from numpy import *


def loadDataSet():
    postinglist=[["my","dog","has","flea","problems","help","please"],["maybe","not","take","him",
    "to","dog","park","stupid"],["my","dalmation","is","so","cute","i","love","him"],["stop","posting","stupid","worthless","garbage"],
                 ["mr","licks","ate","my","steak","how","to","stop","him"],["quit","buying","worthless","dog","food","stupid"]]
    classVec=[0,1,0,1,0,1]
    return postinglist,classVec
def createVocabList(dataSet):
    #创建一个空集
    vocabSet=set([])
    for document in dataSet:
        #创建两个集合的并集
         vocabSet=vocabSet|set(document)
    return  list(vocabSet)
def setOfWord2Vec(vocabList,inputSet):
    #创建一个其中所含元素都为0的向量
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if  word  in  vocabList:
            returnVec[vocabList.index(word)]=1
        else:print("the word:%s is not in my vocabulary" %word)
    return returnVec
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    #以下两行初始化gailv
    p0Num=zeros(numWords);p1Num=zeros(numWords)
    p0Denom=0.0;p1Denom=0.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            #以下两行向量相加
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    p1Vect=p1Num/p1Denom#change to log()
    p0Vect=p0Num/p0Denom
    return  p0Vect,p1Vect,pAbusive
def classifyNB(vec2classify,p0Vec,p1Vec,pClass1):
    #元素相乘
    p1=sum(vec2classify*p1Vec)+log(pClass1)
    p0=sum(vec2classify*p0Vec)+log(1.0-pClass1)
    if p1>p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts,listClasses=loadDataSet()
    myVocablist=createVocabList(listOPosts)
    trainMat=[]
    for  postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocablist,postinDoc))
    p0V,p1V,pAb=trainNB0(array(trainMat),array(listClasses))
    testEntry=["love","my","dalmation"]
    thisDoc=array(setOfWord2Vec(myVocablist,testEntry))
    print(testEntry,"classified as:",classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry=["stupid","garbage"]
    thisDoc=array(setOfWord2Vec(myVocablist,testEntry))
    print(testEntry,"classified as:",classifyNB(thisDoc,p0V,p1V,pAb))


def bagOfWords2VecMN(vocabList,inputSet):
    returnVec=[0]*(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
    return returnVec
def textParse(bigString):
    import re
    listOfTokens=re.split(r"\w",bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]
def spamTest():
    docList=[];classList=[];fullText=[]
    for i in range(1,26):
        #以下七行是导入并解析文本文件
        wordList=textParse(open("").read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList=createVocabList(docList)
    trainingSet=range(50);testSet=[]
    #以下四行是随机构建训练机
    for i in range(10):
        randIndex=int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[];trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWord2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
        p0V,p1V,pSpam=trainNB0(array(trainMat),array(trainClasses))
        errorCount=0
        #以下四行是对测试机进行分类
        for docIndex  in  testSet:
            wordVector=setOfWord2Vec(vocabList,docList[docIndex])
            if classifyNB(array(wordVector),p0V,p1V,pSpam)!=classList[docIndex]:
                errorCount+=1
            print("the error rate  is ",float(errorCount)/len(testSet))


