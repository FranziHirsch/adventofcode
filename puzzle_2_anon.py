import re
import pandas as pd
import os
import urllib.request


os.chdir()#Add directory
df=pd.read_excel("puzzle2.xlsx")

# Puzzle 1/1
counter=0
for row in df.itertuples():
    val_freq=row.val.count(row.char)
    if row.low_lim <= val_freq and row.up_lim >= val_freq:
        counter+=1

print(counter)

# Puzzle 1/2
counter2=0
for row in df.itertuples():
    chars=[]
    chars.append(row.val[row.low_lim-1])
    chars.append(row.val[row.up_lim-1])
    if chars.count(row.char)==1:
        counter2+=1

print(counter2)