import discord
from discord.ext import commands
TOKEN = "NjkyMzQxMzQwNzIxMjUwMzY2.XpGE-Q.koXXbNKaBA8mCCj6iWtvtV6BkRo"
bot = commands.Bot(command_prefix = "./")

#@bot.command
#async def join(pass_context=True):
    #script

@bot.command
async def _ideecmd(message):
    athr = message.author
    chnl = bot.get_channel(692766179101507636)
    n = message.content
    await chnl.send('{} a eu une idée de commande : "{}"'.format(athr, cmd))
    
#bot.add_command(ideecmd)

bot.run(TOKEN)
