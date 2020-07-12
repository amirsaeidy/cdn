from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import datetime
import jdatetime

pd.set_option('display.max_columns', 500)

t0 = time.clock()

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

url = "http://cdn.ime.co.ir/"
driver.get(url)
time.sleep(1)
print(time.clock())

ES1A_series = []
ES2A_series = []
ES3A_series = []
ES1B_series = []
ES2B_series = []
ES3B_series = []

ES1AV_series = []
ES2AV_series = []
ES3AV_series = []
ES1BV_series = []
ES2BV_series = []
ES3BV_series = []

DY1A_series = []
DY2A_series = []
DY3A_series = []
DY1B_series = []
DY2B_series = []
DY3B_series = []

LastTradedES_Series = []
LastTradedDY_Series = []

LastTradedES_Series_Percent = []
LastTradedDY_Series_Percent = []
Prof = []
df = []

DY_Settlement = driver.find_element_by_css_selector("#SAFDY98_LastSettlementPrice")
ES_Settlement = driver.find_element_by_css_selector("#SAFES98_LastSettlementPrice")

DY_Settlement = int(DY_Settlement.text.split(",")[0]) * 1000 + int(DY_Settlement.text.split(",")[1])
ES_Settlement = int(ES_Settlement.text.split(",")[0]) * 1000 + int(ES_Settlement.text.split(",")[1])

print(DY_Settlement)
print(ES_Settlement)

for i in range(400):
    dic = {}
    print()
    dic['Time'] = jdatetime.datetime.now()
    try:
        ###Prices ES
        ES1A = driver.find_element_by_css_selector("#SAFES98_AskPrice1").text
        ES2A = driver.find_element_by_css_selector("#SAFES98_AskPrice2").text
        ES3A = driver.find_element_by_css_selector("#SAFES98_AskPrice3").text
        ES1B = driver.find_element_by_css_selector("#SAFES98_BidPrice1").text
        ES2B = driver.find_element_by_css_selector("#SAFES98_BidPrice2").text
        ES3B = driver.find_element_by_css_selector("#SAFES98_BidPrice3").text

        ES1A_series.append(int(ES1A.split(",")[0] + ES1A.split(",")[1]))
        ES2A_series.append(int(ES2A.split(",")[0] + ES2A.split(",")[1]))
        ES3A_series.append(int(ES3A.split(",")[0] + ES3A.split(",")[1]))
        ES1B_series.append(int(ES1B.split(",")[0] + ES1B.split(",")[1]))
        ES2B_series.append(int(ES2B.split(",")[0] + ES2B.split(",")[1]))
        ES3B_series.append(int(ES3B.split(",")[0] + ES3B.split(",")[1]))

        dic['ES1A'] = int(ES1A.split(",")[0] + ES1A.split(",")[1])
        dic['ES2A'] = int(ES2A.split(",")[0] + ES2A.split(",")[1])
        dic['ES3A'] = int(ES3A.split(",")[0] + ES3A.split(",")[1])
        dic['ES1B'] = int(ES1B.split(",")[0] + ES1B.split(",")[1])
        dic['ES2B'] = int(ES2B.split(",")[0] + ES2B.split(",")[1])
        dic['ES3B'] = int(ES3B.split(",")[0] + ES3B.split(",")[1])
    except:
        print("error 1")
        pass
        ###Volumes ES
        # SAFES98_AskVolume1
    try:
        ES1AV = driver.find_element_by_css_selector("#SAFES98_AskVolume1").text
        ES2AV = driver.find_element_by_css_selector("#SAFES98_AskVolume2").text
        ES3AV = driver.find_element_by_css_selector("#SAFES98_AskVolume3").text
        ES1BV = driver.find_element_by_css_selector("#SAFES98_BidVolume1").text
        ES2BV = driver.find_element_by_css_selector("#SAFES98_BidVolume2").text
        ES3BV = driver.find_element_by_css_selector("#SAFES98_BidVolume3").text

        ES1A_series.append(int(ES1AV))
        ES2A_series.append(int(ES2AV))
        ES3A_series.append(int(ES3AV))
        ES1B_series.append(int(ES1BV))
        ES2B_series.append(int(ES2BV))
        ES3B_series.append(int(ES3BV))

        dic['ES1AV'] = int(ES1AV)
        dic['ES2AV'] = int(ES2AV)
        dic['ES3AV'] = int(ES3AV)
        dic['ES1BV'] = int(ES1BV)
        dic['ES2BV'] = int(ES2BV)
        dic['ES3BV'] = int(ES3BV)

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
        DY1A_series.append(int(DY1A.split(",")[0] + DY1A.split(",")[1]))
        DY2A_series.append(int(DY2A.split(",")[0] + DY2A.split(",")[1]))
        DY3A_series.append(int(DY3A.split(",")[0] + DY3A.split(",")[1]))
        DY1B_series.append(int(DY1B.split(",")[0] + DY1B.split(",")[1]))
        DY2B_series.append(int(DY2B.split(",")[0] + DY2B.split(",")[1]))
        DY3B_series.append(int(DY3B.split(",")[0] + DY3B.split(",")[1]))

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
        # print(DY1A_series)
        LastTradedES = driver.find_element_by_css_selector("#SAFES98_LastTradedPrice").text
        LastTradedDY = driver.find_element_by_css_selector("#SAFDY98_LastTradedPrice").text

        dic['LastTradedES'] = int(LastTradedES.split(",")[0] + LastTradedES.split(",")[1])
        dic['LastTradedDY'] = int(LastTradedDY.split(",")[0] + LastTradedDY.split(",")[1])

        LastTradedES_Series.append(int(LastTradedES.split(",")[0] + LastTradedES.split(",")[1]))
        LastTradedDY_Series.append(int(LastTradedDY.split(",")[0] + LastTradedDY.split(",")[1]))

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

        LastTradedES_Series_Percent.append(les)

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

        LastTradedDY_Series_Percent.append(ldy)

        dic['LastTradedESPercent'] = les
        dic['LastTradedDYPercent'] = ldy
    except:
        print("error 5")
        pass

    try:
        DY_Vol = int(driver.find_element_by_css_selector("#SAFDY98_TradesVolume").text.split(",")[0]) * 1000 + int(
            driver.find_element_by_css_selector("#SAFDY98_TradesVolume").text.split(",")[1])
        ES_Vol = int(driver.find_element_by_css_selector("#SAFES98_TradesVolume").text.split(",")[0]) * 1000 + int(
            driver.find_element_by_css_selector("#SAFES98_TradesVolume").text.split(",")[1])
        print(DY_Vol, ES_Vol)

        DY_OpenInterest = int(
            driver.find_element_by_css_selector("#SAFDY98_OpenInterests").text.split(",")[0]) * 1000 + int(
            driver.find_element_by_css_selector("#SAFDY98_OpenInterests").text.split(",")[1])

        ES_OpenInterest = int(
            driver.find_element_by_css_selector("#SAFES98_OpenInterests").text.split(",")[0]) * 1000 + int(
            driver.find_element_by_css_selector("#SAFES98_OpenInterests").text.split(",")[1])
        print(DY_OpenInterest, ES_OpenInterest)

        dic['DY_Vol'] = DY_Vol
        dic['ES_Vol'] = ES_Vol
        dic['DY_OpenInterest'] = DY_OpenInterest
        dic['ES_OpenInterest'] = ES_OpenInterest

        print(LastTradedDY_Series[-1])
        print(LastTradedES_Series[-1])
        spread = 0.8
        if round(abs(LastTradedES_Series_Percent[-1] - LastTradedDY_Series_Percent[-1]), 4) > spread:
            # print()
            print("-------------------------------")
            print(jdatetime.datetime.now())
            print("ES : ", les, "% ", LastTradedES_Series[-1], "  -  ", "DY : ", LastTradedDY_Series[-1], ldy, "%")
            e = LastTradedES_Series[-1]
            d = LastTradedDY_Series[-1]
            t_d = DY_Settlement
            t_e = ES_Settlement
            g = max(ldy, les) + 1
            r = 1 + g / 100
            t_e = r * t_e
            t_d = r * t_d
            profit = round((max(t_e - e, t_d - d) - min(t_e - e, t_d - d)) * 10 - (0.0068 * (t_e + t_d + e + d)), 3)
            print("Profit : ", profit, " ", round(profit / 2000, 3), "%")
            Prof.append(round(profit / 2000, 3))
            print("----------------------------------")
            print()
        print()

    except:
        print("error 6")
        pass

    df.append(dic)
    time.sleep(15)
    if jdatetime.datetime.now() > jdatetime.datetime(1398, 9, 17, 17, 1, 0):
        break

print(pd.DataFrame(df).head())
print(jdatetime.datetime.now().day, jdatetime.datetime.now().minute, jdatetime.datetime.now().second)
DF = pd.DataFrame(df)

DF.to_csv("1398_{}_{}----{}_{}.csv".format(jdatetime.datetime.now().month, jdatetime.datetime.now().day,
                                           jdatetime.datetime.now().hour, jdatetime.datetime.now().minute), index=False)

print(list(set(Prof)))

print(jdatetime.datetime.now())

driver.quit()
