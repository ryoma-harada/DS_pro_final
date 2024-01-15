import sqlite3
path = '/Users/ryoma/Lecture/DS_pro_final/'
db_name = 'DS_pro_finaldb.db'

#DBに接続する
con = sqlite3.connect(path + db_name)


#SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# テーブルが存在するか確認し、存在する場合は削除する
cur.execute(f"DROP TABLE IF EXISTS weather")
cur.execute(f"DROP TABLE IF EXISTS screentime")

#テーブルを作成
sql_create_table_weather = 'CREATE TABLE weather(day int, hpa int, rainfall int, temp_av int, temp_max int, temp_min int, humidity_av int, humidity_min int, suntime int);'
sql_create_table_screentime = 'CREATE TABLE screentime(day int, screentime int);'

#SQLを実行
cur.execute(sql_create_table_weather)
cur.execute(sql_create_table_screentime)



# 気象データを挿入
weather_data_insert = "INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"

# 気象データをリストで用意する
weather_list = [
    (17, 1007.5, 0, 11.2, 17.2, 5.9, 36, 20, 8.3),
    (18, 1020.5, 0, 7.0, 11.5, 3.8, 36, 23, 6.7),
    (19, 1020.2, 0, 7.0, 10.6, 3.4, 53, 35, 3.3),
    (20, 1008.7, 0, 8.5, 13.5, 4.6, 59, 39, 6.8),
    (21, 1008.3, 0, 7.7, 13.1, 3.3, 41, 21, 9.0),
    (22, 1015.0, 0, 5.3, 10.1, 1.5, 38, 24, 9.0),
    (23, 1023.8, 0, 5.0, 10.6, 0.1, 47 ,24, 9.0),
    (24, 1023.9, 0, 4.9, 8.8, 2.0, 55, 41, 3.0),
    (25, 1018.2, 0, 6.3, 12.1, 1.0, 56, 35, 8.8),
    (26, 1019.2, 0, 7.6, 13.2, 2.6, 58, 33, 8.9),
    (27, 1022.5, 0, 8.4, 12.6, 4.3, 50, 39, 4.4),
    (28, 1022.6, 0, 7.0, 10.8, 4.4, 56, 41, 6.2),
    (29, 1018.2, 0, 7.8, 13.8, 2.2, 61, 37, 7.1),
    (30, 1017.3, 0, 9.0, 14.4, 4.4, 63, 40, 7.1),
    (31, 1004.0, 1.5, 9.2, 12.7, 5.8, 79, 62, 3.7)
]

#スクリーンタイムのデータを挿入
screentime_data_insert = "INSERT INTO screentime VALUES (?, ?);"

#スクリーンタイムをリストで用意
screentime_list = [
    (17, 400),
    (18, 634),
    (19, 432),
    (20, 654),
    (21, 794),
    (22, 243),
    (23, 741),
    (24, 558),
    (25, 646),
    (26, 697),
    (27, 729),
    (28, 881),
    (29, 928),
    (30, 907),
    (31, 851)

]


#SQLを実行
cur.executemany(weather_data_insert, weather_list)
cur.executemany(screentime_data_insert, screentime_list)

#コミット処理（データ操作を反映させる）
con.commit()

#DBへの接続を閉じる
con.close()