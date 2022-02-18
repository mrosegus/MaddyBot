import os
import discord
import random
import re
my_secret = os.environ['TOKEN']

client = discord.Client()
TOKEN = os.getenv('TOKEN')
i = 0
with open('memes.txt', 'r') as f:
    set_of_links = [re.sub(r'[(\[\],)]', '', x) for x in f.read().split()]
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


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    

    if msg.startswith('$3am'):
        await message.channel.send(funnyMeme())

    elif "maddy" in message.content:
        await message.channel.send("Thats me!!! :DD")
    keyWord = er_search(str(msg))
    if keyWord in message.content:
        await message.channel.send(keyWord + "!! I hardly know her!!!")
  

  

client.run(TOKEN)


  