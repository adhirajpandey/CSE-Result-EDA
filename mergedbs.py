import pandas as pd
import os

l = os.listdir()
l.remove("mergedbs.py")
l.remove("CSE.csv")
l.remove("master.csv")

csv_list = l

print(csv_list)

df_master = pd.read_csv('master.csv')
for csv_file in csv_list:
    df = pd.read_csv(csv_file)
    df.to_csv('master.csv', mode='a', header=False, index=False)