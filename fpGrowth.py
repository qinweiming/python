class treeNode:
    def __init__(self,nameValue,numOccur,parentNode):
        self.name=nameValue
        self.count=numOccur
        self.nodeLink=None
        self.parent=parentNode
        self.children={}
    def inc(self,numOccur):
        self.count+=numOccur
    def  disp(self,ind=1):
        print("")
        for child in self.children.values():
            child.disp(ind+1)
def createTree(dataSet,minSup=1):
    headerTable={}
    for trans in dataSet:
        for item in trans:
            headerTable[item]=headerTable.get(item,0)+dataSet[trans]
    #移除不满足最小值支持的元素项
    for  k in headerTable.keys():
        if headerTable[k]<minSup:
            del (headerTable[k])
    freqItemSet=set(headerTable.keys())
    #
    if len(freqItemSet)==0:return  None,None
    for k in headerTable:
        headerTable[k]=[headerTable[k],None]
    retTree=treeNode("Null Set",1,None)
    for tranSet,count in dataSet.items():
        localD={}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item]
    return retTree,headerTable
def updateTree(items,inTree,headerTable,count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]]=treeNode()
