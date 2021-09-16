# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:03:49 2021

@author: David Olivari
"""

import requests 
import pandas as pd
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_screener(version):
    url = 'https://finviz.com/screener.ashx?v={version}&f=cap_small,sh_float_u50,sh_outstanding_u50,sh_price_u10,sh_relvol_o2&ft=4'
    screen = requests.get(url,headers = headers).text
    #use the first row in the dataframe produced by read_html as header cols, also , use string comp to bs4 , totally comaptible with html5
    dfs = pd.read_html(screen,header=0,flavor='bs4')
    for df in dfs:
        if df.columns[0:3].tolist() == ['No.', 'Ticker', 'Company']:
            #if df.columns[0] == 'No.':
            print(df.columns)
            print(f"Table version: {version} detected")
            return df
   
   
'''
https://finviz.com/screener.ashx?v=111&f=cap_mid&ft=4
other cap values:
    cap_small
    cap_micro
ft=4 : Descriptive tab, can choose price
https://finviz.com/screener.ashx?v=111&f=cap_small,sh_price_u10&ft=4
Relative Volume: higher volume means something going on (including buyback?)
https://finviz.com/screener.ashx?v=111&f=cap_small,sh_price_u10,sh_relvol_o2&ft=4
share outstanding: set a small amount ,sh_outstanding_u10
https://finviz.com/screener.ashx?v=111&f=cap_small,sh_price_u10,sh_relvol_o2,sh_outstanding_u10&ft=4
set a matching float
https://finviz.com/screener.ashx?v=111&f=cap_small,sh_price_u10,sh_relvol_o2,sh_outstanding_u10&ft=4
'''

table111 = get_screener('111')
print(table111[['Ticker','P/E','Price']])

#print(consolidatedtables)