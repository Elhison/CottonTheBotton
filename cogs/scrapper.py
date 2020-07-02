import discord
import requests
import wikipedia

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
    async def discord(self, ctx, arg_shit=None):
        if arg_shit is None:
            await ctx.send("")
        
        elif arg_shit.lower() == "tos" or arg_shit.lower() == "termsofservice":
            await ctx.send("")


    @commands.command()
    async def wikipedia_scrapper(self, ctx, function):

        if function == "search":
            await ctx.send(wikipedia.search(function))

        elif function == "suggest":
            await ctx.send(wikipedia.suggest(function))

        elif function == "random":
            await ctx.send(wikipedia.random(5))

        elif function == "summary":
            await ctx.send(wikipedia.summary(function))
            
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


    @commands.command()
    async def stock_price(self, ctx, company_name):
        
        await ctx.channel.purge(limit=1)

        req = requests.get(f"https://money.cnn.com/quote/quote.html?symb={company_name}")
        source = req.content
        src = BeautifulSoup(source, 'html.parser')

        stock_price_broad = src.find(class_="wsod_last")
        stock_price = stock_price_broad.find("span")

        price_change = src.find(class_="posData")

        cmpny_name = src.find(class_="wsod_fLeft")

        last_updated_potato = src.find(class_="wsod_quoteLabelAsOf")
        last_updated_pot = last_updated_potato.get_text()
        last_updated = last_updated_pot[6:]

        embed = discord.Embed(title=f"{company_name} Stock Information", description = f"{cmpny_name.get_text()}", )
        embed.add_field(name=f"Stock price as of {last_updated}", value=f"${stock_price.get_text()}")
        embed.add_field(name=f"Today's change: ", value=f"{price_change.get_text()}")
        embed.set_footer(text="Stock data acquired from https://money.cnn.com (◕‿◕✿)")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Scrapper(bot))