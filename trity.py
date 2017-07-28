# coding: utf-8
#!/usr/bin/env python
import sys, platform, subprocess, socket, time, os, urllib,  random, string, smtplib, urllib2, getpass, zipfile
from urllib2 import urlopen
from time import sleep
from getpass import getpass
from subprocess import call
sys.path.append('trity/')
from smtp import *
from sms import *
from xss import *
from crafttable import *
from info import *
from anon import *
from twitter import *
from whoisweb import *
from coder import *
from clone import *
from admin import *
from banner import *
from joke import *
from quote import *
from web import *
from qr import *
from siteexists import *
from hex import *
from searchs import *
from zip import *
from emaill import *
from sql import *

VersionNum = "3.4" ####### Main for all

try:
    import scapy
    import pip
    import requests
    import pythonwhois
    import argparse
    import google
except ImportError as e:
    print (color.UNDERLINE + "\033[91m" + "Nu aveti instalate unele module! \ Verificați install.py pentru a instala complet acest tool! " + color.END)
    print "Error: {}".format(e)
    print "Execute: pip install (module name)"
    if (e) == "DependencyWarning":
	os.system("sudo apt-get update")
	os.system("apt-get remove python-pip")
	os.system("easy_install pip")
	os.system("sudo pip uninstall requests")
	os.system("sudo pip install requests")
    elif (e) == "Unable to locate package lib32ncurses5":
	os.system("sudo apt-get update")
	os.system("sudo apt-get install lib32ncurses5 lib32bz2-1.0")
    sys.exit()
###############################
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
###############################
os.system('clear')
if str(platform.system()) != "Linux":
	sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Nu utilizați un sistem bazat pe Linux! Linux este un must-have pentru acest scenariu!" + color.END)
if not os.geteuid() == 0:
    sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Trebuie să fie rulat ca root. :/" + color.END)
if 'no' in open('agree.txt').read():# take out the trity/
    print color.BOLD + """
Rețineți că Trity este furnizat ca atare și este o aplicație open source fără licență.

Simțiți-vă liber să modificați, să utilizați, să schimbați, să comercializați, să faceți ce vreți cu el, atâta timp cât acordați creditul adecvat în cazul în care creditul este datorat (ceea ce înseamnă că acordați autorilor creditul pe care îl merită pentru scris).

De asemenea, prin utilizarea acestui instrument, ar trebui să încercați să faceți acest instrument mai bine, să încercați să vă poziționați pozitiv, să încercați să îi ajutați pe ceilalți, să încercați să învățați unul de celălalt, să încercați să stați departe de dramă, să încercați să oferiți îmbrățișări gratuite atunci când este posibil La îmbrățișare reciprocă) și încercați să faceți tot ce puteți pentru a fi minunat.
Tritatea este concepută exclusiv pentru bine și nu pentru rău. Dacă intenționați să utilizați acest instrument în scopuri dăunătoare, care nu sunt autorizate de compania pe care o efectuați evaluări, încălcați termenii și condițiile de utilizare și licența acestui set de instrumente. Prin lovirea da (doar o singură dată), sunteți de acord cu termenii și condițiile și că veți folosi acest instrument doar în scopuri legale.
"""
    agree = raw_input(''+G+'' + color.UNDERLINE + 'Sunteți de acord cu acești termeni și condiții? Daca da scrieti "y" sau "yes">' + color.END)
    if agree == "yes":
	print (''+G+'' + color.UNDERLINE + 'Multumesc!' + color.END)
	time.sleep(3)
	FILE = open("agree.txt","w")# take out the trity/
        FILE.write('yes')
        FILE.close()
    elif agree == "y":
	print (''+G+'' + color.UNDERLINE + 'Multumesc!' + color.END)
	time.sleep(3)
	FILE = open("agree.txt","w")# take out the trity/
        FILE.write('yes')
        FILE.close()
    elif agree == "Yes":
	print (''+G+'' + color.UNDERLINE + 'Multumesc!' + color.END)
	time.sleep(3)
	FILE = open("agree.txt","w")# take out the trity/
        FILE.write('yes')
        FILE.close()
    else:
	print (''+R+'' + color.UNDERLINE + '[!] You have to agree!' + color.END)
	time.sleep(1)
	sys.exit()
os.system('clear')
banner()
#============================================================#
#------------------- Onto the real stuff --------------------#
#============================================================#
def banner1():
    print ""
    print ""+M+"|----- Creat de _t0x1c -----|"
    print color.DARKCYAN +"|-----      Version: {}        -----|".format(VersionNum)
    print color.WARNING + "|-----   1 tool - 34 alegeri    -----|"
    print color.PURPLE + "\n|----- Bine ai venit la Trinity! -----|"
    print color.BLUE + "|----- Translated in Romanian by P1NNgU ! -----|"
    print color.YELLOW + "|----- Distrează-te și rămâi anonym ! -----|"

time.sleep(0.1)
print ""
time.sleep(0.1)
print ""+M+"|----- Creat de _t0x1c  -----|" 
time.sleep(0.1)
print color.DARKCYAN + "|-----      Version: {}        -----|".format(VersionNum)
time.sleep(0.1)
print color.WARNING + "|-----   1 tool - 34 alegeri    -----|"
time.sleep(0.1) 
print color.PURPLE + "\n|----- Bine ai venit la Trinity! -----|"
time.sleep(0.1)
print color.BLUE + "|----- Translated in Romanian by P1NNgU! -----|"
time.sleep(0.1)
print color.YELLOW + "|----- Distrează-te și rămâi anonym ! -----|"
time.sleep(0.1)
r = requests.get('http://pastebin.com/raw/vYcBSV4w') 

if (VersionNum) not in r.text:
    print (''+R+'\nYou need to update! The newest version is: ' + color.BOLD + color.UNDERLINE + r.text + '\n')
    time.sleep(5)
else:
    print ('')
swear = "fuck", "shit", "nigga", "bitch", "dick", "pussy", "cunt", "nigger", "asshole", "ass"
spell = "helpp", "hellp", "bannerr", "baner", "emial", "HELP", "hwlp", "wesbite", "ehco", "anonymouss", "anonymouse", "toool", "tooll", "carft", "Info", "spooof", "spooff", "ecnode", "decde", "encde", "craftt", "qoute", "sitexists", "hlep", "claer", "twiter", "xxs", "sqll", "xsss", "xs"
def tritymain():
    while True:
        try:
            main = raw_input(''+G+'' + color.BOLD + color.UNDERLINE + 'Tri>' + color.END)
            if main in swear:
                print(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Ai grija la vorba !" + color.END)
	    elif main in spell:
                print(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Știi cum să spui?!" + color.END)
            elif main == "joke":
                joke()
            elif main == "info":
                info()
            elif main == "help":
                print ""+W+"+----------------------------+"
                print ""+C+"help "+W+"- Afiseaza comenzile de Ajutor"
                print ""+C+"clear "+W+"- Sterge ecranul "
                print ""+C+"exit "+W+"- Iesi din Tool"
                print ""+C+"tool "+W+"- Arata informatii despre Tool"
                print ""+C+"info "+W+"- Afișează informații despre computer și retea"
                print ""+C+"cd "+W+"- Schimba directoarele de lucru"
                print ""+W+"+----------------------------+"
                print ""+P+"speak "+W+"- Textul în vorbire"
                print ""+P+"ping "+W+"- Ping la un HOST "
                print ""+P+"banner "+W+"- Tipareste un nou banner"
                print ""+P+"joke "+W+"- Spune o gluma"
                print ""+P+"quote "+W+"- Tipareste un citat"
                print ""+P+"contact "+W+"- Contacteaza-ma"
                print ""+W+"+----------------------------+"
                print ""+R+"website "+W+"- Introduce un site si obtinei adresa IP"
	        print ""+R+"clone"+W+" - Clona la o sursa de Website-uri web "
	        print ""+R+"whois"+W+" - Informatii despre un site web"
	        print ""+R+"web"+W+" - Extragi informatii de pe un site web"
	        print ""+R+"siteexists"+W+" - Verifici daca exista un site web"
	        print ""+R+"google"+W+" - Gasesti rezultate Google pentru o interogare"
                print ""+W+"+----------------------------+"
	        print ""+G+"ip "+W+"- Obtii detalii despre o adresa IP"
                print ""+W+"+----------------------------+"
	        print ""+O+"xss "+W+"- Verificati simplu pentru o vulnerabilitate xss"
	        print ""+O+"sql "+W+"- Verificarea de bază pentru o vulnerabilitate sql "
	        print ""+O+"admin "+W+"- Scaneaza AdminPannel la un site Web"
                print ""+W+"+----------------------------+"
	        print ""+T+"email "+W+"- Bomba o adresă de e-mail ( Nu stiu  ce face aceasta , puteti verifica) "
	        print ""+T+"spoof email "+W+"- Pastrati o adresă de e-mail"
	        print ""+T+"anonymous "+W+"- Trimiti un email anonym"
	        print ""+T+"sms"+W+" - Spam cu un anumit text(mesaj)  "
                print ""+T+"twitter"+W+" - Detalii despre un cont de Twitter"
                print ""+W+"+----------------------------+"
	        print color.CYAN + "craft"+W+" - Genereaza scripturi utile  "
	        print color.CYAN + "qr"+W+" - Genereaza un cod qr"
	        print color.CYAN + "zip"+W+" - Sparge un fișier zip protejat prin parolă"
                print ""+W+"+----------------------------+"
	        print color.BLUE + "encode base64"+W+" - Textul la baza64"
	        print color.BLUE + "decode base64"+W+" - Base64 la text"
	        print color.BLUE + "encode hex"+W+" - Text la hexazecimal"
	        print color.BLUE + "decode hex"+W+" - Hex la text"
                print ""+W+"+----------------------------+"
    	    elif main == "sms":
	        sms()
	    elif main == "xss":
	        xss()
	    elif main == "sql":
	        sql()
	    elif main == "anonymous":
	        anon()
	    elif main == "encode base64":
	        encode()
	    elif main == "decode base64":
	        decode()
	    elif main == "email":
	        smtp()
	    elif main == "quote":
	        quote()
	    elif main == "spoof email":
	        spoofemail()
	    elif main == "zip":
	        zipfile()
	    elif main == "decode hex":
	        decode1()
	    elif main == "encode hex":
	        encode1()
	    elif main == "google":
	        googleSearch()
	    elif main == "web":
	        web()
	    elif main == "siteexists":
	        siteexists()
	    elif main == "qr":
	        gen_qrcode()
	    elif main == "twitter":
	        twitter()
	    elif main == "anonymous":
	        anon()
	    elif main == "contact":
	        print(''+T+'' + color.UNDERLINE + 'Skype:'+W+'' + color.BOLD + ' live:mielsenpenguin' + color.END)
	        print(''+T+'' + color.UNDERLINE + 'Youtube:'+W+'' + color.BOLD + ' https://www.youtube.com/channel/UCCcNQuNtq6bsb9ID5wV9tNQ' + color.END)
	        print(''+T+'' + color.UNDERLINE + 'Email:'+W+'' + color.BOLD + ' mielsenpenguin@gmail.com' + color.END)
	    elif main == "ping":
		while True:
	            hostname = raw_input(''+T+'' + color.UNDERLINE + 'Host>' + color.END)
	            os.system("ping " + hostname)
	    elif main == "craft":
		while True:
	            table()
	    elif main == "whois":
	        whoisweb()
	    elif main == "admin":
	        admin()
	    elif main == "banner":
	        os.system('clear')
	        banner()
	        banner1()
	    elif main == "speak":
		while True:
	            speak = raw_input(''+T+'' + color.UNDERLINE + 'Ce de spus>' + color.END)
	            os.system('espeak "' + speak + '"')
	    elif main == "clone":
	        clone()
	    elif main == "cd":
	        try:
	            path = raw_input(''+T+'' + color.UNDERLINE + 'Directory>' + color.END)
	            os.chdir(path)
	        except OSError:
	            print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Acesta nu este un director!" + color.END)
	    elif main == "tool":
	        print(color.UNDERLINE + ''+C+'Version: ' + (VersionNum) + color.END)
		print(color.UNDERLINE + ''+C+'34 Optiuni de alegere!' + color.END)
	        print(color.UNDERLINE + ''+C+'Time spent on it: 76 hours - 14 minutes' + color.END)
	        print(color.UNDERLINE + ''+C+'toxic is a sp00ky h4ck3r' + color.END)
	    elif main == "website":
		while True:
	            a = raw_input(''+T+'' + color.UNDERLINE + 'Website>' + color.END)
	            try:
	                print socket.gethostbyname(a)
	            except socket.gaierror:
	                print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Se pare ca hostul este necunoscută! :/" + color.END)
	    elif main == "ip":
	        ip = raw_input(''+T+'' + color.UNDERLINE + 'IP>' + color.END)
	        if ip is None or ip == "":
	            sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Te rog introduce o adresa IP!" + color.END)
	        reversed_dns = socket.getfqdn(ip)
	        geoip = urllib.urlopen('http://api.hackertarget.com/geoip/?q='
                               + ip).read().rstrip()
	        print (""+G+"[*] " + color.UNDERLINE + "\033[91m" + "IP Info" + color.END)
	        print geoip
	    elif main == "clear":
	        os.system('clear')
            elif main == "exit":
	        print (""+G+"[*] " + color.UNDERLINE + "\033[91m" + "Iesite..." + color.END)
	        print (""+G+"[*] " + color.UNDERLINE + "\033[92m" + "Pa pa !" + color.END)
	        time.sleep(0.2)
	        sys.exit()
	    elif main == "":
	        print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Te rog introduce o obtiune!" + color.END)
            else:
	        print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Aceasta nu este o opțiune!" + color.END)
        except KeyboardInterrupt:
		print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "\nCtrl-C Pressed! Utilizați "exit" pentru a închide tool!" + color.END)
		tritymain()
tritymain()
