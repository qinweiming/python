import  matplotlib.pyplot as plot
#以下三行是定义文本框和箭头格式
decisionNode=dict(boxstyle="sawtooth",fc="0.8")
leafNode=dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")
#以下两行绘制带箭头的注释
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords="axes fraction",xytext=centerPt,textcoords="axes fraction",
                            va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)
def createPlot():
    fig=plot.figure(1,facecolor="white")
    fig.clf()
    createPlot.ax1=plot.subplot(111,frameon=False)
    plotNode("决策点",(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode("叶节点",(0.8,0.1),(0.3,0.8),leafNode)
    plot.show()
createPlot()
def getNumLeafs(myTree):
    numLeafs=0;
    firstStr=myTree.keys()[0];
    secondDict=myTree[firstStr]
    for key in  secondDict.keys():
        #以下三行测试节点的数据类型是否为字典
         if type(secondDict[key]).__name__=="dict":
             numLeafs+=getNumLeafs(secondDict[key])
         else: numLeafs+=1
    return  numLeafs
def  getTreeDepth(myTree):
    maxDepth=0
    firstr=myTree.keys()[0]
    secondDict=myTree[firstr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=="dict":
            thisDepth=1+getTreeDepth(secondDict[key])
        else:thisDepth=1
        if thisDepth>maxDepth:maxDepth=thisDepth
    return maxDepth
def retrieveTree(i):
    listofTrees = [{"no surfacing": {0: "no", 1: {"flippers":{0: "no", 1: "yes"}}}}, {
        "no surfacing": {0: "no", 1: {"flippers":{0: {"head": {0: "no", 1: "yes"}}, 1: "no"}}}}]
    return listofTrees[i]
def classify(inputTree,featLabels,testVec):
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    #将标签字符串转换为索引
    featIndex=featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=="dict":
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:classLabel=secondDict[key]
    return  classLabel
def storeTree(inputTree,filename):
    import  pickle
    fw=open(filename,"w")
    pickle.dump(inputTree,fw)
    fw.close()
def grabTree(filename):
    import  pickle
    fr=open(filename)
    return pickle.load(fr)

