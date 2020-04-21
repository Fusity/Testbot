import discord
from discord.ext import commands
TOKEN = "NjkyMzQxMzQwNzIxMjUwMzY2.XpYFmA.bMIPCiUjHwMhpiBjD6b34DmoPRE"
bot = commands.Bot(command_prefix = "./")

#@bot.command
#async def join(pass_context=True):
    #script

@bot.event
async def on_ready():
    print('Logged as ')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------') 

@bot.command(pass_context=True)
async def join(ctx):
    chnl = ctx.message.author.voice
    ch = bot.get_channel(698510004336197632)
    await ch.connect()
    
@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild
    voix_bot = ctx.guild.voice_client
    await voix_bot.disconnect()

@bot.command(pass_context=True)
async def ping(ctx):
#    if message.content.startswith("./ideecmd"):
 #       athr = message.author
  #      msg = message.content.split(" ", 1)
   #     ch = bot.get_channel(692766179101507636)
    #   await ch.send('{} a eu une idée : " {} "'.format(athr, msg))
    print("Test")

@bot.event
async def on_message(message):
    athr = message.author
    msg = message.content
    chnl = message.channel
    ch = bot.get_channel(699698936709120082)
    if athr == bot.user:
        return
    await ch.send('{} envoyé par {} dans le salon {}'.format(msg, athr, chnl))

#bot.add_command(ideecmd)

bot.run(TOKEN)
'''Comment tu veux mettre ça Fizo ?
Perso j'aime bien mon code, pas toi ?
'''
