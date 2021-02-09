import requests
import time
import numpy as np
import pandas as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
kimetsu2_url = "https://manga-tei.com/kimetsu-no-yaiba-character-list/"
kimetsu2_response = requests.get(kimetsu2_url)
kimetsu2_soup = BeautifulSoup(kimetsu2_response.text, "xml")
names = kimetsu2_soup.find_all("img")
#print(names.text)はなぜ実行できないのか
for i,name in enumerate(names):
    #print(name["src"])
    time.sleep(0.1)
    r = requests.get(name['src'])
    #ここ質問、保存先とtime.sleepについて
    with open(str('./Pictures/Screenshots')+str(i)+str('.jpeg'),'wb') as file:
                file.write(r.content)
