import discord
import asyncio
import datetime
import os
import uuid
import sys
import requests

client = discord.Client()
YOUR_TOKEN = "Yourtokenhere"

now = datetime.datetime.now()
times = datetime.time(now.hour, now.minute, now.second)

# Post
@client.event
async def on_ready():
    now = datetime.datetime.now()
    print('Logged in as')
    print('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Member of:')
    for x in client.servers:
        print('( '+str(x.id)+' ) '+str(x))
    print('\nDate: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')
    date = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    times = datetime.time(now.hour, now.minute, now.second)
    path = 'logs/'+client.user.id+'/'+client.user.name
    userdir = 'logs/'+str(client.user.id)+'/'
    if not os.path.isdir(userdir):
        os.makedirs(userdir)
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
            response = requests.get(x.get('url'))
            if response.status_code == 200:
                with open("logs/"+client.user.id+'/files/'+str(uuid.uuid4())+'.'+x.get('url')[len(x.get('url'))-3:], 'wb') as f:
                    f.write(response.content)
            with open(userdir+'Uploaded'+date+'.txt','a') as handle:
                try:
                    handle.write(prefix+' : '+x.get('url')+'\n')
                except Exception:
                    return ""
    with open(userdir+date+'.txt','a') as handle:
        try:
            print(prefix+': '+str(message.content))
            handle.write(prefix+': '+str(message.content)+'\n')
        except Exception:
            return ""
client.run(YOUR_TOKEN, bot=False)
