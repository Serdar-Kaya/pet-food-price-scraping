from bs4 import BeautifulSoup
import requests
import time 
import datetime
import smtplib
import datetime
import pandas as pd

def check_price():
    URL = 'https://www.petlebi.com/kedi-urunleri/royal-canin-sterilised-37-kisirlastirilmis-kedi-mamasi-4kg.html'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(class_ ='product-h1').get_text()
    price = soup2.find(class_ ='new-price').get_text()
    price = price.strip()[:3]
    title = title.strip()[:25]
    import datetime
    today = datetime.date.today()
    import csv
    header = ['Title', 'Price','Date']
    data = [title, price, today]
    with open('MamaFiyat.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    if(price < 350):
        send_mail()
    

while(True):
    check_price()
    time.sleep(86400)

df = pd.read_csv(r'C:\Users\kserd\notebooks\MamaFiyat.csv')
print(df)


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('kayaserdar664@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "Mama fiyat"
    body = "Link: https://www.petlebi.com/kedi-urunleri/royal-canin-sterilised-37-kisirlastirilmis-kedi-mamasi-4kg"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'kayaserdar664@gmail.com',
        msg
    )

