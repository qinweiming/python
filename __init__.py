import pandas as pd
import sys
import fibo
data={"name":["jhon","anna","peter","linda"],"location":["new york","pairs","berlin","london"],"age":[23,34,21,33]}
data_pands=pd.DataFrame(data)
print(data_pands)
print("=================================")
basket={"apple","orange","apple","pear","orange","banana"}#集合set的写法，没有重复的元素
print(basket)
print("orange" in basket)
a=set("abracadabra",)
print(a)
print("==============================")
tel={"jack":4098,"sape":4139}
tel["jim"]=90888
for  k,v  in  tel.items():
    print(k,v)
print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[")
fibo.fib(1000)
print(fibo.__name__)
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
s="hello,world"
aa=str(s)
print(aa)
print("99999999999999999999999999999999999999")
f=open("E:\\1.txt")
s=f.readline()
i=int(s.strip())
print(i)