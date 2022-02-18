import os
import discord
import random
import re
my_secret = os.environ['TOKEN']

client = discord.Client()
TOKEN = os.getenv('TOKEN')

def funnyMeme():
  memes = ['https://i.pinimg.com/564x/5b/fd/ff/5bfdff1a63946d1bf84ea3c1c78ad9a9.jpg', 'https://i.pinimg.com/236x/48/49/00/484900be868a5fa27210a69988af6965.jpg', 'https://i.pinimg.com/236x/f8/a7/d1/f8a7d1f5f2a3fff92a67d0d5c78ab8c1.jpg', 'https://i.pinimg.com/236x/0d/b9/5a/0db95a4ec22245449e0b34dcfbf2c26c.jpg', 'https://i.pinimg.com/236x/39/65/d1/3965d1cef4308e763cf5c5a2145eb38a.jpg', 'https://i.pinimg.com/236x/79/0f/f8/790ff82ceeb30bc6dd41f5809781ef7a.jpg', 'https://i.pinimg.com/564x/6b/43/eb/6b43eb2c9f549f725cf75d6990afe4ce.jpg','https://i.pinimg.com/236x/f7/54/70/f7547041d74f920773353891d62f4583.jpg','https://i.pinimg.com/236x/a3/dc/ee/a3dcee6061e6cbff18c261ad87b7ca27.jpg','https://i.pinimg.com/236x/00/e7/8d/00e78db38bc3db6d89b24afd31830d8b.jpg']
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

    if "maddy" in message.content:
        await message.channel.send("Thats me!!! :DD")
    keyWord = er_search(str(msg))
    if keyWord in message.content:
        await message.channel.send(keyWord + "!! I hardly know her!!!")
  

  

client.run(TOKEN)


  