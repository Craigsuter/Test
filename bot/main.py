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
    a_file = open("translationchannels.txt","r")
    datatester = a_file.read()
    value = datatester.rsplit(",")
    

    if(str(channelDataID) in value):
      print("This channel is translating!")
      location = value.index(str(channelDataID))

      a_file =open("translationchannelstosendtoo.txt", "r")
      datascan = a_file.read()
      values = datascan.rsplit(",")

      channeltosendtoo = values[int(location)]
      channel = message.guild.get_channel(int(channeltosendtoo))
      await channel.send("auto translation from - <#" + str(channelDataID) + ">")
    

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
              
              print("here")
              channel = message.guild.get_channel(int(sec))
              print("got here")
              await channel.send("Channel selected for translation with - <#" + str(channelDataID) + ">")
              datatosave = str(channelDataID) + ","
              
              datatosave2= str(sec) + ","

              a_file = open("translationchannels.txt", "a")
              a_file.writelines(datatosave)
              a_file.close()


              a_file = open("translationchannelstosendtoo.txt", "a")
              a_file.writelines(datatosave2)
              a_file.close()

            except:
              await message.channel.send("Error was hit with channel selected - this could be due to access")


          if (messagereceived =="!goosehelp"):
            willshelp1 = "!nextdota - This will tell you the next OG Dota 2 game coming up \n !nextcsgo - This will tell you the next OG CSGO game coming up \n !nextvalo - This will tell you the next OG Valorant  game coming up"
            willshelp2 = "!dotastreams / !dotastreams2 [B-streams if we're on there]- This will tell you the streams available for the next / current series of dota happening!\n !csgostreams - This will tell you the next / current CSGO games streams\n !valostreams - This will tell you the streams for the current / next Valorant series"
            willshelp3= "!nextdt - This will tell you the next game coming up in the currently tracked tournament\n\nAs a gardener you also gain access to commands found in: '!gardenerhelp'"
            willshelp4 = "!teaminfo - Use this to get info on a dota team you're looking for\nE.G - !teaminfo EG, this will give the information on EG\n!playerinfo - Use this to get information on a player"
            willshelp5 = "!dtstreams / !dtstreams2 - This will collect the streams listed on the page of the tournaments being tracked for !nextdt / !nextdt2"

            embed=discord.Embed(title="The commands I work with", color=0xff8800)
            embed.add_field(name="The next OG games", value=willshelp1, inline=True)
            embed.add_field(name="The streams for games", value=willshelp2, inline=False)
            embed.add_field(name="The streams for tournament tracked", value=willshelp5, inline=False)
            embed.add_field(name="Next game in tournament", value =willshelp3, inline=False)
            embed.add_field(name="Team / player info", value=willshelp4, inline=False)
            await message.channel.send(embed=embed) 


          if ((messagereceived =="!gardenerhelp")):
            GardenerHelp9 = "!verifydturl / !resetdt / !changedt\n\n!verifydturl - This will tell you the currently tournament link being tracked\n!resetdt - This will the currently tracked tournament\n!changedt - This will change the tournament being tracked to the URL provided"
            GardenerHelp4 = "!DotaBo1 / Bo3 / Bo5 \n \n !CSGOBo1 / Bo3 / Bo5 \n \n !ValoBo1 / Bo3 / Bo5 \n \n These will create the roles required to host a predictions game, purely type the one required, e.g - \n !CSGOBo3 \n \n"

            GardenerHelp5 = "!deleteDotaBo1 / Bo3 / Bo5 \n \n !deleteCSGOBo1 / Bo3 / Bo5 \n \n !deleteValoBo1 / Bo3 / Bo5 \n \n These will delete the roles that were made for the prediction game e.g - \n !deleteCSGOBo3 will delete the CSGOBo3 roles \n \n"

            GardenerHelp6 = "!avatar - You're able to see the avatars of any user / yourself, if you ping nobody it'll show your own avatar, if you ping someone it will show theirs\n\n!server_badge - This will get your the icon used for the server icon"

            GardenerHelp7 = "!dotastreams / !csgostreams / !valostreams - these will tell you the streams available for the next match of OG Dota / CSGO / Valorant respectively\n\n"

            GardenerHelp8 = "!copyover [channel to copy from here] - use this command to copy the content of a channel from 1 to another, the command will send the last 100 messages from a channel to the channel the command is being used in\n\nE.G of usage - !copyover 847832196294115349\nThis will give you the value from a copy test, the bot must be in both servers if copying from a different server"

            GardenerHelp10 = "!reminder - This command will let you set reminders for future you, the bot will remind you in the channel it is used in after a set amount of time! Use !reminder to find more information!\n!myreminders - This command will tell you your currently saved reminders and when they are going to be sent\n!deletereminder - This will allow for you to remove a reminder of your choice, choose the reminder you want to delete by checking for it on !myreminders and then using it for example like - !deletereminder 1\n!snooze - This will let you reset the reminder you received last, you will need to specify a new time the same way you did for !reminder, example !snooze 5m - will remind you again in 5 minutes"

            GardenerHelp11 = "!todolist - This will list the current to do list for the bot\n!addtodo - This will add to the todolist the test following the command\n!deletetodo - This will delete the 'todo' that is attached to the number chosen, find the to-do values using !todolist"
            
            embed=discord.Embed(title="The commands you get as a Gardener!", color=0xff8800)
            embed.add_field(name="Getting game streams",value=GardenerHelp7, inline=True)
            embed.add_field(name="Creating the roles for prediction games", value=GardenerHelp4, inline=False)
            embed.add_field(name="Delete the roles that were used for a prediction game", value=GardenerHelp5, inline=False)
            embed.add_field(name="Viewing avatars of users", value=GardenerHelp6, inline=False)
            embed.add_field(name="Tracking a tournament", value=GardenerHelp9, inline=False)
            embed.add_field(name="Reminders", value=GardenerHelp10, inline=False)
            embed.add_field(name="Copying data", value=GardenerHelp8, inline=False)
            embed.add_field(name="To-Do / suggestion list", value=GardenerHelp11, inline=False)
            await message.channel.send(embed=embed)


    
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