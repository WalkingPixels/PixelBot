import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
```
General Commands:
?help - well you know what this command is
?p - Play Music
?q - Displays the current music queue
?skip - Skips current playing song
?clear - Clears the queue and stops bot from playing
?leave - Disconnect the bot from the voice channel
?pause - Pauses the current song playing
?resume - Resumes the current playing song
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)       

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
