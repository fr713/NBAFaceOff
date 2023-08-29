from bs4 import BeautifulSoup
import pandas as pd
from statistics import mean
import csv
from csv import writer
from nba_api.stats.static import players
import requests
from selenium import webdriver 
import chromedriver_binary

def get_championships(player_name):
    player_id = players.find_players_by_full_name(player_name)[0]['id']

    with open("championships.csv", "r") as csv_file: 
        data = list(csv.reader(csv_file))
        for row in range(len(data)):
            if len(data[row]) == 0:
                break
            if player_id == int(data[row][-1]):
                adv_data = data[row][:-1]
                for i in range(len(adv_data)):
                    adv_data[i] = int(adv_data[i])
                return adv_data

        csv_file.close()
    string_sub = ""
    player_name = player_name.lower()
    last_name = False
    num_letters = 0
    for i in range(len(player_name)):
        if last_name and num_letters < 5:
            string_sub+=player_name[i]
            num_letters+=1
        if player_name[i] == " ":
            string_sub = string_sub + player_name[i+1] + '/'
            last_name = True
    string_sub = string_sub + player_name[0] + player_name[1]

    url = "https://www.basketball-reference.com/players/{}01.html".format(string_sub)
    r = requests.get(url)
    
    parser = BeautifulSoup(r.content, "html5lib")
    name_table = parser.find("div", attrs = {"id": "meta"})
    name = name_table.find('span')
    name = name.get_text()
    name = name.lower()
    num = 2
    string_sub = string_sub + "0" + str(num)
    while name != player_name:
        url = "https://www.basketball-reference.com/players/{}.html".format(string_sub)
        r = requests.get(url) 
        parser = BeautifulSoup(r.content, "html5lib")
        name_table = parser.find("div", attrs = {"id": "meta"})
        name = name_table.find('span')
        name = name.get_text()
        name = name.lower()
        num+=1
        string_sub = string_sub[:-2] + "0" + str(num)
    table = parser.find("ul", attrs = {"id": "bling"})
    try:
        headers = table.find_all('a')
        headerlist = [h.text.strip() for h in headers[0:]]
    except AttributeError:
    # Handle the case where headers are not found or None
        return [0,player_id]
    championships = 0
    for i in headerlist:
        if "NBA Champ" in i:
            if i[1] == 'x':
                championships = int(i[0])
            else:
                championships = 1
    chmp = [championships, player_id]
    with open("championships.csv", "a") as f:
        writer_obj = writer(f)
        writer_obj.writerow(chmp)
        f.close()
    return chmp


def get_advanced_stats(player_id):
    with open("db.csv", "r") as csv_file: 
        data = list(csv.reader(csv_file))
        for row in range(len(data)):
            if len(data[row]) == 0:
                break
            if player_id == int(data[row][-1]):
                adv_data = data[row][:-1]
                for i in range(len(adv_data)):
                    adv_data[i] = float(adv_data[i])
                return adv_data

        csv_file.close()

    driver = webdriver.Chrome()

    url = "https://www.nba.com/stats/player/{}?SeasonType=Regular+Season".format(player_id)

    driver.get(url)

    src = driver.page_source
    parser = BeautifulSoup(src, "lxml")
    table = parser.find("div", attrs = {"class": "Crom_container__C45Ti crom-container"})
    headers = table.findAll('th')
    headerlist = [h.text.strip() for h in headers[1:]]
    rows = table.findAll('tr')[1:]
    player_stats = [[td.getText().strip()  for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]

    plus_minus = []
    for i in range(1,len(player_stats)):
        num = float(player_stats[i][len(player_stats[i])-1])
        plus_minus.append(num)

    table_advanced = parser.find("div", attrs = {"class": "mt-4"})
    headers_adv = table_advanced.findAll('th')
    headerlist_adv = [h.text.strip() for h in headers_adv[1:]]
    rows_adv = table_advanced.findAll('tr')[1:]
    advanced_stats = [[td.getText().strip()  for td in rows_adv[i].findAll('td')[1:]] for i in range(len(rows_adv))]
    off_rating = []
    def_rating = []
    ts_per = [] 
    for i in range(1,len(advanced_stats)):
        num = float(advanced_stats[i][3])
        num1 = float(advanced_stats[i][4])
        num2 = float(advanced_stats[i][14])
        if int(advanced_stats[i][1]) >= 30:
            off_rating.append(num)
            def_rating.append(num1)
            ts_per.append(num2)
    
    data_advanced = [mean(plus_minus), mean(off_rating), mean(def_rating), mean(ts_per), player_id]
    with open("db.csv", "a") as f:
        writer_obj = writer(f)
        writer_obj.writerow(data_advanced)
        f.close()

    return data_advanced


