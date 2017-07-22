import  pandas  as pd
import numpy  as np
import matplotlib.pyplot as plt
s=pd.Series([1,3,5,np.nan,6,8])
print(s)
datas=pd.date_range("20150101",periods=6)
print(datas)
print("=================")
print(np.__version__)
z=np.zeros(10)
print(z)
