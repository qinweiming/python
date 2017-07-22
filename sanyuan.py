import pandas as pd
import seaborn as  sns
import matplotlib.pyplot as  plt
from  sklearn.cross_validation import  train_test_split
from sklearn.linear_model  import LinearRegression



# display the first 5 rows
data=pd.read_csv("E:\\Advertising.csv")
print(data.head())
# check the shape of the DataFrame(rows, colums)
print(data.shape)
sns.pairplot(data,x_vars=['TV','Radio','Newspaper'],y_vars="Sales",size=7,aspect=0.8,kind="reg")
#plt.show()
#create a python list of feature names
feature_cols=["TV","Radio","Newspaper"]
# use the list to select a subset of the original DataFrame
X = data[feature_cols]
print( X.head())
# check the type and shape of X
print (type(X)  )
print( X.shape )
# select a Series from the DataFrame
y = data['Sales']
# equivalent command that works if there are no spaces in the column name
y = data.Sales
# print the first 5 values
print(y.head())
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=1)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
linereg=LinearRegression()
model=linereg.fit(X_train,y_train)
print(linereg.intercept_)
print(model)
print(linereg.coef_)
zip(feature_cols,linereg.coef_)
