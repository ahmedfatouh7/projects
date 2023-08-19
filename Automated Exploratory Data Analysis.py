import pandas as pd

df = pd.read_excel('sample.xlsx')

print(df)
**************************************** 
import os
import pandas as pd

file_path = input("enter the path to the file you want to open")
if file_path.endswith('.csv'):
   df = pd.read_csv(file_path)
   print (df)
elif file_path.endswith('xlsx'): 
   df = pd.read_excel(file_path)
   print (df)
else:
   print("file format not supported")
x = df.dtypes
print('the data types of each column \n' + str(x))
df=df.drop_duplicates()
df=df.dropna()
print('The dataset after drop duplicates and null values \n '+str(df))
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
df_numerical_features = df.select_dtypes(include='number')
df_categorical_features = df.select_dtypes(include='object')
print('numerical_features is \n'+ str(df_numerical_features))
print('categorical_features is \n'+ str(df_categorical_features))

****************************************
 It will pre-process the data by identifying the data types of each column 
and performing appropriate pre-processing steps such as handling missing values, 
encoding categorical features, 
scaling numerical features, and more.
 The tool will also provide options for feature selection 
and dimensionality reduction,
 making it easier to analyze large datasets. 
****************************************
comprehensive visualization dashboard for each column type, including histograms, box plots, scatter plots

#boxplot
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('International_Report_Passengers.csv')
sns.boxplot(data=df[df.columns], orient="h")
plt.show
-----------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('International_Report_Passengers.csv')
sns.boxplot(data=df[df.columns[1]], orient="h")
plt.show 
------------------------------------------------------
#histogram
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Plot histograms of all columns in the DataFrame
df.hist()

# Set the title and axis labels for each histogram
for ax in plt.gcf().axes:
   ax.set_title(ax.get_title().replace('Histogram of ', ''))
   ax.set_xlabel('Values')
   ax.set_ylabel('Number of repetation')
   
# Display the histograms
plt.show()
***************************************************
#scatter plot
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file into a Pandas DataFrame:
df = pd.read_csv("International_Report_Passengers.csv")

# plotting scatterplot with Age and Weight
# weight in kgs
while True:
 try:   
    print('The two columns wanted to plot as scatter plot')
    z1 = int(input("enter the first column index wanted to select ")) 
    z2 = int(input("enter the second column index wanted to select ")) 
    if z1+1 <= int(df.shape[1]) and z2+1<= int(df.shape[1]): 
       sb.scatterplot(x=df.columns[0],y=df.columns[1],data=df)
       plt.show()
    break    
 except:
    print('Please enter right indexes of two columns')
    continue
*******************************************
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file into a Pandas DataFrame:
df = pd.read_csv("International_Report_Passengers.csv")

# plotting scatterplot with Age and Weight
# weight in kgs
sb.scatterplot(x=df.columns[0],y=df.columns[1],data=df)

plt.show()




