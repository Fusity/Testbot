import discord
from discord.ext import commands

TOKEN = 'NjkyMzQxMzQwNzIxMjUwMzY2.XpYFmA.bMIPCiUjHwMhpiBjD6b34DmoPRE'
client = commands.Bot(command_prefix='.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "Allez dans la catégorie à gauche (Règlement)")
    await member.add_roles(role)

@client.event
async def on_raw_reaction_add(payload, member):
    message_id = payload.message.id
    if message_id == 694904107596775475:
            role_member = discord.utils.get(member.guild.roles, name = "Membre Vérifié")
            await member.add_roles(member, role_member)

client.run(TOKEN)