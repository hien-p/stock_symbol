from tokenize import String
from typing_extensions import Self
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
import argparse 
import io
class Stock_info:
    def __init__(self, name, year, quarter):
        self.stock_name  = name
        self.year_stock = year
        self.quarter_stock = quarter
    def _get_name(self):
        return str(self.stock_name)

    def _get_year(self):
        return str(self.year_stock)


if __name__ == "__main__":

    #url = 'https://s.cafef.vn/bao-cao-tai-chinh/VNG/IncSta/2022/2/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-du-lich-thanh-thanh-cong.chn'
  
    parser = argparse.ArgumentParser(description='Test.')
    parser.add_argument('text', action='store', type=str, help='The text to parse.')
    parser.add_argument('year', action='store', type=int, help='The year to parse.')
    parser.add_argument('--qua', nargs='?',const=4, type=int, help='The quarter to parse.',)

    args = parser.parse_args()
    print(args.text,args.year, args.qua)

    stock = Stock_info(args.text,args.year, args.qua)
    url = 'https://s.cafef.vn/bao-cao-tai-chinh/{}\
        /BSheet/{}\
        /2/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-du-lich-thanh-thanh-cong.chn'.format(stock._get_name(), stock._get_year())
    url = url.replace(" ", "")
    print(url)

    response=requests.get(url)  
    with open('data/test.txt','w') as f:
        #f.write(response.text)
        doc_quotes =BeautifulSoup(response.text,'html.parser')
    
    
    tien_tai_san_ngan_han = doc_quotes.find_all('tr', class_='r_item',id='111')
    
    for i in tien_tai_san_ngan_han:
        text = i.text.strip().splitlines()

    res = [text[0], text[-1]]
    for i in res:
        print(i.strip().lower())

    dau_tu_tai_chinh_ngan_hang = doc_quotes.find_all('tr',class_='r_item',id=120)
    for i in dau_tu_tai_chinh_ngan_hang:
        text = i.text.strip().splitlines()
    res = [text[0], text[-1]]
    for i in res:
        print(i.strip().lower())

    # tiền và các khoản đầu tư ngắn hạn
    # tien_and_khoan_dau_tu_ngan_hang

    Phai_thu_dai_han = doc_quotes.find_all('tr',class_='r_item_a',id=210)
      
    for i in Phai_thu_dai_han:
        text = i.text.strip().splitlines()
    res = [text[0], text[-1]]
    for i in res:
        print(i.strip().lower())


    # khoản phải thu =  khoản phải thu ngắn hạn +  khoản phải thu dài hạn 
