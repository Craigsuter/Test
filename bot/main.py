import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
#imports
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
from dotenv import load_dotenv
load_dotenv()
import datetime
from time import strptime
import asyncio
import time
from translation import translations
from dropboxUploader import upload_file
from dropboxUploader import download_file


#sets up command prefix
intents = discord.Intents().all()
client = commands.Bot(command_prefix = '!', intents=intents)



#This is the OG URL for Dota 2 / CSGO / Valo
my_url = 'https://liquipedia.net/dota2/OG'
my_url2 = 'https://liquipedia.net/counterstrike/OG'
my_url3 = 'https://liquipedia.net/valorant/OG'
global my_url5
global my_url6
global my_url7
global dotadailypost
global csgodailypost
global valodailypost


dotadailypost = True
csgodailypost = True
valodailypost = True

#Posts once bot has started up
startup = datetime.datetime.now()

print("Bot started up at: ", startup)



#Logs the discord bot on
@client.event
async def on_ready():
    print("We have logged in as {0.user}.format(client)")
    #Sets presence
    await client.change_presence(activity=discord.Game(name="with languages (use !translationhelp)"))

    


#Starts the bot up to check for messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
      return
    
    guild=message.guild
    
    
#All commands that are blocked to none admins are found in here
    global currenttime
    global currentH
    global currentM
    global currentd
    global dotadailypost
    global csgodailypost
    global valodailypost
    currenttime =  datetime.datetime.now()
    #day
    currentd = currenttime.strftime("%d")
    #hour [UK time - 1]
    currentH = currenttime.strftime("%H")
    #Minute
    currentM = currenttime.strftime("%M")
    #Month
    currentmonth = currenttime.strftime("%m")
    #year
    currentyear = currenttime.strftime("%y")
    #second
    currentsecond = currenttime.strftime("%S")
    
    

    currentH = int(currentH)
    currentM = int(currentM)
    author=message.author
    areadmin = author.guild_permissions.administrator



    global my_url5
    global my_url6
    global my_url7

    #Gets segments of every message - full message found in 'fullMEssage to avoid over use of Discord API'
    fullMessage = message.content
    nexttrans= fullMessage
    sectionsofmessage = fullMessage.rsplit(" ")
    introtomessage = sectionsofmessage[0]
    first_char = introtomessage[0]
    channelDataID = message.channel.id

    #Getting the 2nd part of a message
    try:
      secondPartOfMessage= sectionsofmessage[1]
    except:
      secondPartOfMessage = "none"
      
      

    messagetolower = introtomessage
    messagereceived = messagetolower.lower()
    mention = f'<@!{client.user.id}>'
    #Checks for a ping of the bot
    if ((mention in message.content) and (messagereceived[0] != '!')):
      await message.channel.send("Im up! How can I help? if you're running into issues you're able to reach out at my support server - https://discord.gg/HzEhdZApP4")


    
    #Translation bot testing area
    try:
      data = download_file('/droptranslationchannels.txt', 'translationchannels.txt')
      a_file = open("translationchannels.txt","r")
      datatester = a_file.read()
      value = datatester.rsplit(",")
    except:
      value="blooooooooooooooooooo"
      print("No file found")
    

    if(str(channelDataID) in value):
      download_file('/droptranslationchannelstosendtoo.txt', 'translationchannelstosendtoo.txt' )
      
      location = value.index(str(channelDataID))

      a_file =open("translationchannelstosendtoo.txt", "r")
      datascan = a_file.read()
      values = datascan.rsplit(",")

      channeltosendtoo = values[int(location)]
      channel = message.guild.get_channel(int(channeltosendtoo))

      
      msgID = message.jump_url
      author = message.author
      data = translations(nexttrans, author, msgID)
      #Getting translation data
      embed=data
      await channel.send(embed=embed)



    #None mod commands
    if (author.guild_permissions.administrator == False):
        if(messagereceived=="!translationhelp"):
          await message.channel.send("You're not an administrator in this server")
        

        if (messagereceived =="!BZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZARk234283u49234"):
          willshelp1 = "!nextdota - This will tell you the next OG Dota 2 game coming up \n!nextcsgo - This will tell you the next OG CSGO game coming up \n!nextvalo - This will tell you the next OG Valorant  game coming up \n \n"

          willshelp2 = "!dotastreams / !dotastreams2 [B-Streams listed for our team] - This will tell you the streams available for the next / current series of dota happening!\n!csgostreams - This will tell you the next / current CSGO games streams\n!valostreams - This will tell you the streams for the current / next Valorant series"
          willshelp3= "!nextdt - This will tell you the next game coming up in the currently tracked tournament"
          willshelp4 = "!teaminfo - Use this to get info on a dota team you're looking for\nE.G - !teaminfo EG, this will give the information on EG\n!playerinfo - Use this to get information on a player"
          willshelp5 = "!dtstreams / !dtstreams2 - This will collect the streams listed on the page of the tournaments being tracked for !nextdt / !nextdt2"

         
        return





    #All gardener commands  
    else:
      

        if(messagereceived=="!count" and str(message.author.id) =="183707605032501248"):
          count = len(client.guilds)
          count2 = len(client.users)

          await message.channel.send("I'am currently serving in - " + str(count) + " servers\nWith a total member count of - " + str(count2))
          




        if(messagereceived=="!translatehere"): 
          i=0
          try:
            for channel in message.guild.channels:
                if(sectionsofmessage[1][2:len(sectionsofmessage[1])-1] == str(channel.id)):
                  i=i+1
            
            
        
            
                  try:
                    
                    sec = sectionsofmessage[1][2:len(sectionsofmessage[1])-1]
                    channel = message.guild.get_channel(int(sec))

                    await message.channel.send("I have added this channel to automatically translate into - <#" + str(sec) + ">")
            
                    await channel.send("Channel selected for translation with - <#" + str(channelDataID) + ">")
                    datatosave = str(channelDataID) + ","
                    
                    datatosave2= str(sec) + ","

                    try:
                      data = download_file('/droptranslationchannels.txt', 'translationchannels.txt')
                      data2 = download_file('/droptranslationchannelstosendtoo.txt', 'translationchannelstosendtoo.txt')
                    except:
                      print("no files")

                    a_file = open("translationchannels.txt", "a")
                    a_file.writelines(datatosave)
                    a_file.close()

                    upload_file('/droptranslationchannels.txt', 'translationchannels.txt' )
                        


                    a_file = open("translationchannelstosendtoo.txt", "a")
                    a_file.writelines(datatosave2)
                    a_file.close()
                    upload_file('/droptranslationchannelstosendtoo.txt', 'translationchannelstosendtoo.txt' )

                  except:
                    i=i+1
                    
                    embed=discord.Embed(title="Error was hit initialising command", color=0xff8800)
                    embed.add_field(name="Use of command", value="The command is used by typing: !translatehere #ChannelOfChoice", inline=True)
                    embed.add_field(name="What can cause errors", value="Not adding the channel to the command\nThe bot not being able to see the channel chosen to send translated messages too\n\nFor support feel free to reach out on the support server - [Support Server](https://discord.gg/HzEhdZApP4)",inline=False)
                    await message.channel.send(embed=embed) 
            if(i==0):
              await message.channel.send("That channel is not in this server / available")
          except:
            embed=discord.Embed(title="Error was hit initialising command", color=0xff8800)
            embed.add_field(name="Use of command", value="The command is used by typing: !translatehere #ChannelOfChoice", inline=True)
            embed.add_field(name="What can cause errors", value="Not adding the channel to the command\nThe bot not being able to see the channel chosen to send translated messages too\n\nFor support feel free to reach out on the support server - [Support Server](https://discord.gg/HzEhdZApP4)",inline=False)
            await message.channel.send(embed=embed) 







        if (messagereceived =="!translationhelp" or messagereceived=="!help"):
          willshelp1 = "!translatehere - use this to set the translation tracking \nExample of use -\n!translatehere #ChannelHere"
          willshelp2 = "!deletetracking - use this to remove any tracking used on the channel that you're activating the command in"

          embed=discord.Embed(title="The commands I work with", color=0xff8800)
          embed.add_field(name="Add channel tracking for translation", value=willshelp1, inline=True)
          embed.add_field(name="Delete tracking of channel", value=willshelp2,inline=False)
          await message.channel.send(embed=embed) 






        if (messagereceived=="!deletetracking"):
          currentchannel = message.channel.id
          currentchannelstring = str(currentchannel)
          data = download_file('/droptranslationchannels.txt', 'translationchannels.txt')
          a_file = open("translationchannels.txt","r")
          datatester = a_file.read()
          value = datatester.rsplit(",")


          download_file('/droptranslationchannelstosendtoo.txt', 'translationchannelstosendtoo.txt')
          a_file2 = open("translationchannelstosendtoo.txt","r")
          datatester2 = a_file2.read()
          value2 = datatester2.rsplit(",")
          basechannels=""
          basetosend=""
          i=0
          j=0
          if(str(channelDataID) in value):
            while i < len(value):
              if(str(value[i]) == currentchannelstring):
                value.pop(i)
                value2.pop(i)
              i=i+1

          while j < len(value):
            basechannels = basechannels + str(value[j]) + ","
            basetosend= basetosend + str(value2[j]) + ","
            j=j+1
          
          f=open("translationchannels.txt","w")
          f.write(basechannels)
          f.close()

          f2=open("translationchannelstosendtoo.txt", "w")
          f2.write(basetosend)
          f2.close()

          upload_file('/droptranslationchannels.txt', 'translationchannels.txt' )
          upload_file('/droptranslationchannelstosendtoo.txt', 'translationchannelstosendtoo.txt' )

          await message.channel.send("Tracking for this channel has been removed")



client.run(os.getenv('TOKEN'))
server.server()