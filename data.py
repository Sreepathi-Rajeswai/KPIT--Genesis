import pandas as pd
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
df['Salary']=[50000,600000,70000,80000]
print("\nDataframe after")
print(df)