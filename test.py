@client.event
async def on_member_join(member):
    role = discord.utils.get(member.serveur.role, name = "Non Vérifié")
    await client.add_roles(member, role)

@client.event
async def on_raw_reraction_add(payload, member):
    message_id = payload.message.id
    if message_id == 703523838746427494:
            role_member = discord.utils.get(member.serveur.role, name = "Membre")
            await client.add_roles(member, role_member)
