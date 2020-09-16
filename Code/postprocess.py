import pandas as pd 
df = pd.read_csv("slov.csv",names=['pref','Name','Ministry','urls'],encoding= 'unicode_escape')
print("Before cleaning: length =",len(df))

df2 = df.drop_duplicates(subset=['Name'], keep=False)
df2.to_csv("cleanslov.csv",index=False)
print("After cleaning: length =",len(df2))