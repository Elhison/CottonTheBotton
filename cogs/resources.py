import discord
import datetime
from discord.ext import commands

class Resources(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def send_resources_list(self, ctx):
        embed_gen=discord.Embed(title="A Curated List of High-Quality Resources", description=f"Last updated on {time.ctime()} UTC+8.", color=0xff000d)
        embed_gen.add_field(name="Khanacademy", value="https://www.khanacademy.org", inline=False)
        embed_gen.add_field(name="Britannica", value="https://www.britannica.com/", inline=False)
        embed_gen.add_field(name="HowStuffWorks", value="https://www.howstuffworks.com/", inline=False)
        embed_gen.add_field(name="ThoughtCo", value="https://www.thoughtco.com/", inline=False)
        embed_gen.add_field(name="Wikipedia", value="https://en.wikipedia.org/", inline=False)
        embed_gen.add_field(name="Live Science", value="https://www.livescience.com/", inline=False)
        embed_gen.add_field(name="WIP", value="WIP", inline=False)
        await ctx.send(embed=embed_gen)

def setup(bot):
    bot.add_cog(Resources(bot))
