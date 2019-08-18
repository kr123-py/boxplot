'''Example:-
first goto folder image/boxploImage.png  that have  image which is use  for easy to understand  concept of boxplot
25,28,29,29,30,34,35,35,37,38

1)	Order the data from smallest to largest order
	25,28,29,29,30,34,35,35,37,38
2)	 Find the median
	10/2=5  so (30+34)/2=32
So divide the series into two parts
1.	25,28,29,29,30
2.	34,35,35,37,38
3)	Find the quantities(Q1,Q2)
	1. 25,28,29,29,30
      5/2=2.5->29(Q1)
   2.34,35,35,37,38
      5/2=2.5->35(Q3)
4)	Find the min and max in whole series 
Min=25
Max =38'''
import pandas as pd 
A=[25,28,29,29,30,34,35,35,37,38]#A is list 
print(A)
df = pd.DataFrame({'col':A}) #convert list into DataFrame
print(df)
import seaborn as sb
sb.boxplot(df['col'])
# for categorical  data set
data_read=pd.read_csv("boxplot\\Dataset\\iris_new.csv")
data_read.head()
sb.boxplot(y='Sepal.Length',x='Species', data=data_read)
