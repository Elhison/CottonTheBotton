import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(title="List of commands", description="")

        embed.add_field(name="affection", value="Sends an affectionate unicode face or emoji.", inline=True)

        embed.add_field(name="ban", value="**Don't abuse!**", inline=True)

        embed.add_field(name="battle/duel", value="Challenge someone to a fight!", inline=True)

        embed.add_field(name="covid", value="Sends information about Covid-19 cases.", inline=True)

        embed.add_field(name="discord *tos/privacy/cg*", value="Sends the terms of service, privacy policy, community "
                                                               "guidelines, or Wikipedia summary of Discord.",
                        inline=True)

        embed.add_field(name="eat_dog", value="🇨🇳", inline=True)

        embed.add_field(name="gay-o-meter `member`", value="Find out how gay someone is!", inline=True)

        embed.add_field(name="hamburger", value="CAN I HAVE SOME HAMBURGER PLS?!", inline=True)

        embed.add_field(name="invite", value="Sends a permanent invite link.", inline=True)

        embed.add_field(name="members_count", value="Send the total number of members (excluding bots).", inline=True)

        embed.add_field(name="pi", value="pi", inline=True)

        embed.add_field(name="ping", value="Sends the latency of CottonTheBotton", inline=True)

        embed.add_field(name="poll -poll message-", value="Create a poll!", inline=True)

        embed.add_field(name="randomnum -min number- -max number-", value="Sends a random number between and "
                                                                          "including the 1st and 2nd argument.",
                        inline=True)

        embed.add_field(name="r/ -subreddit name-", value="Sends a link to the specified subreddit.", inline=True)

        embed.add_field(name="reverse", value="Reverses a string.", inline=True)

        embed.add_field(name="role -role name-", value="Assigns yourself the specified role name.", inline=True)

        embed.add_field(name="send_roles", value="Sends a list of all possible roles.", inline=True)

        embed.add_field(name="send_rules", value="Sends the server's rules.", inline=True)

        embed.add_field(name="sort_alphabetically -words-", value="abcdefghijklmnopqrstuvwxyz in that order.", inline=True)

        embed.add_field(name="stock_price", value="r/wallstreetbets", inline=True)

        embed.add_field(name="user_info", value="For stalking someone.", inline=True)

        embed.add_field(name="whoami", value="Yeah, who **are** you?", inline=True)

        embed.add_field(name="wikipedia_scrapper", value="Why is your English teacher outside your house?", inline=True)

        embed.add_field(name="world_population", value="Use contraception, kids.", inline=True)

        # embed.add_field(name=" ", value=" ", inline=True)

        embed.add_field(name="Note:", value="Stuff enclosed with asterisks are optional.", inline=True)

        embed.add_field(name="WIP", value="WIP", inline=True)

        await ctx.author.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Help(bot))