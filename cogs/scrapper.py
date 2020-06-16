import discord
import requests

from discord.ext import commands
from bs4 import BeautifulSoup


class Scrapper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def covid(self, ctx):

        result = requests.get("https://virusncov.com/")
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')
        total_cases = soup.find(class_="first-count")
        death_cases = soup.find(class_="red-text")
        recovery_cases = soup.find(class_="green-text")

        embed = discord.Embed(title="Covid-19 cases: ", color=0xff0000)
        embed.add_field(name="Total Cases:", value=f"{total_cases.get_text()}",
                        inline=False)
        embed.add_field(name="Deaths:", value=f"Total number of deaths: {death_cases.get_text()}",
                        inline=False)
        embed.add_field(name="Recovered:", value=f"Total number of recoveries: {recovery_cases.get_text()}",
                        inline=False)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    @commands.command()
    async def world_population(self, ctx):

        result = requests.get("https://countrymeters.info/en/World")
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')
        total_population = soup.find(id="cp1")
        embed = discord.Embed(title="World population", description="Make more babies! :3")
        embed.add_field(name=f"World Population:", value=f"{total_population.get_text()}")

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Scrapper(bot))