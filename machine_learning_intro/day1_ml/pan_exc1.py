import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

df = pd.read_csv('International_football_results.csv')

print(df.info())

"""演習問題"""
# 列名が”tournament" の列を取り出す
print(df['tournament'])
# 行番号100行目以上6000行目未満を取り出せ
line = df[100:6000]
print(line)
# 列名は’date','city', 'country' となっている列を3列まとめてとりだせ
three = df[['date', 'city', 'country']]
print(three)
# 'Brazil' がhome_team となっている試合を取り出せ
br = df['home_team'] == 'Brazil'
print(df[br])
# 'Brazil'が出場している試合を全て取り出せ
br_union1 = (df['away_team'] == 'Brazil') | (df['home_team'] == 'Brazil')
print(df[br_union1])
# different method
br_union2 = (df[['away_team', 'home_team']] == 'Brazil').any(axis=1)
print(df[br_union2])
# 2003年に行われた試合を全て取り出せ
year = df.date.str.contains('2003')
print(df[year])
# 試合2チームの総合得点の例、point_add を追加せよ
df['score_add'] = df['home_score'] + df['away_score']
print(df.head())

# England が出場（しゅつじょう）した試合を全て抜き出し新たな変数にだいにゅうせよ
England_exists= (df[['home_team','away_team']] == 'England').any(axis=1)

dfE= df[England_exists]
print(dfE)

# csv file へ書き出せ
dfE.to_csv('Englad_matches.csv', index= True)

# 総合演習問題　general excersices
dfs= pd.read_csv('sample-data.csv')
print(dfs.info())
# データの基本情報を確認せよ
print(dfs.head())
# first eight rows
print(dfs[:8])
#third row fifth element
print('3,5 :',dfs.iloc[3,0])

# データには欠損がある。欠損値のある行を除け
print(dfs.dropna())

# Gender の列をダミー変数かしてデータに付け加えよ
Male_Female = pd.get_dummies(dfs['Gender'])
print(Male_Female)
dfs = pd.concat([dfs,Male_Female],axis = 1)
print(dfs)

# e out the sick patients out == 0 , healthy == 1
Disease_exists = (dfs['Disease'] == 1).replace({True:1,False:0})
dfD= dfs[Disease_exists == 0]
print(dfD)

# 病気が1の人のみを抜き出せ isolate the Diseased
Diseased_bros = (dfs[dfs['Disease'] == 1]).Disease
print(Diseased_bros )

# データを学習用と検証陽に８対２の割合で分割せよ
train_dfs, test_dfs = train_test_split(dfs,test_size= 0.2)
print('the train len is:',len(train_dfs),'the test len is:',len(test_dfs))