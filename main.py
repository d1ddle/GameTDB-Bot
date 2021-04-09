#Discord Bot Invite URL - https://discord.com/api/oauth2/authorize?client_id=824312967586906193&permissions=268815424&scope=bot

import discord
import os
import requests
import json
import keep_alive
import wget
from pathlib import Path
import time
from bs4 import BeautifulSoup
import math
import discord.utils 
import random
from threading import Thread
import asyncio

# to do:
# fix finding region for titles without images
# return "release World" (date), "ESRB rating", but bit hard since location in scraped array changes for every game
# add guild management and create a custom role with access to channels, read text etc.
# publicise and test bot via multiple servers

client = discord.Client()
keep_alive.keep_alive()
finished = 0
start = time.time()



@client.event
async def on_message(message):
  if message.author == client.user:
    return



def random_line(fname):
  random_lines = open(fname).read().splitlines()
  return random.choice(random_lines)



def same(my_file, my_file2): 
  with open(my_file, "rb") as one: 
    with open(my_file2, "rb") as two: 
      chunk = other = True 
      while chunk or other: 
        chunk = one.read(10000) 
        other = two.read(10000) 
        if chunk != other: 
          return False 
      return True 



directory = "./"

files_in_directory = os.listdir(directory)
filtered_files = [file for file in files_in_directory if file.endswith(".tmp")]

for file in filtered_files:
	os.remove(file)



with open('entries.json') as entries:
  data = json.load(entries)

wii = 0
ps3 = 1
ds = 2
switch = 3
threeds = 4
wiiu = 5
all = 6
index = 7

consoles = [wii, ps3, ds, switch, threeds, wiiu, index]

def update():
  for console in consoles:
    my_file = Path(data["databases"][console]["file"])
    my_file2 = Path(data["databases"][console]["file2"])
    

    if not my_file.exists():
      url = data["databases"][console]["url"]
      wget.download(url, data["databases"][console]["file"])


    if my_file2.exists():
      os.remove(data["databases"][console]["file2"])


    if my_file.exists():
      url = data["databases"][console]["url"]
      wget.download(url, data["databases"][console]["file2"])
      

      if same(my_file, my_file2) == False:
        os.remove(data["databases"][console]["file"])
        os.rename(data["databases"][console]["file2"], data["databases"][console]["file"])
        print("\n", data["databases"][console]["id"], "DB updated.")


      else:
        os.remove(data["databases"][console]["file2"])


  filenames = [data["databases"][0]["file"], data["databases"][1]["file"], data["databases"][2]["file"], data["databases"][3]["file"], data["databases"][4]["file"], data["databases"][5]["file"]]


  with open(data["databases"][6]["file"], 'w') as outfile:
    for names in filenames:
      with open(names) as infile:
        outfile.write(infile.read())
      outfile.write("\n")
  
  return

update()
#Suprised this works!!



# @client.event
# async def role(ctx, * role: discord.Role):
#   role = discord.utils.get(ctx.guild.roles, name = "GameTDB-Bot")
#   user = ctx.client.author
#   await user.add_roles(role)



# await channel.create_role(name="GameTDB-Bot", colour=discord.Colour(0x0026FF))
#   await channel.send("Role created.")
#   await client.add_roles(channel.author, "GameTDB-Bot")



@client.event
async def on_ready():
  print('\n\nLogged in as {0.user}'.format(client))



def search_string_in_file(gamename, gamePage, gameConsole):
  line_number = 0
  list_of_results = []
  total_line_number = 0
  
  with open(gameConsole) as read_obj:
    t0 = time.time()
    global line
    
    for line in read_obj:
        
      if gamename in line:
        total_line_number += 1
        line_number += 1

        gamePage = int(gamePage)
        
        if gamePage > 1:
          start_line = (gamePage * 10) - 9
          end_line = (gamePage * 10)

        elif gamePage == 1:
          start_line = gamePage
          end_line = gamePage * 10
        
        if line_number >= start_line and line_number <= end_line:
          list_of_results.append((line_number, line.rstrip()))

    global finished
    finished = 1
    t1 = time.time()

    global total
    total = t1 - t0

  return list_of_results, total_line_number

  return



@client.event
async def on_message(message):

  msg = message.content
  print(msg)

  if message.content.startswith('game'):
    gamearray = message.content.split(" ")
    # gamePage = 1

    if len(gamearray) == 1:
      e = discord.Embed(title = "Please provide a console and search term, idiot.", color = 0x277ae8)
      e.add_field(name = "Help", value = "Enter `gtdb` for help.")
      await message.channel.send(embed = e)

    else:
      with open('entries.json') as entries:
        data = json.load(entries)

      wii = 0
      ps3 = 1
      ds = 2
      switch = 3
      threeds = 4
      wiiu = 5
      all = 6
      index = 7

      console_check = ["wii", "ps3", "ds", "switch", "threeds", "wiiu", "index"]

      gameConsole = ""

      for console_line in console_check:
        if str(gamearray[1]) in console_check:
          gameConsole = gamearray[1]
          gamename = gamearray[2]

        elif str(gamearray[1]) not in console_check and gameConsole != data["databases"][6]["id"]:
            gameConsole = data["databases"][6]["id"]
            gamename = gamearray[1]

      gamename = gamename.replace("_", " ")
      gameConsole = gameConsole.lower()
      gameConsole += "tdb.txt"
    

    if len(gamearray) == 4:
      gamearray[3] = str(gamearray[3])
      if gamearray[3].isdigit():
        gamePage = int(gamearray[3])

    if len(gamearray) == 3:
      gamearray[2] = str(gamearray[2])
      if gamearray[2].isdigit():
        gamePage = int(gamearray[2])
      
      else:
        gamearray[2] = str(gamearray[2])
        gamePage = 1
    
    if len(gamearray) == 2:
      gamePage = 1

    matched_lines, total_line_number = search_string_in_file(gamename, gamePage, gameConsole)
    finished = 0

    if finished == 0:
      msg = ("Searching for '" + str(gamename) + "' in '" + str(gameConsole.replace('tdb.txt', '')) + "' and printing page '" + str(gamePage) + "'/'" + str(math.ceil(total_line_number / 10)) + "' of results.")
      e = discord.Embed(title = msg, color = 0x0026FF)
      await message.channel.send(embed = e)

    print('Total Matched lines : ', len(matched_lines))
    

    with open('entries.json') as entries:
      data = json.load(entries)


    for elem in matched_lines:
      linesplit = elem[1].split(" ")[0]

      if gameConsole == "alltdb.txt":

        with open("index.txt") as infile:
          for index_line in infile:
            if linesplit in index_line:
              print(index_line)
              game_url = index_line

      else:
        game_url = "https://www.gametdb.com/" + str(gameConsole.replace('tdb.txt', '')) + "/" + str(linesplit)

      print(game_url)

      headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        }


      response = requests.request("GET", game_url, headers=headers)
      data = BeautifulSoup(response.text, 'html.parser')

      images = data.find_all('img', src=True)
      print('Number of Images: ', len(images))

      desc = data.find_all('td', class_="notranslate", valign="top")
      print('Number of descriptions: ', len(desc))

      image_src = [x['src'] for x in images]
      
      image_src = [x for x in image_src if x.startswith('https') and linesplit in x]

      image_count = 1


      for image in image_src:
        print(image)

        data.desc_tags = data.find_all("td", class_="notranslate", valign="top")[4]
        text = data.desc_tags.get_text()

        if len(text) > 20:
          shortened = text[0:100] + "..."

        else:
          shortened = "No description"

        data.type = data.find_all("td", valign="top")[6]
        game_type = data.type.get_text()
        game_type = game_type[0:10]

        data.region = data.find_all("td", valign="top")[4]
        region_tag = data.region.get_text()

        data.reg_tag = data.find_all("span", style="font-size:83%;font-weight:bold;", class_="notranslate")[0]
        region = " (" + data.reg_tag.get_text() + ")"


        if "cover3d" in image:
          image_send = image

        elif "box" in image:
          image_send = image

        elif "cover" in image and not "coverfull" in image:
          image_send = image

        image_count = image_count+1


      if not image_src:
        data.desc_tags = data.find_all("td", class_="notranslate", valign="top")[4]

        text = data.desc_tags.get_text()
        shortened = text[0:100] + ""

        region = ""

        image_send = "https://www.gametdb.com/pub/skins/GameTDB-400.png"
        game_type = "No type"
        region_tag = "No region"


      ost_term = elem[1].split("=")[1].lower().replace(" ", "-")

      n = 1
      ost_term = ost_term[n:]

      ost_url = "https://downloads.khinsider.com/game-soundtracks/album/" + ost_term

      response2 = requests.request("GET", ost_url, headers=headers)
      soup = BeautifulSoup(response2.text, 'html.parser')
      if soup.h2.string == "Ooops!":
        print('Error')
        ost_url = "None"
      else:
        print('Album exists')
        ost_url = "[Khinsider](" + ost_url + ")"

      e = discord.Embed(title = elem[1] + region, description = shortened, url = game_url, color = 0x277ae8)
      e.set_thumbnail(url = image_send)
      e.add_field(name = game_type, value = region_tag)
      e.add_field(name = "Game OST", value = ost_url)

      await message.channel.send(embed = e)


      print('Line Number = ', elem[0], ' :: Line = ', elem[1])
      finished = 1


    if finished == 1:
      end = time.time()
      time_taken = (end - start)
      if time_taken > 10000:
        update()

      with open('entries.json') as entries:
        data = json.load(entries)

      line_count = 0
      with open(data["databases"][6]["file"]) as all_tdb:
        for line in all_tdb:
          
          line_count += 1


      if random_line('alltdb.txt') != None:
        linesplit2 = random_line('alltdb.txt').split("=")[1]
      else:
        linesplit2 = random_line('alltdb.txt')


      msg = ("Finished. Total of '" + str(line_count) + "' games.")
      e = discord.Embed(title = msg, color = 0x0026FF)
      await message.channel.send(embed = e)
      await client.change_presence(activity=discord.Game(name=linesplit2))
    

    if len(matched_lines) == 0:
      e = discord.Embed(title = "No results, check your casing.", color = 0x277ae8)
      e.add_field(name = "Help", value = "Enter `gtdb` for help.")
      await message.channel.send(embed = e)
  

  if message.content.startswith('gtdb' or 'GTDB'):
    desc = ("**Simply search for titles with a console term, search term and a results page number and the Bot will return a Title ID, Name, Cover Image, Description and link.** \n**New**: Search for multiple search terms by splitting them with underscores (_).\n**Double New**: Search without a console term. Don't provide one, and it'll search them all!\n**Triple New**:Now searches for Game OST's on Khinsider!")

    Use = "`game {console} {search term}_{second term} {results page no.}`\nMinimal:\n**`game {search term}`**\nIf a results page number isn't specified, page 1 will print.\nIf a console isn't specified, it'll search all. Please note that this is noticeably slower.\nBy the way, you can search for Title IDs too. Try RMCE01."

    Note = "If you can't see images, make sure your `Text and Image` settings are all set to On."

    Supported_consoles = "-[Wii - Nintendo Wii](https://www.gametdb.com/Wii)\n-[PS3 - Sony's PlayStation 3](https://www.gametdb.com/PS3)\n-[DS - Nintendo DS](https://www.gametdb.com/DS)\n-[Switch - Nintendo Switch](https://www.gametdb.com/Switch)\n-[3DS - Nintendo 3DS](https://www.gametdb.com/3DS)\n-[WiiU - Nintendo WiiU](https://www.gametdb.com/WiiU)"

    e = discord.Embed(title = "Hi, I'm d1ddle's GameTDB bot.", url = 'https://d1ddle.com',  description = desc, color = 0x0026FF)

    e.add_field(name = "Use", value = Use, inline = True)
    e.add_field(name = "Notes", value = Note, inline = False)
    e.add_field(name = "Supported Consoles", value = Supported_consoles, inline = False)
    e.add_field(name = "Credit", value = "Powered by the [Game Title DataBase](https://gametdb.com)\nAnd [Khinsider](https://downloads.khinsider.com/)\nView my [Replit repo](https://replit.com/@d1ddle/GamesTDB-Bot#main.py)\n[Invite Link](https://discord.com/api/oauth2/authorize?client_id=824312967586906193&permissions=268815424&scope=bot)")

    e.set_thumbnail(url = "https://avatars.githubusercontent.com/u/69437145?v=4")

    await message.channel.send(embed = e)



client.run(os.getenv('TOKEN'))  