import discord
import asyncio
import datetime
import os
import uuid
import sys


client = discord.Client()
YOUR_TOKEN = "Yourtokenhere"

now = datetime.datetime.now()
times = datetime.time(now.hour, now.minute, now.second)
if not os.path.isdir('./logs'):
    os.makedirs('./logs')
# Post
@client.event
async def on_ready():
    global now
    global times
    now = datetime.datetime.now()
    path = 'logs/'+str(client.user.id)
    if not os.path.isdir('./logs/'+str(client.user.id)+'/'):
        os.makedirs('./logs/'+str(client.user.id)+'/')
    with open('logs/'+str(client.user.id)+'/'+client.user.name+'DMS'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as a:
        with open('logs/'+str(client.user.id)+'/'+client.user.name+'-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as b:
            a.write('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n'+'Member of:\n')
            b.write('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n'+'Member of:\n')
            for x in client.servers:
                try:
                    a.write('( '+str(x.id)+' ) '+str(x)+'\n')
                    b.write('( '+str(x.id)+' ) '+str(x)+'\n')
                except Exception:
                    print('Error Writing server name to file.')
            b.write('---------\n')
        a.write('----------\n')
    print('Logged in as')
    print('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Member of:')
    for x in client.servers:
        print('( '+str(x.id)+' ) '+str(x))
    print('\nDate: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')

@client.event
async def on_message(message):
    mattach = message.attachments
    global now
    global times
    now = datetime.datetime.now()
    times = datetime.time(now.hour, now.minute, now.second)
    if not mattach:
        pass
    else:
        for x in mattach:
            with open('logs/'+str(client.user.id)+'/'+'Uploaded-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
                try:
                    print('File Upload Detected: \n'+str(times)+" ("+str(message.channel)+") "+str(message.author)+' Uploaded: '+x.get('url'))
                    handle.write('\n'+str(times)+" ( "+str(message.server)+' ) ( '+str(message.channel)+" ) "+str(message.author)+' Uploaded: '+x.get('url'))
                except Exception:
                    return "Unable to write to file. Unknown ascii type."
    if 'Direct' or 'None' in str(message.channel):
        with open('logs/'+str(client.user.id)+'/'+client.user.name+'DMS'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
            try:
                print(str(times)+' ( '+str(message.server)+' ) ( '+str(message.channel)+" ) "+str(message.author)+' : '+str(message.content))
                handle.write('\n'+str(times)+" ( "+str(message.server)+' ) ( '+str(message.channel)+" ) "+str(message.author)+' : '+str(message.content))
            except Exception:
                return ""
    else:
        with open('logs/'+str(client.user.id)+'/'+client.user.name+'-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
            try:
                print("( "+str(times)+" ( "+str(message.server)+' ) ( '+str(message.channel)+" ) "+str(message.author)+' : '+str(message.content))
                handle.write('\n'+str(times)+" ( "+str(message.server)+' ) ( '+str(message.channel)+" ) "+str(message.author)+' : '+str(message.content))
            except Exception:
                return ""

client.run(YOUR_TOKEN, bot=False)
