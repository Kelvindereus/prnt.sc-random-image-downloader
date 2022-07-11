#################################################################
####### CODE TO FIND AND DOWNLOAD https://prnt.sc/ IMAGES #######
#################################################################

####### IMPORTING THE NEEDED PYTHON MODULES
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
import time
import string    
import random 


###LOOPING THE CODE BELOW
attempt = 0
while True:


####### GENERATE RANDOM NUMBERS
    S = 4  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    randomnummersresult = ''.join(random.choices(string.ascii_lowercase, k = S))    


####### REQUESTING AND FILTERING IMAGES FROM WEBPAGE + MAKING THE URL
    URL = "https://prnt.sc/"  + str(randomnummersresult)
    getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(getURL.text, 'html.parser')
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))

####### SPLIT URLS TO 1 STRING
    s = images
    str1 = ""
    for i in s:
        str1 += i 
        

####### IF "imgur" IS IN STRING FROM ABOVE, FILTER THE SCREENSHOT 
    if "imgur" in str1:
        attempt += 1
        text = str1
        start = text.index('i.imgur.com')
        end = text.index('.png',start)
        substring = text[start:end]
        nieuweimgurl = str ("https://"+ str(substring) + str(".png")) 

####### SPLIT AFTER THE /, AND DOWNLOAD THAT IMAGE
        url = nieuweimgurl
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        print("I found a image, and downloaded it!")
        time.sleep(2.1)
    else:
        attempt += 1
        print("....")
        time.sleep(2.1)





####### WHEN ABOVE 300 TRY'S, RUN CODE ABOVE, BUT WITH 5 CHARACTERS

    if attempt > 300:
        
###LOOPING CODE BELOW
        attempt = 0
        while True:

            
####### RANDOM LETTERS (5x)
            import string    
            import random # define the random module  
            S = 5  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            randomnummersresult = ''.join(random.choices(string.ascii_lowercase, k = S))    



####### REQUESTING EN FILTERING IMAGES
            URL = "https://prnt.sc/"  + str(randomnummersresult)
            getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
            soup = BeautifulSoup(getURL.text, 'html.parser')
            images = []
            for img in soup.findAll('img'):
                images.append(img.get('src'))

####### SPLIT URLS TO STRING
            s = images
            str1 = ""
            for i in s:
                str1 += i 
                

####### IF "imgur" IS IN STRING FROM ABOVE, FILTER THE SCREENSHOT 
            if "imgur" in str1:
                attempt += 1
                text = str1
                start = text.index('i.imgur.com')
                end = text.index('.png',start)
                substring = text[start:end]
                nieuweimgurl = str ("https://"+ str(substring) + str(".png")) 


                url = nieuweimgurl
                filename = url.split('/')[-1]
                r = requests.get(url, allow_redirects=True)
                open(filename, 'wb').write(r.content)
                print("Ik heb een afbeelding gevonden en gedownload!")
                time.sleep(2.1)
            else:
                attempt += 1
                print("....")
                time.sleep(2.1)
####### WHEN ABOVE 900 TRY'S, RUN CODE ABOVE, BUT WITH 5 CHARACTERS
    if attempt > 900:
        
###LOOPING CODE BELOW 
        attempt = 0
        while True:

            
####### RANDOM LETTERS (6x)
            import string    
            import random # define the random module  
            S = 6  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            randomnummersresult = ''.join(random.choices(string.ascii_lowercase, k = S))    



####### REQUESTING AND FILTERING IMAGES
            URL = "https://prnt.sc/"  + str(randomnummersresult)
            getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
            soup = BeautifulSoup(getURL.text, 'html.parser')
            images = []
            for img in soup.findAll('img'):
                images.append(img.get('src'))

####### SPLIT URLS TO STRING
            s = images
            str1 = ""
            for i in s:
                str1 += i 
                

####### IF "imgur" IS IN STRING FROM ABOVE, FILTER THE SCREENSHOT 
            if "imgur" in str1:
                attempt += 1
                text = str1
                start = text.index('i.imgur.com')
                end = text.index('.png',start)
                substring = text[start:end]
                nieuweimgurl = str ("https://"+ str(substring) + str(".png")) 


                url = nieuweimgurl
                filename = url.split('/')[-1]
                r = requests.get(url, allow_redirects=True)
                open(filename, 'wb').write(r.content)
                print(str(attempt) + str ("Ik heb een afbeelding gevonden en gedownload!"))
                time.sleep(2.1)
            else:
                attempt += 1
                print(str(attempt) + str ("..."))
                time.sleep(2.1)
