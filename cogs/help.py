import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        embed=discord.Embed(title="List of commands", description="")

        embed.add_field(name="test", value="test", inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def list_commands(self, ctx):

        await ctx.channel.purge(limit=1)
        await ctx.send(bot.commands)

def setup(bot):
    bot.add_cog(Help(bot))