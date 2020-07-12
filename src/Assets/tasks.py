from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import requests

import time
# import pandas as pd
from .constants import options_underlying_assets
import jdatetime
import datetime
from .models import Time,Symbols,Symbols_Transactions


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_binary="/usr/bin/google-chrome"
chrome_options.binary_location=chrome_binary


# @task(name="sum_two_numbers")
# def add(x, y):
#     return x + y

# @task(name="multiply_two_numbers")
# def mul(x, y):
#     total = x * (y * random.randint(3, 100))
#     return total

# @task(name="sum_list_numbers")
# def xsum(numbers):
#     return sum(numbers)

driver = webdriver.Chrome(executable_path = "/home/option/chromedriver" , chrome_options=chrome_options)
# driver = webdriver.Chrome(executable_path="/home/amir/chromedriver", chrome_options=chrome_options)

@task(name="Time_Crawler")
def TimeCrawler():
    url = "https://www.time.ir/"
    driver.get(url)
    time.sleep(2)
    time_=driver.find_element_by_css_selector("#digitalClock").text
    Time.objects.create(TimeExample=time_)

    driver.quit()

    return time_

@task(name="Adding Symbols and Ids")
def AddSymbols():
    Ids=options_underlying_assets

    for id in Ids:
        url="http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=" + id
        html_doc=requests.get(url).text
        if requests.get(url).status_code==200:

            html = BeautifulSoup(html_doc, 'html.parser')
            try:
                stock_name=html.find_all('script')[4].contents[0].split("LVal18AFC='")[1].split("'")[0]
            except:
                stock_name="Except Error 1"
            
            Symbols.objects.create(
                Symbol_Id = id,
                Symbol_Name=stock_name
            )
            
        else:
            print("error")
        



# @task(name="Orders_Crawler")
# def Orders():
#     i = 11555144562661058
#     date = 20200212

#     url = "http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i={}&d={}".format(i, date)

#     driver.get(url)
#     time.sleep(10)
#     name = driver.find_element_by_css_selector("#d16").text
#     print(name, date)
#     l = driver.execute_script('return BestLimitData')
#     df_ = []
#     for i in range(len(l)):
#         dic = {}
#         time = str(l[i][0])
#         date = str(date)
#         dic["Date_Time"] = jdatetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:]), int(time[:-4]),
#                                             int(time[-4:-2]),
#                                             int(time[-2:]))

#         dic["n{}_b".format(l[i][1])] = l[i][2]
#         dic["v{}_b".format(l[i][1])] = l[i][3]
#         dic["p{}_b".format(l[i][1])] = l[i][4]

#         dic["n{}_s".format(l[i][1])] = l[i][7]
#         dic["v{}_s".format(l[i][1])] = l[i][6]
#         dic["p{}_s".format(l[i][1])] = l[i][5]

#         df_.append(dic)
        
#     print(df_)

#     # df = pd.DataFrame(df_)
#     # df = df[(df['Date_Time'] > jdatetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:]), 8, 0, 0)) & (
#             # df['Date_Time'] < jdatetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:]), 13, 0, 0))]
#     # df = df.fillna(0)

#     # print(df.head())

#     # df.to_csv("{}-{}.csv".format(name, date), index=False)
#     return df_
#     # driver.quit()


@task(name="Stocks_Historically_Transactions")
def Transactions(id,date):
    url = "http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i={}&d={}".format(id, date)
    # print(url)
    # print("---"*2)
    # print(Symbols.objects.all())
    # print("--")
    # print(Symbols.objects.get(Symbol_Id__exact=id))
    # print("---"*5)
    # print(type(Symbols.objects.get(Symbol_Id__exact=id)))
    smbl=Symbols.objects.get(Symbol_Id__exact=id)

    req=requests.get(url)
    
    Bool_1 = True

    if req.status_code==200:
        print("Connection is OK")
        while Bool_1:
            try:
                driver.get(url)
                Bool_1=False
                print("Out of While")
            except:
                print("sleep")
                time.sleep(10)
    else:
        print("Connection Error")

    time.sleep(20)

    ll = driver.execute_script('return ClosingPriceData')
    Fa_Date = driver.find_element_by_css_selector("#MainBox > div.header.bigheader > span:nth-child(3)").text
    Fa_Date = (int(Fa_Date.split("/")[0]), int(Fa_Date.split("/")[1]), int(Fa_Date.split("/")[2]))

    date=str(date)
    En_Date=(date[:4],date[4:6],date[6:])
    
    for i in range(len(ll)):
        print(i,len(ll))

        Price = ll[i][2]
        Volume = ll[i][9]
        Transactions_Value = ll[i][10]

        # DateTime_ = jdatetime.datetime(1300+Fa_Date[0], Fa_Date[1], Fa_Date[2], int(ll[i][12][:-4]), int(ll[i][12][-4:-2]),int(ll[i][12][-2:]))#.strftime("%Y-%m-%d %H:%M:%S.%f")
        DateTime_ = datetime.datetime(int(En_Date[0]), int(En_Date[1]), int(En_Date[2]), int(ll[i][12][:-4]), int(ll[i][12][-4:-2]),int(ll[i][12][-2:]))

        # Date_=jdatetime.date(1300+Fa_Date[0], Fa_Date[1], Fa_Date[2])
        Date_=datetime.date(int(En_Date[0]), int(En_Date[1]), int(En_Date[2]))

        print(DateTime_)
        print()

        Symbols_Transactions.objects.create(
                Symbol = smbl,
                Date = Date_,
                DateTime = DateTime_,
                Price = Price,
                Volume = Volume,
                Value = Transactions_Value
            )




# @task(name="Geting Symbols name and IDs")
# def Symbols_IDs():

# celery -A Assets worker -l info

# from Assets.tasks import AddSymbols,Transactions
# AddSymbols.delay()
# Transactions("51617145873056483",20200404)
