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

'''if not os.path.isdir('./logs'):
    os.makedirs('./logs')

''' 
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
    if not os.path.isdir('./logs/'+str(client.user.id)+'/'):
        os.makedirs('./logs/'+str(client.user.id)+'/files/servers')
        os.makedirs('./logs/'+str(client.user.id)+'/files/users')
    def create():
        if os.path.exists(userdir+str(client.user.name)+'-UserInfo-'+date+'.txt'):
            os.remove(userdir+str(client.user.name)+'-UserInfo-'+date+'.txt')
        with open(userdir+str(client.user.name)+'-UserInfo-'+date+'.txt','a') as a:
            a.write('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n'+'Member of:\n')
            print('Done!')
            for x in client.servers:
                try:
                    a.write('( '+str(x.id)+' ) '+str(x)+'\n')
                except Exception:
                    print('Error Unable to write server to file.')
    create()

@client.event
async def on_message(message):
    mattach = message.attachments
    now = datetime.datetime.now()
    date = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    times = datetime.time(now.hour, now.minute, now.second)
    prefix = '['+str(times)+"] ( "+str(message.server)+' ) ( '+str(message.channel)+" ) "+str(message.author)
    userdir = './logs/'+str(client.user.id)+'/'
    if mattach:
        for x in mattach:
            response = requests.get(x.get('url'))
            if response.status_code == 200:
                if 'None' in str(message.server):
                    if not os.path.isdir('./logs/'+str(client.user.id)+'/files/users/'+str(message.channel)[20:]):
                        try:
                            os.mkdir('./logs/'+str(client.user.id)+'/files/users/'+str(message.channel)[20:])
                            with open('./logs/'+str(client.user.id)+'/files/users/'+str(message.channel)[20:]+'/'+date+'-'+str(uuid.uuid4())+'.'+x.get('url')[len(x.get('url'))-3:], 'wb') as f:
                                f.write(response.content)
                        except Exception:
                            os.mkdir('./logs/'+str(client.user.id)+'/files/users/'+str(message.channel.id))
                            with open('./logs/'+str(client.user.id)+'/files/users/'+str(message.channel.id)+'/'+date+'-'+str(uuid.uuid4())+'.'+x.get('url')[len(x.get('url'))-3:], 'wb') as f:
                                f.write(response.content)                            
                else:
                    if not os.path.isdir('./logs/'+str(client.user.id)+'/files/servers/'+str(message.server)+'/'):
                        try:
                            os.mkdir('./logs/'+str(client.user.id)+'/files/servers/'+str(message.server)+'/')
                            with open('./logs/'+str(client.user.id)+'/files/servers/'+str(message.server)+'/'+date+'-'+str(uuid.uuid4())+'.'+x.get('url')[len(x.get('url'))-3:], 'wb') as f:
                                f.write(response.content)
                        except Exception:
                            os.mkdir('./logs/'+str(client.user.id)+'/files/servers/'+str(message.server.id)+'/')
                            with open('./logs/'+str(client.user.id)+'/files/servers/'+str(message.server.id)+'/'+date+'-'+str(uuid.uuid4())+'.'+x.get('url')[len(x.get('url'))-3:], 'wb') as f:
                                f.write(response.content)
                    
            with open(userdir+'Uploaded'+date+'.txt','a') as handle:
                try:
                    print('File Upload Detected!\n'+prefix+' Uploaded: '+x.get('url'))
                    handle.write(prefix+' : '+x.get('url')+'\n')
                except Exception:
                    return ""
    if 'None' in str(message.server):
        with open(userdir+str(client.user.name)+'-DMS'+date+'.txt','a') as dms:
            try:
                print(prefix+': '+str(message.content)+'\n')
                dms.write(prefix+': '+str(message.content)+'\n')
            except Exception:
                return ""
    else:
        with open(userdir+str(client.user.name)+'-'+date+'.txt','a') as handle:
            try:
                print(prefix+': '+str(message.content))
                handle.write(prefix+': '+str(message.content)+'\n')
            except Exception:
                return ""
client.run(YOUR_TOKEN, bot=False)
