import os
import json
import time
from discord.ext import commands
from dotenv import load_dotenv
import random
from math import floor
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX')

bot = commands.Bot(command_prefix=PREFIX)

##############################################################################################################
#Ne pas oublier de mettre les extension ici \/\/
extensions = ['cogs.FBGames', 'cogs.infos']

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    with open('users.json', 'r') as json_file:
        users = json.load(json_file)
        if not users:
            await user_insert(users, message.author)
            with open("users.json", "w") as f:
                json.dump(users, f)
            await message.channel.send("You are now in the list you can level up (write some message to lvl up)")
        try:
            print (users[str(message.author.id)])
        except:
            await user_insert(users, message.author)
            with open("users.json", "w") as f:
                json.dump(users, f)
            await message.channel.send("You are now in the list you can level up (write some message to lvl up)")

        if time.time() - users[str(message.author.id)]["last_message"] > 5:
            number = random.randint(1, 5)
            await add_experience(users, message.author, number)
            await add_money(users, message.author)
            await level_up(users, message.author, message.channel)
            with open("users.json", 'w') as f:
                json.dump(users, f)
    await bot.process_commands(message)

async def user_insert(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1
        users[user.id]["last_message"] = time.time()
        users[user.id]["money"] = 0

async def add_experience(users, user, number):
    experience = floor(9.5 + number + (users[str(user.id)]['level'] - 2))
    users[str(user.id)]["experience"] += experience
    users[str(user.id)]["last_message"] = time.time()

async def add_money(users, user):
    money = floor((9.5 + users[str(user.id)]['level'] + 50.75 + (users[str(user.id)]['level'] - 2) / 4 * 2 * ((users[str(user.id)]['level']) % 4) + 1 + (users[str(user.id)]['level'] - 6) / 4 * 2) / 18)
    users[str(user.id)]["money"] += money

async def level_up(users, user, channel):
    experience = users[str(user.id)]["experience"]
    current_level = users[str(user.id)]["level"]
    next_level = int(experience ** (1 / 4))

    if current_level < next_level:
        await channel.send(f":tada: {user.mention}, tu as atteint le niveau {next_level} !")
        users[str(user.id)]["level"] = next_level

        
@bot.command()
async def load(extension):
    try:
        chnl = bot.get_channel(702017626011861012)
        bot.load_extension(extension)
        await chnl.send('Loaded {}'.format(extension))
    except Exception as error:
        chnl = bot.get_channel(702017626011861012)
        await chnl.send('{} cannot be loaded. [{}]'.format(extension, error))

@bot.command()
async def unload(extension):
    try:
        chnl = bot.get_channel(702017626011861012)
        bot.unload_extension(extension)
        await chnl.send('Unloaded {}'.format(extension))
    except Exception as error:
        chnl = bot.get_channel(702017626011861012)
        await chnl.send('{} cannot be unloaded. [{}]'.format(extension, error))



if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension, error))
    bot.run(TOKEN)
