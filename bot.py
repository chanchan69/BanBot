from discord.ext import commands

TOKEN = "your bot token"
BLACKLIST = open("blacklist.txt", "r").read().splitlines()

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_member_join(member):
    if [member.username == i for i in BLACKLIST]:
        member.ban(reason="blacklisted username / automatic")

bot.run(TOKEN)
