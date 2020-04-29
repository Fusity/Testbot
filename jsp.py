import discord
from discord.ext import commands
TOKEN = "NjkyMzQxMzQwNzIxMjUwMzY2.XpYFmA.bMIPCiUjHwMhpiBjD6b34DmoPRE"
bot = commands.Bot(command_prefix = "./")


@bot.event
async def on_ready():
    print('Logged as ')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------') 

@bot.command(pass_context=True)
async def ping(ctx):
    print("Test!")


@bot.command(pass_context=True)
async def kick(ctx, member = discord.Member, *, reason=None):
    await member.kick(reason=reason)




bot.run(TOKEN)
