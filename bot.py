#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	apt install python python-pip -y
#	pip install uptime telepot requests
#
import sys
import time
import random
import datetime
import uptime
from uptime import boottime
import telepot
import subprocess
import os
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import requests




requests.packages.urllib3.disable_warnings()

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    passp
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context





#####################################################################################################################
#######################################################VARIABLEN#####################################################
#####################################################################################################################

chat_id = 0

# Berechtigte Chat-IDs für Befehle

listOfIDs = [CHAT_ID_OF_YOUR_TELEGRAM_ACCOUNT]

#####################################################################################################################
#######################################################Funktionen####################################################
#####################################################################################################################


def measure_temp():
		temp = os.popen("sensors | grep Package | grep -o '.\{43\}$'").readline()
		return (temp.replace("temp=",""))


def systeminfo():
		os.system('free -h > /tmp/mem.txt')
		pathmem = '/tmp/mem.txt'
		memoryusage = open(pathmem,'r')
		memoryusage2 = memoryusage.read()
		return memoryusage2



def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']


	print 'Got command: %s' % command


#####################################################################################################################
#######################################################COMMANDS######################################################
#####################################################################################################################

	if command == '/start':
		if chat_id not in listOfIDs :
			bot.sendMessage(chat_id, 'Guten Tag!\n\nDieser Bot antwortet nur berechtigten Administratoren dieses Docker Servers.\nFür weitere Informationen sende meinem Admin eine Nachricht \n\nVielen Dank!')

	elif command == '/getcontainer':
		if chat_id in listOfIDs :
			os.system('docker ps -a --format "table {{.Image}}\t{{.Status}}" > /opt/zustand.txt')
			bot.sendDocument(chat_id, open('/opt/zustand.txt', 'rb'))

	elif command == '/getressources':
		if chat_id in listOfIDs :
			os.system('docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" | sort -k 4 -h > /opt/zustand.txt')
			bot.sendDocument(chat_id, open('/opt/zustand.txt', 'rb'))

	elif command == '/killcontainer':
		if chat_id in listOfIDs :
			keyboard = ReplyKeyboardMarkup(keyboard=[['all', 'the'], ['names', 'of'], ['your', 'Docker'], ['Container', 'Text']])
			bot.sendMessage(chat_id, 'Bitte wähle einen Container aus...', reply_markup=keyboard)

	elif command == 'all' or command == 'names' or command == 'of' or command == 'your' or command == 'Docker' or command == 'Container':
		if chat_id in listOfIDs :
			command
			os.system('docker container ls | grep {} | cut -c 1-12 - | xargs docker kill'.format(command))
			bot.sendMessage(chat_id,'{} wurde beendet!'.format(command),  reply_markup=ReplyKeyboardRemove())

	elif command == '/exit':
		if chat_id in listOfIDs :
			bot.sendMessage(chat_id, 'Chat wird beendet!'.format(command),  reply_markup=ReplyKeyboardRemove())

###################################################################################################################


	elif command == '/backup':
		if chat_id in listOfIDs :
			bot.sendMessage(chat_id, 'Der Server wird gesichert.\n\nBitte warten, dies kann einige Minuten in Anspruch nehmen! 🤷🏼‍♂️\n\n Du wirst benachrichtigt wenn der Vorgang abgeschlossen ist ☺️')
			os.system('bash /opt/bin/Backup_Script.sh --backup')
			bot.sendMessage(chat_id, 'Backup wurde hochgeladen!')

	elif command == '/reboot':
		if chat_id in listOfIDs :
			bot.sendMessage(chat_id, 'Der Server wird neu gestartet.')
			os.system('reboot')


	elif command == '/systeminfo':
		if chat_id in listOfIDs :
			bot.sendMessage(chat_id, 'Arbeitsspeicher:\n\n {}'.format(systeminfo()))
			bot.sendMessage(chat_id, 'CPU Temp:\n\n {}'.format(measure_temp()))
			bot.sendMessage(chat_id, 'Letzter Neustart:\n\n {}'.format(uptime._boottime_linux()))

	elif command == 'Danke':
		bot.sendMessage(chat_id, 'Gerne')



#####################################################################################################################
##############################################################S######################################################
#####################################################################################################################

bot = telepot.Bot('Telegram_Bot_TOKEN')
bot.message_loop(handle, run_forever=True)
