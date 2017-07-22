from  numpy import *
import matplotlib.pyplot  as plt


# huoqushuju
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat


def disEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def ranCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(array(dataSet)[:, j])
        rangeJ = float(max(array(dataSet)[:, j]) - minJ)
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
    return centroids


def kmeans(dataset, k, distMeas=disEclud, createCent=ranCent):
    m = shape(dataset)[0]
    clusterAssment = mat(zeros((m, 2)))  # create mat to assign data points
    centroids = createCent(dataset, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf;
            minIndex = -1
            for j in range(k):
                distJI = distMeas(array(centroids)[j, :], array(dataset)[i, :])
                if distJI < minDist:
                    minDist = distJI;
                    minIndex = j
                if clusterAssment[i, 0] != minIndex: clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist ** 2
        print(centroids)

        #         print nonzero(array(clusterAssment)[:,0]
        for cent in range(k):  # recalculate centroids
            ptsInClust = dataSet[
                nonzero(array(clusterAssment)[:, 0] == cent)[0][0]]  # get all the point in this cluster

            centroids[cent, :] = mean(ptsInClust, axis=0)  # assign centroid to mean
    id = nonzero(array(clusterAssment)[:, 0] == cent)[0]
    return centroids, clusterAssment, id


def plotBestFit(dataSet, id, centroids):
    dataArr = array(dataSet)
    cent = array(centroids)
    n = shape(dataArr)[0]
    n1 = shape(cent)[0]
    xcord1 = [];
    ycord1 = []
    xcord2 = [];
    ycord2 = []
    xcord3 = [];
    ycord3 = []
    j = 0
    for i in range(n):
        if j in id:
            xcord1.append(dataArr[i, 0]);
            ycord1.append(dataArr[i, 1])
        else:
            xcord2.append(dataArr[i, 0]);
            ycord2.append(dataArr[i, 1])
        j = j + 1
    for k in range(n1):
        xcord3.append(cent[k, 0]);
        ycord3.append(cent[k, 1])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    ax.scatter(xcord3, ycord3, s=50, c='black')

    plt.xlabel('X1');
    plt.ylabel('X2');
    plt.show()


if __name__ == '__main__':
    dataSet = loadDataSet('E:\\2.txt')
    # #     print randCent(dataSet,2)
    #      print dataSet
    #
    #      print  kMeans(dataSet,2)
    a = []
    b = []
    a, b, id = kmeans(dataSet, 2)
    plotBestFit(dataSet, id, a)
