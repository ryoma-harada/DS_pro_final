import sqlite3
import csv
path = '/Users/ryoma/Lecture/DS_pro_final/'
db_name = 'DS_pro_finaldb.db'


# データベースへの接続
con = sqlite3.connect(path + db_name)
cur = con.cursor()

# 結合クエリの実行
sql_integration = 'SELECT * FROM weather INNER JOIN screentime ON weather.day = screentime.day;'
cur.execute(sql_integration)

# 結果を取得
result = cur.fetchall()

# CSVファイルに書き込み
csv_filename = 'DSproFinaldata.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    # CSVライターを作成
    csv_writer = csv.writer(csvfile)

    # ヘッダーを書き込み
    header = [description[0] for description in cur.description]
    csv_writer.writerow(header)

    # データを書き込み
    csv_writer.writerows(result)

# データベースへの接続を閉じる
con.close()

print(f'Data has been exported to {csv_filename}.')
