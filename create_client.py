#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://github.com/LonamiWebs/Telethon/issues/46
from telethon import TelegramClient
import sqlite3
import time

db = sqlite3.connect('Account.db')
cur = db.cursor()

cur.execute(f"SELECT * FROM Account")
amount_of_users=len(cur.fetchall())

start=1
while start<amount_of_users+1:
	try:
		for user_id in range(start,amount_of_users+1):
			cur.execute(f"SELECT * FROM Account WHERE ID = '{user_id}'")
			components=cur.fetchall().copy()[0]
			name,phone,api_id,api_hash=components[1],components[2],components[3],components[4]
			print("Входим в аккаунт: "+str(user_id)+") "+phone+" ("+name+")")			
			print(api_id,api_hash)
			api_id=input().strip()
			api_hash=input().strip()
			
			session="app"+str(user_id)
			client=TelegramClient(session, api_id, api_hash)
			client.start()

			user_id+=1
			time.sleep(1)
	except Exception as e:
		print(e)
		start=user_id+1

input("Aккаунты активированы!")
