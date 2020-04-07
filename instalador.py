#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


os.system("clear")

print("""
Author : D3pl0yzz Epysp
Contato: wa.me/+5582981690602
Telegram: @NinjaOFC
""")

import os
from termcolor import colored
from time import sleep


### Code



def instalar():
	
	print(colored("\nPython Install Repositores and Scripts\n",'red'))

	sleep(2)

	print("List\n")
	
	print("-" *20)
	
	print(colored("\n1 - ATSCAN \n2 - SQLMAP\n3 - HAMMER\n4 - SEND EMAIL\n5 - IP LOCATION\n6 - LITESPAM\n7 - METASPLOIT\n8 - NGROK\n9 - XERXES\n10 - WEEMAN\n11 - SAIR"))
	
	print("-" *20)
	
	option_user = int(input(colored("QUAL FERRAMENTA DESEJA OBTER : ",'green')))
	
	if option_user == 1: # atscan
			
		os.system("git clone https://github.com/AlisamTechnology/ATSCAN")
		
		print(colored('\nINSTALLED','green'))
		
	elif option_user == 2: # sqlmap
			
		os.system("git clone https://github.com/sqlmapproject/sqlmap")
		
		print(colored("\nINSTALLED",'green'))
		
	elif option_user == 3: #hammer
		
		os.system("git clone https://github.com/cyweb/hammer")
		
		print(colored("\nINSTALLED",'green'))
		
	elif option_user == 4: # Enviar_email
	
		os.system("git clone https://github.com/VictorONinja/enviar_email")
		
		sleep(3)
		
		print(colored("NESSE SCRIPT PRA PODER OLHE O REPOSITÓRIO DO CRIADOR (github.com/VictorONinja)\n",'red'))
		
		print(colored("\nINSTALLED",'green'))
		
	elif option_user == 5: # IP LOCATION
		
		os.system("git clone https://github.com/VictorONinja/IpLocation")
		
		print(colored("\nINSTALLED",'green'))
		
	elif option_user == 6: #LITESPAM
		
		os.system('clear')
		
		os.system("git clone https://github.com/4L13199/LITESPAM")
	
		print(colored("\nINSTALLED",'green'))
		
	elif option_user == 7: # METASPLOIT
		
		os.system("clear")
		
		os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh")
		
		print(colored("\nINSTALLED",'green'))
	
	
	elif option_user == 8: # NGROK
	
		os.system("clear")
		
		os.system("git clone https://github.com/PSecurity/ps.ngrok")
		
		print(colored("\nINSTALLED","green"))
		
	elif option_user == 9: # XERXES
		
		os.system("clear")
		
		os.system("git clone https://github.com/zanyarjamal/xerxes")
		
		print(colored("\nINSTALLED",'green'))

	elif option_user == 10: # WEEMAN
		
		os.system("clear")
		
		os.system("git clone https://github.com/evait-security/weeman")
		
		print(colored("\nINSTALLED","green"))
		
		
	elif option_user == 11:
		
		print(colored("OBRIGADO POR USAR <3",'red'))
		
		exit()
	
while True:
	instalar()
	
