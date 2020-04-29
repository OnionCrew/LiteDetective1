import sys
import time
import tqdm
import urllib.request
import json
import os
import pyfiglet
from pyfiglet import Figlet
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty()) 
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('LiteDetective'),'yellow', 'on_red', attrs=['bold'])
language1 = print("[1]Русский")
language2 = print("[2]English")
language3 = print("[3]Polish")
language4 = print("[4]German")
language5 = print("[5]French")

lang = input("Choose a language: ")

if lang == "2":
           getIP = input("[+] Enter IP -> ")
           url = "https://ipinfo.io/" + getIP + "/json"

           try:     
              getInfo = urllib.request.urlopen( url )

           except:
               print( "\n[!] - IP not found - [!]\n" )
               sys.exit()
 
           infoList = json.load(getInfo)
 
           def whoisIPinfo(ip):
 
            try:
               sys.exit()
               myComand = "whois" + getIP
               whoisInfo = os.popen( myComand ).read()
               return whoisInfo

 
            except:
               return ""
           print( "-" * 60 )
           print("#####################################")
           print( "IP: ", infoList["ip"] )
           print( "City: ", infoList["city"] )
           print( "Region: ", infoList["region"] )
           print( "Country: ", infoList["country"] )
           print( "Hostname: ", infoList["hostname"] )
           print( "Timezone: ", infoList["timezone"] )
           print("Location: ", infoList["loc"] )
           print("#####################################")
           print( "-" * 60 )
           print( whoisIPinfo ( getIP ) )

elif lang == "1":
        getIP = input("[+] Введите IP -> ")
        url = "https://ipinfo.io/" + getIP + "/json"

        try:
           getInfo = urllib.request.urlopen( url )

        except:
            print( "\n[!] - IP не найден - [!]\n" )
            sys.exit()

        infoList = json.load(getInfo)

        def whoisIPinfo(ip):

         try:
           sys.exit()
           myComand = "whois " + getIP
           whoisInfo = os.popen( myComand ).read()
           return whoisInfo

         except:
            return ""
        print( "-" * 60 )
        print("#####################################")
        print( "IP: ", infoList["ip"] )
        print( "Регион: ", infoList["city"] )
        print( "Город: ", infoList["region"] )
        print( "Страна: ", infoList["country"] )
        print( "Хост: ", infoList["hostname"] )
        print( "Часовой пояс: ", infoList["timezone"] )
        print("Приблизительные координаты: ", infoList["loc"] )
        print("#####################################")
        print( "-" * 60 )
        print( whoisIPinfo ( getIP ) )
elif lang == "3":
          getIP = input("[+] Enter IP -> ")
          url = "https://ipinfo.io/" + getIP + "/json"

          try:
             getInfo = urllib.request.urlopen( url )

          except:
              print( "\n[!] - Nie znaleziono adresu IP - [!]\n" )
              sys.exit()

          infoList = json.load(getInfo)

          def whoisIPinfo(ip):

           try:
             sys.exit()
             myComand = "whois " + getIP
             whoisInfo = os.popen( myComand ).read()
             return whoisInfo

           except:
              return ""
          print( "-" * 60 )
          print("#####################################")
          print( "IP: ", infoList["ip"] )
          print( "Miasto: ", infoList["city"] )
          print( "Region: ", infoList["region"] )
          print( "Kraj: ", infoList["country"] )
          print( "Nazwa hosta: ", infoList["hostname"] )
          print( "Strefa czasowa: ", infoList["timezone"] )
          print("Współrzędne: ", infoList["loc"] )
          print("#####################################")
          print( "-" * 60 )
          print( whoisIPinfo ( getIP ) )
elif lang == "4":
          getIP = input("[+] Eingeben IP -> ")
          url = "https://ipinfo.io/" + getIP + "/json"

          try:
             getInfo = urllib.request.urlopen( url )

          except:
              print( "\n[!] - IP nicht gefunden - [!]\n" )
              sys.exit()

          infoList = json.load(getInfo)

          def whoisIPinfo(ip):

           try:
             sys.exit()
             myComand = "whois " + getIP
             whoisInfo = os.popen( myComand ).read()
             return whoisInfo

           except:
              return ""
          print( "*" * 60 )
          print("#####################################")
          print( "IP: ", infoList["ip"] )
          print( "Stadt: ", infoList["city"] )
          print( "Region: ", infoList["region"] )
          print( "Land: ", infoList["country"] )
          print( "Hostname: ", infoList["hostname"] )
          print( "Zeitzone: ", infoList["timezone"] )
          print( "Koordinaten: ", infoList["loc"] )
          print("#####################################")
          print( "*" * 60 )



elif lang == "5":
          getIP = input("[+] Entrer IP -> ")
          url = "https://ipinfo.io/" + getIP + "/json"

          try:
             getInfo = urllib.request.urlopen( url )

          except:
              print( "\n[!] - IP introuvable - [!]\n" )
              sys.exit()

          infoList = json.load(getInfo)

          def whoisIPinfo(ip):

           try:
             sys.exit()
             myComand = "whois " + getIP
             whoisInfo = os.popen( myComand ).read()
             return whoisInfo

           except:
              return ""
          print( "*" * 60 )
          print("#####################################")
          print( "IP: ", infoList["ip"] )
          print( "Ville: ", infoList["city"] )
          print( "Région: ", infoList["region"] )
          print( "Pays: ", infoList["country"] )
          print( "Nom d'hôte: ", infoList["hostname"] )
          print( "Fuseau horaire: ", infoList["timezone"] )
          print( "Coordonnées: ", infoList["loc"] )
          print("#####################################")
          print( "*" * 60 )

elif lang > "5":
        print("Incorrect value")
        sys.exit()
elif lang < "1":
        print("Incorrect value")
        sys.exit()

 
