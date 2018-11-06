import discord
import asyncio
import datetime
import os
import uuid
import sys


client = discord.Client()
YOUR_TOKEN = "NDg2MTQ2MDQ0Mzg4NzA0MjY4.Dr2yFg.QRFCXS3Al29YJuzd3o1DlLJRQSg"

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
                    a.write('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n'+'Member of:\n')
                    b.write('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'\n'+'Member of:\n')
                    print('Created new user!') # new improvements just tidied up the code
                    for x in client.servers:
                        a.write('( '+str(x.id)+' ) '+str(x)+'\n')
                        b.write('( '+str(x.id)+' ) '+str(x)+'\n')
                    a.write('-----------')
                    b.write('-----------')

        else:
            pass
    print('Logged in as')
    print('User: '+str(client.user.name)+'\n'+'UserID: '+str(client.user.id)+'\n'+'Email: '+str(client.email)+'\n'+'Member of:')
    for x in client.servers:
        print('( '+str(x.id)+' ) '+str(x))
    print('\nDate: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')
    create()    
    
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
            #print(x.get('url'))
            print('File Upload Detected: \n'+str(times)+" ("+str(message.channel)+") "+str(message.author)+' Uploaded: '+x.get('url'))
            with open('logs/'+str(client.user.id)+'/'+'Uploaded-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
                handle.write('\n'+str(times)+" ("+str(message.server)+') ('+str(message.channel)+") "+str(message.author)+' Uploaded: '+x.get('url'))
    if 'Direct' or 'None' in str(message.channel):
        with open('logs/'+str(client.user.id)+'/'+client.user.name+'DMS'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
            print(str(times)+" ("+str(message.channel)+") "+str(message.author)+' : '+str(message.content))
            handle.write('\n'+str(times)+" ("+str(message.channel)+") "+str(message.author)+' : '+str(message.content))            
    else:
        with open('logs/'+str(client.user.id)+'/'+client.user.name+'-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt','a') as handle:
                print("("+str(message.server)+') '+'('+str(message.channel)+") "+str(message.author)+' : '+str(message.content))
                handle.write('\n'+str(times)+" ("+str(message.server)+') '+'('+str(message.channel)+") "+str(message.author)+' : '+str(message.content))         

client.run(YOUR_TOKEN, bot=False) # remove bot=False if you're logging
