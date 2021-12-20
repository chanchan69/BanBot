import discord
from discord.ext import commands

TOKEN = ""
BLACKLIST = open("blacklist.txt", "r").read().splitlines()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_member_join(member):
    print(member.display_name + " was banned")
    if [member.display_name == i for i in BLACKLIST]:
        await member.ban(reason="blacklisted username / automatic")

bot.run(TOKEN)
