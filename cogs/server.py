import discord
from discord.ext import commands


class Server(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):

        await ctx.send(f'{self.bot.latency * 1000}ms')

    @commands.command()
    async def invite(self, ctx):

        await ctx.channel.purge(limit=1)
        await ctx.send('https://discord.com/invite/QrZgbhk')


    @commands.command()
    async def members_count(self, message):

        guild_id = self.bot.get_guild(693377457243553873)

        await message.channel.purge(limit=2)
        await message.channel.send(f"There are {guild_id.member_count - 4} virgins on this server.")

def setup(bot):
    bot.add_cog(Server(bot))
