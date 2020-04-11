import os
import json
import time
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author == client.user:
        return

    with open('users.json', 'r') as json_file:
        users = json.load(json_file)
        if not users:
            await user_insert(users, message.author)
            with open("users.json", "w") as f:
                json.dump(users, f)
            return await message.channel.send("You are now in the list you can level up (write some message to lvl up)")
        try:
            print (users[str(message.author.id)])
        except:
            await user_insert(users, message.author)
            with open("users.json", "w") as f:
                json.dump(users, f)
            return await message.channel.send("You are now in the list you can level up (write some message to lvl up)")

        number = random.randint(5, 20)
        await add_experience(users, message.author, number)
        await add_money(users, message.author, number)
        await level_up(users, message.author, message.channel)
        with open("users.json", 'w') as f:
            json.dump(users, f)

async def user_insert(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1
        users[user.id]["last_message"] = time.time()
        users[user.id]["money"] = 0

async def add_experience(users, user, number):
    users[str(user.id)]["experience"] += number
    users[str(user.id)]["last_message"] = time.time()

async def add_money(users, user, number):
    users[str(user.id)]["money"] += number

async def level_up(users, user, channel):
    experience = users[str(user.id)]["experience"]
    current_level = users[str(user.id)]["level"]
    next_level = int(experience ** (2 / 6))

    if current_level < next_level:
        await channel.send(f":tada: {user.mention}, tu as atteint le niveau {next_level} !")
        users[str(user.id)]["level"] = next_level

client.run(TOKEN)