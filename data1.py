'''import pandas as pd
data={'Name':['Alice','Bob','Charlie','David'],'Age':[25,30,35,40],'City':['New york','san francisco','los angele','chicago']}
df=pd.DataFrame(data)
print("original dataframe:")
print(df)
print("\nAcessing specific column:")
print(df['Name'])
print(df[['Name','Age']])
print("\nFiltering:")
filtered_df=df[df['Age']>30]
print(filtered_df)
df['Salary']=[50000,600000,70000,80000]#['New york','san francisco','los angele','chicago']
print("\nDataframe after")
print(df)
print("\nBasic statistics:")
print(df.describe())
print(df.info())'''
#2
import pandas as pd
import matplotlib.pyplot as plt
file_path='Documents/example_data.csv'
df=pd.read_csv(file_path)
print("First row")
print(df.head())
print("\nData Frame")
print(df.info())
print("\nSummary:")
print(df.describe())
print(df.info())
selected_columns=['Name','Age','Salary']
selected_df=df[selected_columns]
print("\nDataFrame with selected columns:")
print(selected_df.head())
grouped_data=df.groupby('City')['Salary'].mean()
print("\nAvarage salary by city:")
print(grouped_data)
df.plot(x='Age',y="Salary",kind='scatter',title='Age vs. Salary')
plt.show()