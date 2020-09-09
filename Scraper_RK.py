#!/usr/bin/env python
# coding: utf-8

#! python3
import bs4, requests, smtplib, re

getPage = requests.get('https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Risikogebiete_neu.html')
getPage.raise_for_status() #check ci je chyba
soup = bs4.BeautifulSoup(getPage.text,'html.parser') #toto vrati linky
zoznam = soup.findAll('div',attrs={'class':'text'});

zoznam2 = ' '.join(map(str, zoznam)) #skonvertovanie na list
def check():
    if ('Tschechien') in zoznam2:
        return(True)

if check() == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('libor.riska@gmail.com', 'lfgmhcbwgraoqzdx')
    conn.sendmail('libor.riska@gmail.com', 'libor.riska@gmail.com', 'Subject:Czechia is on a list!')
    conn.quit()