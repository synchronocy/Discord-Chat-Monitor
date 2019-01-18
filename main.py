import discord
import asyncio
import datetime
import os
import uuid
import sys


client = discord.Client()
YOUR_TOKEN = "yourtokenhere"

now = datetime.datetime.now()
times = datetime.time(now.hour, now.minute, now.second)

# Post
@client.event
async def on_ready():
    print('Logged in as')
    print('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Member of:')
    for x in client.servers:
        print('( '+str(x.id)+' ) '+str(x))
    print('\nDate: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')
    now = datetime.datetime.now()
    date = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    times = datetime.time(now.hour, now.minute, now.second)
    prefix = '['+str(times)+"] ( "+str(message.server)+' ) ('+str(message.channel)+" ) "+str(message.author)
    path = 'logs/'+client.user.id+'/'+client.user.name
    print(prefix)
    userdir = 'logs/'+str(client.user.id)+'/'
    def create():
        with open(userdir+'DMS'+date+'.txt','a') as a:
            with open(userdir+date+'.txt','a') as b:
                a.write('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n'+'Member of:\n')
                b.write('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n'+'Member of:\n')
                print('Done!')
                for x in client.servers:
                    a.write('( '+str(x.id)+' ) '+str(x)+'\n')
                    b.write('( '+str(x.id)+' ) '+str(x)+'\n')
                    a.write('-----------')
                    b.write('-----------')
    create()

@client.event
async def on_message(message):
    mattach = message.attachments
    now = datetime.datetime.now()
    date = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    times = datetime.time(now.hour, now.minute, now.second)
    prefix = '['+str(times)+"] ( "+str(message.server)+' ) ( '+str(message.channel)+" ) "+str(message.author)
    userdir = 'logs/'+str(client.user.id)+'/'
    if mattach:
        for x in mattach:
            print('File Upload Detected!\n'+prefix+' Uploaded: '+x.get('url'))
            with open(userdir+'Uploaded'+date+'.txt','a') as handle:
                try:
                    handle.write(prefix+' : '+x.get('url'))
                except Exception:
                    return ""
    '''if 'Direct' or 'None' in str(message.channel):
        with open(userdir+date+'.txt','a') as handle:
            try:
                handle.write(prefix+': '+str(message.content))
            except Exception:
                return ""'''# broken need to fix this function
    with open(userdir+date+'.txt','a') as handle:
        try:
            print(prefix+': '+str(message.content))
            handle.write(prefix+': '+str(message.content)+'\n')
        except Exception:
            return ""
client.run(YOUR_TOKEN, bot=False)
