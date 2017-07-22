from  PIL import  Image
im=Image.open("E:\\2.jpg")
(x,y) = im.size #read image size
x_s = 300 #define standard width
y_s = y * x_s / x

im.resize((x_s,y_s),Image.ANTIALIAS).save("E:\\5.jpg")
print(im.size)

