from PIL import Image
import numpy

img = Image.open("E:\\2.jpg")
coloe1=[]
for i in range(300):
    for j in range(300):
        color = []
        matt=[]
        r, g, b = img.getpixel((i, j))
        matt2=[]
        matt2.append(r)
        matt2.append(g)
        matt2.append(b)
        if (b > g and b > r):  # 对蓝色进行判断
            b = 127
            g = 127
            r = 127
        matt.append(i)
        matt.append(j)
        color.append(matt)
        color.append(matt2)
        coloe1.append(color)
        #color.extend(matt2)

        img.putpixel((i, j), (r, g, b))
#print(numpy.mat(color))
print(matt)
print("=======")
print(matt2)
print("---")

print(numpy.mat(coloe1))
#img.show()