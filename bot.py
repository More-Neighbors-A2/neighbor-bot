import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.channel.name != "introductions":
        return

    all_roles = message.guild.roles
    author = message.author
    if get_role(author.roles, "Member"):
        return

    lurker = get_role(all_roles, "Lurkers")
    member = get_role(all_roles, "Member")
    await author.add_roles(member)
    await author.remove_roles(lurker)


def get_role(roles, name):
    return next((role for role in roles if role.name == name), None)


client.run(os.getenv("DISCORD_TOKEN"))
