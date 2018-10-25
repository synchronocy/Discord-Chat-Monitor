# ADDED Folders drunk fyi
import discord
import asyncio
import datetime
import os
import uuid
import sys


client = discord.Client()
YOUR_TOKEN = sys.argv[1]

now = datetime.datetime.now()
times = datetime.time(now.hour, now.minute, now.second)

# Post
@client.event
async def on_ready():
    global now
    global times
    now = datetime.datetime.now()
    path = 'logs/'+str(client.user.id)
    def create():
        if not os.path.exists(path):
            os.mkdir(path)
            with open('logs/'+str(client.user.id)+'/'+client.user.name+'DMS'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as a:
                with open('logs/'+str(client.user.id)+'/'+client.user.name+'-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as b:
                    a.write('User: '+str(client.user.name)+'\n')
                    b.write('User: '+str(client.user.name)+'\n')
                    a.write('UserID: '+str(client.user.id)+'\n')
                    b.write('UserID: '+str(client.user.id)+'\n')
                    a.write('Email: '+str(client.email)+'\n')
                    b.write('Email: '+str(client.email)+'\n')
                    a.write('Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n')
                    b.write('Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n')
                    print('Done!')
                    a.write('Member of:\n')
                    b.write('Member of:\n')
                    for x in client.servers:
                        a.write('( '+str(x.id)+' ) '+str(x)+'\n')
                        b.write('( '+str(x.id)+' ) '+str(x)+'\n')
                    a.write('\n-----------')
                    b.write('\n-----------')

        else:
            pass
        # EOF create()
    print('Logged in as')
    print('User: '+str(client.user.name))
    print('UserID: '+str(client.user.id))
    print('Email: '+str(client.email))
    print('Member of: ')
    for x in client.servers:
        print('( '+str(x.id)+' ) '+str(x)+'\n')
    print('Date: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')
    create()    

# Log all Messages including files
@client.event
async def on_message(message):
    mattach = message.attachments
    global now
    global times
    now = datetime.datetime.now()
    times = datetime.time(now.hour, now.minute, now.second)
    if not mattach: # check if the message is an upload.
        pass
    else: # if it is get the url ~ plan to download
        for x in mattach:
            print(x.get('url'))
            print('\nFile Upload Detected: '+'\n'+str(times)+" ("+str(message.channel)+") "+str(message.author)+' Uploaded: '+x.get('url'))
            with open('logs/'+str(client.user.id)+'/'+'Uploaded-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
                handle.write('\n'+str(times)+" ("+str(message.server)+') ('+str(message.channel)+") "+str(message.author)+' Uploaded: '+x.get('url'))
    if 'Direct' in str(message.channel):
        with open('logs/'+str(client.user.id)+'/'+client.user.name+'DMS'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
            print("("+str(message.channel)+") "+str(message.author)+' : '+str(message.content))
            handle.write('\n'+str(times)+" ("+str(message.channel)+") "+str(message.author)+' : '+str(message.content))            
    else:
        with open('logs/'+str(client.user.id)+'/'+client.user.name+'-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
                print("("+str(message.server)+') '+'('+str(message.channel)+") "+str(message.author)+' : '+str(message.content))
                handle.write('\n'+str(times)+" ("+str(message.server)+') '+'('+str(message.channel)+") "+str(message.author)+' : '+str(message.content))         

client.run(YOUR_TOKEN, bot=False)


# December bday
