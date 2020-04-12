import discord
from discord.ext import commands
TOKEN = "NjkyMzQxMzQwNzIxMjUwMzY2.XpG1vg.kpA2gwBVhN8R7J8wQChDerPnWXA"
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

#bot.add_command(ideecmd)

bot.run(TOKEN)
'''Comment tu veux mettre ça Fizo ?
Perso j'aime bien mon code, pas toi ?
'''
