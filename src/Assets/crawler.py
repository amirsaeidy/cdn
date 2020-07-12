from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import jdatetime

from .models import Future,Symbols_Transactions


t0 = time.clock()


@task(name="CDN Crawler")
def cdncrawler():
    # driver = webdriver.Chrome(executable_path="/home/amir/ChromeDriver")
    driver = webdriver.Chrome(executable_path="/home/amirs/chromedriver")

    url = "http://cdn.ime.co.ir/"
    driver.get(url)
    time.sleep(1)
    print(time.clock())

    DY_Settlement = driver.find_element_by_css_selector("#SAFDY98_LastSettlementPrice")
    ES_Settlement = driver.find_element_by_css_selector("#SAFES98_LastSettlementPrice")

    DY_Settlement = int(DY_Settlement.text.split(",")[0]) * 1000 + int(DY_Settlement.text.split(",")[1])
    ES_Settlement = int(ES_Settlement.text.split(",")[0]) * 1000 + int(ES_Settlement.text.split(",")[1])

    for i in range(5000):
        if (jdatetime.datetime.now().hour > 17) or (jdatetime.datetime.now().hour < 10):
            break
        elif (jdatetime.datetime.now().hour==10) and (jdatetime.datetime.now().minute < 30):
            break

        dic = {}
        # print()
        dic['Time'] = jdatetime.datetime.now()
        try:
            ###Prices ES
            ES1A = driver.find_element_by_css_selector("#SAFES98_AskPrice1").text
            ES2A = driver.find_element_by_css_selector("#SAFES98_AskPrice2").text
            ES3A = driver.find_element_by_css_selector("#SAFES98_AskPrice3").text
            ES1B = driver.find_element_by_css_selector("#SAFES98_BidPrice1").text
            ES2B = driver.find_element_by_css_selector("#SAFES98_BidPrice2").text
            ES3B = driver.find_element_by_css_selector("#SAFES98_BidPrice3").text

            dic['ES1A'] = int(ES1A.split(",")[0] + ES1A.split(",")[1])
            dic['ES2A'] = int(ES2A.split(",")[0] + ES2A.split(",")[1])
            dic['ES3A'] = int(ES3A.split(",")[0] + ES3A.split(",")[1])
            dic['ES1B'] = int(ES1B.split(",")[0] + ES1B.split(",")[1])
            dic['ES2B'] = int(ES2B.split(",")[0] + ES2B.split(",")[1])
            dic['ES3B'] = int(ES3B.split(",")[0] + ES3B.split(",")[1])
        except:
            print("error 1")
            pass
        try:
            ES1AV = driver.find_element_by_css_selector("#SAFES98_AskVolume1").text
            ES2AV = driver.find_element_by_css_selector("#SAFES98_AskVolume2").text
            ES3AV = driver.find_element_by_css_selector("#SAFES98_AskVolume3").text
            ES1BV = driver.find_element_by_css_selector("#SAFES98_BidVolume1").text
            ES2BV = driver.find_element_by_css_selector("#SAFES98_BidVolume2").text
            ES3BV = driver.find_element_by_css_selector("#SAFES98_BidVolume3").text

            dic['ES1AV'] = int(ES1AV)
            dic['ES2AV'] = int(ES2AV)
            dic['ES3AV'] = int(ES3AV)
            dic['ES1BV'] = int(ES1BV)
            dic['ES2BV'] = int(ES2BV)
            dic['ES3BV'] = int(ES3BV)

            DY1AV = driver.find_element_by_css_selector("#SAFDY98_AskVolume1").text
            DY2AV = driver.find_element_by_css_selector("#SAFDY98_AskVolume2").text
            DY3AV = driver.find_element_by_css_selector("#SAFDY98_AskVolume3").text
            DY1BV = driver.find_element_by_css_selector("#SAFDY98_BidVolume1").text
            DY2BV = driver.find_element_by_css_selector("#SAFDY98_BidVolume2").text
            DY3BV = driver.find_element_by_css_selector("#SAFDY98_BidVolume3").text


            dic['DY1AV'] = int(DY1AV)
            dic['DY2AV'] = int(DY2AV)
            dic['DY3AV'] = int(DY3AV)
            dic['DY1BV'] = int(DY1BV)
            dic['DY2BV'] = int(DY2BV)
            dic['DY3BV'] = int(DY3BV)

        except:
            print("error 2")
            pass

        try:
            DY1A = driver.find_element_by_css_selector("#SAFDY98_AskPrice1").text
            DY2A = driver.find_element_by_css_selector("#SAFDY98_AskPrice2").text
            DY3A = driver.find_element_by_css_selector("#SAFDY98_AskPrice3").text
            DY1B = driver.find_element_by_css_selector("#SAFDY98_BidPrice1").text
            DY2B = driver.find_element_by_css_selector("#SAFDY98_BidPrice2").text
            DY3B = driver.find_element_by_css_selector("#SAFDY98_BidPrice3").text

            dic['ES1AV'] = int(ES1AV)
            dic['ES2AV'] = int(ES2AV)
            dic['ES3AV'] = int(ES3AV)
            dic['ES1BV'] = int(ES1BV)
            dic['ES2BV'] = int(ES2BV)
            dic['ES3BV'] = int(ES3BV)

        except:
            print("error 3")
            pass

        try:
            LastTradedES = driver.find_element_by_css_selector("#SAFES98_LastTradedPrice").text
            LastTradedDY = driver.find_element_by_css_selector("#SAFDY98_LastTradedPrice").text

            dic['LastTradedES'] = int(LastTradedES.split(",")[0] + LastTradedES.split(",")[1])
            dic['LastTradedDY'] = int(LastTradedDY.split(",")[0] + LastTradedDY.split(",")[1])

            LastTradedESPercent = driver.find_element_by_css_selector("#SAFES98_C_LastTradedPriceChangesPercent").text
            LastTradedDYPercent = driver.find_element_by_css_selector("#SAFDY98_C_LastTradedPriceChangesPercent").text
        except:
            print("error 4")
            pass

        try:
            if '-' in LastTradedESPercent:
                les = (-1) * (int(LastTradedESPercent.split('%')[0].split(".")[0]) + float(
                    LastTradedESPercent.split('%')[0].split(".")[1]) / 10 ** len(
                    LastTradedESPercent.split('%')[0].split(".")[1]))
            else:
                les = int(LastTradedESPercent.split('%')[0].split(".")[0]) + float(
                    LastTradedESPercent.split('%')[0].split(".")[1]) / 10 ** len(
                    LastTradedESPercent.split('%')[0].split(".")[1])


            print("ldy? : ", LastTradedDYPercent)

            if '-' in LastTradedDYPercent:
                ldy = (-1) * (int(LastTradedDYPercent.split('%')[0].split(".")[0]) + float(
                    LastTradedDYPercent.split('%')[0].split(".")[1]) / 10 ** len(
                    LastTradedDYPercent.split('%')[0].split(".")[1]))
            else:
                ldy = int(LastTradedDYPercent.split('%')[0].split(".")[0]) + float(
                    LastTradedDYPercent.split('%')[0].split(".")[1]) / 10 ** len(
                    LastTradedDYPercent.split('%')[0].split(".")[1])

            print("clean ldy? : ", ldy)

            dic['LastTradedESPercent'] = les
            dic['LastTradedDYPercent'] = ldy
        except:
            print("error 5")
            pass

        try:
            if "," in driver.find_element_by_css_selector("#SAFDY98_TradesVolume").text:
                DY_Vol = int(driver.find_element_by_css_selector("#SAFDY98_TradesVolume").text.split(",")[0]) * 1000 + int(
                    driver.find_element_by_css_selector("#SAFDY98_TradesVolume").text.split(",")[1])
            else:
                DY_Vol = int(driver.find_element_by_css_selector("#SAFDY98_TradesVolume").text)

            if "," in driver.find_element_by_css_selector("#SAFES98_TradesVolume").text:
                ES_Vol = int(driver.find_element_by_css_selector("#SAFES98_TradesVolume").text.split(",")[0]) * 1000 + int(
                    driver.find_element_by_css_selector("#SAFES98_TradesVolume").text.split(",")[1])
            else:
                ES_Vol = int(driver.find_element_by_css_selector("#SAFES98_TradesVolume").text)

            print(DY_Vol, ES_Vol)
        except:
            print("error 6")
            pass
        try:
            DY_OpenInterest = int(
                driver.find_element_by_css_selector("#SAFDY98_OpenInterests").text.split(",")[0]) * 1000 + int(
                driver.find_element_by_css_selector("#SAFDY98_OpenInterests").text.split(",")[1])

            ES_OpenInterest = int(
                driver.find_element_by_css_selector("#SAFES98_OpenInterests").text.split(",")[0]) * 1000 + int(
                driver.find_element_by_css_selector("#SAFES98_OpenInterests").text.split(",")[1])
            print(DY_OpenInterest, ES_OpenInterest)
        except:
            print("error 7")
            pass

        dic['DY_Vol'] = DY_Vol
        dic['ES_Vol'] = ES_Vol
        dic['DY_OpenInterest'] = DY_OpenInterest
        dic['ES_OpenInterest'] = ES_OpenInterest

        
        Future.objects.create(

            Comodity_Name='SA',
            Maturity_Date='ES',
            En_DateTime=datetime.date.now(),
            Fa_DateTime=str(jdatetime.datetime.now()),
            AP1=ES1A,
            AP2=ES2A,
            AP3=ES3A,
            BP1=ES1B,
            BP2=ES1B,
            BP3=ES1B,
            LastDay_Settlement=ES_Settlement,
            AV1=ES1AV,
            AV2=ES2AV,
            AV3=ES3AV,
            BV1=ES1BV,
            BV2=ES2BV,
            BV3=ES3BV,
            Last_Price=LastTradedES,
            Volume_Traded=ES_Vol,
            Open_Interest=ES_OpenInterest

        )

        Future.objects.create(

            Comodity_Name='SA',
            Maturity_Date='DY',
            En_DateTime=datetime.date.now(),
            Fa_DateTime=str(jdatetime.datetime.now()),
            AP1=DY1A,
            AP2=DY2A,
            AP3=DY3A,
            BP1=DY1B,
            BP2=DY2B,
            BP3=DY3B,
            LastDay_Settlement=DY_Settlement,
            AV1=DY1AV,
            AV2=DY2AV,
            AV3=DY3AV,
            BV1=ES1BV,
            BV2=ES2BV,
            BV3=ES3BV,
            Last_Price=LastTradedDY,
            Volume_Traded=DY_Vol,
            Open_Interest=DY_OpenInterest
        )

        time.sleep(15)

    return


@task(name="Stocks History Crawler")
def stockscrawler(id):
    driver = webdriver.Chrome(executable_path="/home/amir/ChromeDriver")
    # driver = webdriver.Chrome(executable_path="/home/amirs/chromedriver")

    ll = driver.execute_script('return ClosingPriceData')
    Fa_Date = driver.find_element_by_css_selector("#MainBox > div.header.bigheader > span:nth-child(3)").text
    Fa_Date = (int(Fa_Date.split("/")[0]), int(Fa_Date.split("/")[1]), int(Fa_Date.split("/")[2]))
    
    for i in range(len(ll)):

        Price = ll[i][2]
        Volume = ll[i][9]
        Transactions_Value = ll[i][10]
        Time = jdatetime.datetime(Fa_Date[0], Fa_Date[1], Fa_Date[2], int(ll[i][12][:-4]), int(ll[i][12][-4:-2]),
                                        int(ll[i][12][-2:])).strftime("%Y-%m-%d %H:%M:%S.%f")

        Symbols_Transactions.objects.create(
                Symbol = id
                DateTime = Time
                Price = Price
                Volume = Volume
                Value = Value
            )

