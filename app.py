from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

url = 'https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view='
r = requests.get(url)
time.sleep(1)

soup = BeautifulSoup(r.text, 'html.parser')

datas = soup.find_all('tr', style="text-align:right;")

index = 0

while index < len(datas):
    a_tag = datas[index].find('a')
    if a_tag:
        day = a_tag.text
        print(day)
        temp = datas[index].find_all('td', class_="data_0_0")
        if temp:
            hpa = temp[0].text
            Precipition = temp[2].text
            rainfall = temp[4].text
            temp_av = temp[7].text
            temp_max = temp[8].text
            temp_min = temp[9].text
            humidity_av = temp[10].text
            humidity_min = temp[11].text
            suntime = temp[17].text
            print(hpa,Precipition,rainfall,temp_av,temp_max,humidity_av,humidity_min,suntime)
        else:
            print("nodata")
    else:
        print("not found atag")
    index += 1