#!/usr/bin/env python
# coding: utf-8

# In[93]:


#! python3
import bs4, requests, smtplib, re, mailshake



getPage = requests.get('https://www.mzv.sk/cestovanie/covid19/registracia')
getPage.raise_for_status() #check ci je chyba
soup = bs4.BeautifulSoup(getPage.text,'html.parser') #toto vrati linky
zoznam = soup.findAll('div',attrs={'class':'journal-content-article'});


# In[94]:


zoznam2 = ' '.join(map(str, zoznam)) #skonvertovanie na list
def check():
    if ('Nemecko') in zoznam2:
        return(True)


# In[ ]:





# In[105]:


if check() == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('libor.riska@gmail.com', 'lfgmhcbwgraoqzdx')
    conn.sendmail('libor.riska@gmail.com', 'libor.riska@gmail.com', 'Subject:Slovensko stale povazuje Nemecko za bezpecnu krajinu')
    conn.quit()
    
      
    



# In[ ]:




