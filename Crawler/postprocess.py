import pandas as pd 
df = pd.read_csv("trial1.csv",names=['pref','Name','Ministry','urls'],encoding= 'unicode_escape')
print("Before cleaning: length =",len(df))

df2 = df.drop_duplicates(subset=['Name'], keep=False)
df2.to_csv("clean_t1.csv",index=False)
print("After cleaning: length =",len(df2))