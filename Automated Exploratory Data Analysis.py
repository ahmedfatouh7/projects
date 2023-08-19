import os
import pandas as pd
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
#Automitically read files 
file_path = input("enter the path to the file you want to open")
if file_path.endswith('.csv'):
   df = pd.read_csv(file_path)
   print (df)
elif file_path.endswith('xlsx'): 
   df = pd.read_excel(file_path)
   print (df)
else:
   print("file format not supported")
#determine the types of columns 
x = df.dtypes
print('the data types of each column \n' + str(x))
#handle null values and zeros
df=df.drop_duplicates()
df=df.dropna()
print('The dataset after drop duplicates and null values \n '+str(df))
#select feature (column)from dataframe
while True:
 y = input("enter the feature you wanted to select ")    
 try:
    if y in df.columns:
      dl=df.loc[:,y]
      print(dl)
      break
 except:
    print('Please enter feature in the file')
    continue
#determine dimensions you want to display    
while True:
 z1 = int(input("enter the first dimension wanted to select ")) 
 z2 = int(input("enter the second dimension wanted to select "))
 try:
    if z1 <= int(df.shape[0]) and z2<= int(df.shape[0]): 
        if  z2>z1 :
            dm=df[z1:z2]
            print(dm)
            break
        else:
            print('Please make the value of second dimension grater the value of first dimension ')
 except:
    print('Please enter right dimensions in the file')
    continue
# numerical_features and categorical_features selection  
df_numerical_features = df.select_dtypes(include='number')
df_categorical_features = df.select_dtypes(include='object')
print('numerical_features is \n'+ str(df_numerical_features))
print('categorical_features is \n'+ str(df_categorical_features))
#boxplot to all columns
sb.boxplot(data=df[df.columns], orient="h")
plt.show
#histogram to all columns
df.hist()
# Set the title and axis labels for each histogram
for ax in plt.gcf().axes:
   ax.set_title(ax.get_title().replace('Histogram of ', ''))
   ax.set_xlabel('Values')
   ax.set_ylabel('Number of repetation')
plt.show()
#scatter plot to two columns 
print('The two columns wanted to plot as scatter plot')
while True: 
 w1 = int(input("enter the first column place wanted to select ")) 
 w2 = int(input("enter the second column place wanted to select "))    
 try:
    if w1 <= int(df.shape[1]) and w2<= int(df.shape[1]): 
       sb.scatterplot(x=df.columns[0],y=df.columns[1],data=df)
       plt.show()
       break 
    else:
       print('Please enter right indexes of two columns') 
 except:
    print('Please enter right indexes of two columns')
    continue 
