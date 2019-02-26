#!usr/bin/env python3

# Date: 02-26-18, Feb ~ 26th 2019 | Synchronocy
# Project: DIscord Chat Monitor
# "No I don't remember saying that!"

currentissues = '''
1.) Some DB code won't input to the database.
2.) Not using any input validation, please use V1 this version is considered vuln to sqli.
3.) Messy code, need to follow the docco more.
4.) if you don't have an existing database without the required tables it will not work.
5.) possible emoji(none utf-8) characters may corrupt/malform the query
'''
import discord
import asyncio
import datetime
import os
import uuid
import sys
import requests
import sqlite3

print('Connecting to local database.')
connection = sqlite3.connect('./logs.db') # and yes I'll update it so you'll have all required tables and columns. just not right now.
cursor = connection.cursor()
client = discord.Client()
YOUR_TOKEN = "YourTokenHere."

now = datetime.datetime.now()
times = datetime.time(now.hour, now.minute, now.second)
print("\nLogging in using provided token.")
# Post
@client.event
async def on_ready():
    now = datetime.datetime.now()
    date = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    times = datetime.time(now.hour, now.minute, now.second)
    userdir = './logs/'+str(client.user.id)+'/'
    print('Logged in as')
    print('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Member of:')
    for x in client.servers:
        print('( '+str(x.id)+' ) '+str(x))
    print('\nDate: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')
    connection.commit()
    
    
@client.event
async def on_message(m):
    mattach = m.attachments
    now = datetime.datetime.now()
    date = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    times = datetime.time(now.hour, now.minute, now.second)
    prefix = '['+str(times)+"] ( "+str(m.server)+' ) ( '+str(m.channel)+" ) "+str(m.author)
    if mattach:
        for x in mattach:
            format_str = '''INSERT INTO uploads (timestamp, user, userid, link) VALUES ("{timestamp}", "{user}", "{userid}","{link}");'''
            sql_command = format_str.format(timestamp=times,user=str(m.author),userid=str(m.author.id),link=x.get('url'))
            cursor.execute(sql_command)
            connection.commit()
    if 'Direct' in str(m.channel):
        format_str = '''INSERT INTO dm (date, timestamp, user, message) VALUES ("{date}", "{timestamp}", "{user}","{message}");'''
        sql_command = format_str.format(date=date, timestamp=times,user=str(m.author),message=str(m.content))
        print(prefix+': '+str(m.content))
        cursor.execute(sql_command)
        connection.commit()
    else:
        format_str = '''INSERT INTO servers (date, timestamp, servername, channel, user, message) VALUES ("{date}", "{timestamp}","{servername}","{channel}", "{user}","{message}");'''
        sql_command = format_str.format(date=date, timestamp=times, servername=str(m.server),channel=str(m.channel), user=str(m.author),message=str(m.content))
        print(prefix+': '+str(m.content))
        cursor.execute(sql_command)
        connection.commit()
        
'''@client.event
async def on_server_join(server):
    print('User has joined: '+str(server))
    format_str = ''INSERT INTO servers (serverid, servername) VALUES ("{serverid}", "{servername}");''
    sql_command = format_str.format(serverid=str(server.id),servername=str(server))
    cursor.execute(sql_command)
    connection.commit()
'''
client.run(YOUR_TOKEN, bot=False)
