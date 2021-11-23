import discord
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "生气", "伤心"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

yun_shi = [
    "吉气冲天你最蒂！",
    "超级上吉",
    "上吉",
    "中吉",
    "小吉",
    "没胸",
    "小胸",
    "一般般的胸",
    "大胸",
    "胸太大你被压垮了",
    "哎呀呀，你最好还是不要知道呢"
]

with open('./feminism.txt') as f:
    fem = f.read().splitlines()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if 'hello' in msg.lower():
    await message.channel.send("Hello sis!")
    return

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
    return

  if msg.startswith('运势'):
    await message.channel.send(random.choice(yun_shi))
    return

  if msg.lower().startswith('come on'):
    await message.channel.send(random.choice(fem))



my_secret = "change this string to our token"
client.run(my_secret)
