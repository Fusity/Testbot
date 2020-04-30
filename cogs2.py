import discord
from discord.ext import commands

class infos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(pass_context=True)
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        with open("users.json", "r") as f:
            users = json.load(f)

            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
            embed.set_author(name=f"{member}", icon_url=member.avatar_url)
            embed.add_field(name="Niveau", value=users[member_id]["level"])
            embed.add_field(name="Money", value=users[member_id]["money"])
            embed.add_field(name="XP", value=users[member_id]["experience"])
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def rank(self, ctx):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
            lb = []
            z = 0
            for member in ctx.message.guild.members:
                if str(member.id) in users:
                    lb.append([users[str(member.id)].get('experience', 0), member.id])

            for i in sorted(lb, reverse=True):
                z += 1
                if z == 4:
                    break

                embed = discord.Embed(color=bot.get_user(i[1]).color, timestamp=ctx.message.created_at)
                embed.set_author(name=f"{bot.get_user(i[1])}", icon_url=bot.get_user(i[1]).avatar_url)
                embed.add_field(name="Niveau", value=users[str(i[1])]["level"])
                embed.add_field(name="Money", value=users[str(i[1])]["money"])
                embed.add_field(name="XP", value=users[str(i[1])]["experience"])
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(infos(bot))   