import discord
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
from discord.ext import commands
import os

from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix="?")

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

bot.run("OTcxMTAyODY3MDI3MDIxODc0.GvQ8fV.EMJ2flUzYEyCjxYaogrdGgTJSXfGqN_LD3Gbl0")