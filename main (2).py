import os
from keep_alive import keep_alive
import discord
import random
import re
my_secret = os.environ['TOKEN']
from discord.ext import commands
bot = commands.Bot(command_prefix="$")

TOKEN = os.getenv('TOKEN')
i = 0
with open('memes.txt', 'r') as f:
    set_of_links = [re.sub(r'[(\[\],)]', '', x) for x in f.read().split()]


with open('hswords.txt', 'r') as f2:
    #homestuck = [line.strip() for line in f2]
    homestuck = [re.sub(r'[(\[\],)]', " ", x) for x in f2.read().split()]
 
def funnyMeme():
  memes = set_of_links
  r1 = random.randint(0, len(memes))
  imageLink = memes[r1] 
  return imageLink

def er_search(messageFromUser):
  p = re.compile(r'\w*er\b')
  word = p.findall(messageFromUser)
  returnWord = word[0]
  return returnWord



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot)) 
@bot.event
async def on_message(message):
  
  if message.author == bot.user:
      return
  for i in homestuck:
    if i in message.content:
      await message.channel.send(f"{(message.author.mention)} is *that* a Homestuck reference??!  :eyes:")
      return

  if "maddy" in message.content:
        await message.channel.send("Thats me!!! :DD")
        return
  if "rice a roni" in message.content:
        await message.channel.send("I do not smell like Rice-A-Roni!!! >:((")
        return 
  keyWord = er_search(str(message.content))
  if keyWord in message.content:
        await message.channel.send(keyWord + "?! I hardly know her!!!")
        return  
     	# INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS. 
  await bot.process_commands(message)

@bot.command
async def hello(ctx):
  await ctx.send(ctx.author.mention + " hello!")

keep_alive()
bot.run(TOKEN)


  