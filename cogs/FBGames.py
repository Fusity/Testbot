import discord
from discord.ext import commands

class FBGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect(reconnect=True)

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        voiceBot = ctx.guild.voice_client
        await voiceBot.disconnect()

    @commands.command(pass_context=True)
    async def tts(self, ctx):
        finalMessage = ctx.message.content.replace('./tts', '')
        await ctx.send(finalMessage, tts=True)

   
def setup(bot):
    bot.add_cog(FBGames(bot))