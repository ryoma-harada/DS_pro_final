from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

url = 'https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view='
r = requests.get(url)
time.sleep(1)

html_soup = BeautifulSoup(r.text, 'html.parser')

title_lists = html_soup.select('a')

print(title_lists)