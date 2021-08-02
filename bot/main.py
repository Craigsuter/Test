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
      await message.channel.send("Im up! Im up! Are you okay... cool... co... <:OGmonkaThink:821509791523930162> ")


    
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
      print("This channel is translating!")
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
        

        if (messagereceived =="!goosehelp"):
          willshelp1 = "!nextdota - This will tell you the next OG Dota 2 game coming up \n!nextcsgo - This will tell you the next OG CSGO game coming up \n!nextvalo - This will tell you the next OG Valorant  game coming up \n \n"

          willshelp2 = "!dotastreams / !dotastreams2 [B-Streams listed for our team] - This will tell you the streams available for the next / current series of dota happening!\n!csgostreams - This will tell you the next / current CSGO games streams\n!valostreams - This will tell you the streams for the current / next Valorant series"
          willshelp3= "!nextdt - This will tell you the next game coming up in the currently tracked tournament"
          willshelp4 = "!teaminfo - Use this to get info on a dota team you're looking for\nE.G - !teaminfo EG, this will give the information on EG\n!playerinfo - Use this to get information on a player"
          willshelp5 = "!dtstreams / !dtstreams2 - This will collect the streams listed on the page of the tournaments being tracked for !nextdt / !nextdt2"

          embed=discord.Embed(title="The commands I work with", color=0xff8800)
          embed.add_field(name="The next OG games", value=willshelp1, inline=True)
          embed.add_field(name="The streams for games", value=willshelp2, inline=False)
          embed.add_field(name="The streams for tournament tracked", value=willshelp5, inline=False)
          embed.add_field(name="Next game in tournament", value =willshelp3, inline=False)
          embed.add_field(name="Team / player info", value=willshelp4, inline=False)
          await message.channel.send(embed=embed) 

        return













    #All gardener commands  
    else:
        if(messagereceived=="!translatehere"): 
          
          print(message.content)
          print(sectionsofmessage[1])
          sec = sectionsofmessage[1][2:len(sectionsofmessage[1])-1]
          print(sec)
          try:
            

            channel = message.guild.get_channel(int(sec))

            await message.channel.send("I have added this channel to automatically translate into - <#" + str(message.channel.id) + ">")
     
            await channel.send("Channel selected for translation with - <#" + str(channelDataID) + ">")
            datatosave = str(channelDataID) + ","
            
            datatosave2= str(sec) + ","

            a_file = open("translationchannels.txt", "a")
            a_file.writelines(datatosave)
            a_file.close()

            upload_file('/droptranslationchannels.txt', 'translationchannels.txt' )
                


            a_file = open("translationchannelstosendtoo.txt", "a")
            a_file.writelines(datatosave2)
            a_file.close()
            upload_file('/droptranslationchannelstosendtoo.txt', 'translationchannelstosendtoo.txt' )

          except:
            await message.channel.send("Error was hit with channel selected - this could be due to access")





        if (messagereceived =="!translationhelp"):
          willshelp1 = "!translatehere - use this to set the translation tracking \nExample of use -\n!translatehere #ChannelHere"

          embed=discord.Embed(title="The commands I work with", color=0xff8800)
          embed.add_field(name="Add channel tracking for translation", value=willshelp1, inline=True)
          await message.channel.send(embed=embed) 


        if (messagereceived=="!deletetracking"):
          currentchannel = message.channel.id
          currentchannelstring = str(currentchannel)
          data = download_file('/droptranslationchannels.txt', 'translationchannels.txt')
          a_file = open("translationchannels.txt","r")
          datatester = a_file.read()
          value = datatester.rsplit(",")


          data2 = download_file('/droptranslationchannelstosendtoo.txt', 'translationchannelstosendtoo.txt')
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

          await message.channel.send("Trackign for this channel has been removed")


          







              



       

    
    #Rus translation - N0tail Discord
    if(channelDataID == 808362012849340416):
      channel = message.guild.get_channel(834445890235138133)
      msgID = message.jump_url
      author = message.author
      data = translations(nexttrans, author, msgID)
      #Getting translation data
      embed=data
      await channel.send(embed=embed)



client.run(os.getenv('TOKEN'))
server.server()