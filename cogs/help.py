import discord
from discord.ext import commands

class Help(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def help(self, ctx):
        embed=discord.Embed(title="List of commands", description="")

def setup(bot):
    bot.add_cog(Help(bot))