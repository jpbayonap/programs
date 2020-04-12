# needed libraries
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

# データの読み込み
# 絶対パス　file path
df2 = pd.read_csv(r'~/Desktop/ml_ python/python_day1/International_football_results.csv')

df1 = pd.read_csv('International_football_results.csv')
print(df1)
print(df2)

# 最初の５行だけ表示 5th row  df1.head(# of rows)
print(df1.head(5))

# データの情報を表示 basic information concerning data
print(df1.info())

# shape of the data データの形を確認
print(df1.shape)

# 列名の表示　name of the columns
print(df1.columns)

# 行名の表示 range of rows
print(df1.index)

# データの縦の長さをチェック
print(len(df1))

"""データから情報を取り出す"""
print(df1.home_team)  # look for the name of the column
print(df1['away_team'])
# 2列以上
print(df1[['home_team', 'date']])
"""cool way　 特定の列だけを抽出したデータフレームを作成 df1[ [] ]"""
df_subset = df1[['date', 'home_team', 'away_team']]
print(df_subset)

"""行番号で取り出す df[n1:n2:n3]  
n1 above　以上
n2 less than 　未満
n3  step　　増加量
"""
# 0行目以上、1000行目未満
print(df1[0:1000])
# 15000行目以降を抽出
print(df1[15000:])
# 　0行目以上、100行目未満を2行ごとに抽出
print(df1[0:100:2])
# 全データを2行ごとに抽出
print(df1[::2])

""" .iloc で行番号と列番号で取り出す　specific parts df.iloc[row,column] """
print('first row , second column', df1.iloc[1, 2])
# 10 行目以上、20行目未満 1列目以上、　5列目未満 less than
print(df1.iloc[10:20, 1:5])
# 全行　、1列〜5列未満
print(df1.iloc[:, 1:5])

"""statistical values 時計的な値"""

# 最大値
print(df1[['home_score', 'away_score']].max())
# 最小値
print(df1[['away_score', 'home_score']].min())
# 平均値　mean value
print(df1[['home_score', 'away_score']].mean())

# 標準偏差　standard deviation
print(df1[['home_score', 'away_score']].std())

"""データから情報を取り出す"""
array1 = np.array([16, 6, 3])
# 全要素を取り出す 真偽（しんぎ）ベクトル　use boolean vector to print
print(array1[[True, True, True]])
# same as
print(array1)
# array of arrays
print(array1[True, True, True])

# 1つ目と3つ目の要素だげ
print(array1[[True, False, True]])

# 判定で真偽ベクトル　各要素が　5より大きいかの判定
print(array1 > 5)

# 以下　less or equal than
print(array1 <= 8)

# print your condition 判定に基づいて要素を抽出する
condition = array1 <= 10
print(array1[condition])

# 条件に一致する行を取り出す
'''積集合 & intersection 　　｜集合  union  　を　抽出する'''

# home_teamがCOLOMBIAのデータ
print(df1[df1['home_team'] == 'Colombia'])

# home_team が Brazil かつaway_team がColombiaのデータ
union = (df1['home_team'] == 'Brazil') & (df1['away_team'] == 'Colombia')
print(df1[union])

# home_team がEngland　または  away_team が Colombiaのデータ
inter = (df1['home_team'] == 'England') | (df1['away_team'] == 'Colombia')
print(df1[inter])

# datesに1972が含まれる行を抽出 column.str.contains
year = '1972'
print(df1[df1.date.str.contains(year)])

# interval dates 1875 ,1876 , 1877
year_union = df1.date.str.contains('1875') | df1.date.str.contains('1876') | df1.date.str.contains('1877')
print(df1[year_union])

# just games of Colombia
tu_pais = (df1['home_team'] == 'Colombia') | (df1['away_team'] == 'Colombia')
print(df1[tu_pais])
# 別解
tu_p = (df1[['away_team', 'home_team']] == 'Colombia').any(axis=1)
print(df1[tu_p])

# クエリ検索 query search
print('query search', df1.query("home_team == 'Colombia'"))
print(df1.query("home_team == 'Colombia' | away_team == 'Colombia'"))

'''新たな列の作成'''
# データフレームの列同士の演算
# 点差
score_diff = df1['home_score'] - df1['away_score']
# redefine
score_diff = abs(score_diff)

# 列を作成 df1['name'] = new_column
df1['score_diff'] = score_diff
# show the new column 新しい列が作成されていることの確認
print(df1.head())

'''内包（ないほう）表現を用いた文字列の部分切り出し　text comprehension'''

# pd.to_numeric string to number で文字列型を数値型に変換
# get the year　実施年（じっしねん）だけを格納した列
""" [column.split('-')[position] for column in df1['column']]"""
df1['year'] = pd.to_numeric([date.split('-')[0] for date in df1['date']])
df1['month'] = pd.to_numeric([date.split('-')[1] for date in df1['date']])
df1['day'] = pd.to_numeric([date.split('-')[2] for date in df1['date']])
print(df1.head())

'''ascending or descending sorting 並び替え'''
# ascending= False で降順指定。Trueだと昇順（しょうじゅん）True as default
print(df1.sort_values('home_score', ascending=False))

# multiple column　arguments, importance from left to right 引数
df1.sort_values(['away_score', 'home_score'], ascending=False)
print(df1[['away_score', 'home_score']])

'''置換
    df1.replace(｛置換元：置換先）｝ 　'''
# change 1 values to 39007
print(df1.replace({1: 39007}))

# 　1を100に2を200に置き換える
print(df1.replace({1: 100, 2: 200}))
# 　true to 1 false to 0
print(df1.replace({True: 1, False: 0}))
# pg 30 typo df.raplace to df.replace


'''データの取出し　高度 extract useful data for analysis'''
# 　分析に使う国だけのデータを作成する　Colombia, Brazil, Germany, Italy, Argentina
""" change the argument list from boolean to 0,1 list"""
Colombia_exists = (df1[['home_team', 'away_team']] == 'Colombia').any(axis=1).replace({True: 1, False: 0})
Brazil_exists = (df1[['home_team', 'away_team']] == 'Brazil').any(axis=1).replace({True: 1, False: 0})
Germany_exists = (df1[['home_team', 'away_team']] == 'Germany').any(axis=1).replace({True: 1, False: 0})
Italy_exists = (df1[['home_team', 'away_team']] == 'Italy').any(axis=1).replace({True: 1, False: 0})
Argentina_exists = (df1[['home_team', 'away_team']] == 'Argentina').any(axis=1).replace({True: 1, False: 0})
'''add all existing teams
試合で5力国中の2力国が含まれていれば和は2　show any two pairs from df5,  n=1 then all existing teams will appear'''
df5 = df1[Colombia_exists + Brazil_exists + Germany_exists + Italy_exists + Argentina_exists == 2]
print(df5)

''' データの書き出し'''
# csv ファイルへのデータの書き出し
# no index needed
# postscript mode mode= 'a'  追記モード（ついき）
df5.to_csv('5teams.csv', index=False)

"""データの結合"""
# 勝った国の列を追加 from df5 data frame (df5[condition]).column
homewin = (df5[df5.away_score < df5.home_score]).home_team
print(homewin)
awaywin = (df5[df5.home_score < df5.away_score]).away_team
# concatenate lists pd.concat([df1,df2]) 縦方向　pd.concat([df1,df2], axis= 1)
win = pd.concat([homewin, awaywin])
# make a new column WinCountry  NaN = not a number
df5['Win_Country'] = win
print(df5.head())

# home_team が勝利したかの列を追加
# 勝利　1・引き分け0　draw、敗北（はいぼく）-1
# initialize the column with nan
df5["home_win"] = np.nan
# mask(condition, value)
'''with replace'''
df5['home_win'] = df5['home_win'].mask(df5.home_score > df5.away_score, 1)
# df5['home_win'] = (df5.home_score > df5.away_score).replace({True:1})
df5['home_win'] = df5['home_win'].mask(df5.home_score == df5.away_score, 0)
df5['home_win'] = df5['home_win'].mask(df5.home_score < df5.away_score, -1)
print(df5.head())

'''　欠損値処理　deficit values '''
# 欠損値のある行を除外する
print(df5.dropna())
# 欠損値を穴埋めする　fill with zero draw matches
print(df5.fillna(0))

# 欠損値を抽出する isolate null  data with True
print(df5.isnull())
print(df5[df5['Win_Country'].isnull()])
# 欠損値を0で穴埋めして元データに代入
df5 = df5.fillna(0)
print(df5)

'''ダミーへんすう化 Change to dummie variable'''
# change categorical data to numerical data

# チームをダミー変数化したデータフレームを作成
team_dummy = pd.get_dummies(df5[['home_team', 'away_team']])
print(team_dummy)

# 元のdata frame と teamをダミー変数化したdata frameを結合
df5 = pd.concat([df5, team_dummy], axis=1)
print(df5)

'''drop columns  ダミー変数化したもの、tournament,city ,country , neutral を消去（しょうきょ）   
erase columns which were changed and those who weren't  '''
df5 = df5.drop(['home_team', 'away_team', 'tournament', 'city', 'country', 'neutral'], axis=1)
print(df5.head())

''' 学習データと検証データへ分割'''
# randomly select n rows ランダムに1行抽出 入れた行数分抽出ヲ行う
print(df5.sample())
print(df5.sample(3))

# train_test_splitの利用

# 25%をテストデータとして使う default
train_df5, test_df5 = train_test_split(df5)
print('train len:', len(train_df5), 'test len:', len(test_df5))
# 50% を使う
train_df5, test_df5 = train_test_split(df5, test_size=0.5)
print('train len ',len(train_df5),'test len',len(test_df5))
