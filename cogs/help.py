import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        # embed.add_field(name=" ", value=" ")

        embed = discord.Embed(title="List of commands", description="")

        embed.add_field(name="affection", value="Sends an affectionate unicode face or emoji.")

        embed.add_field(name="ban", value="**Don't abuse!**")

        embed.add_field(name="battle/duel", value="Challenge someone to a fight!")

        embed.add_field(name="covid", value="Sends information about Covid-19 cases.")

        embed.add_field(name="discord *tos/privacy/cg*", value="Sends the terms of service, privacy policy, community "
                                                               "guidelines, or Wikipedia summary of Discord.",
                )

        embed.add_field(name="eat_dog", value="🇨🇳")

        embed.add_field(name="gay-o-meter `member`", value="Find out how gay someone is!")

        embed.add_field(name="hamburger", value="CAN I HAVE SOME HAMBURGER PLS?!")

        embed.add_field(name="invite", value="Sends a permanent invite link.")

        embed.add_field(name="members_count", value="Send the total number of members (excluding bots).")

        embed.add_field(name="pi", value="pi")

        embed.add_field(name="ping", value="Sends the latency of CottonTheBotton")

        embed.add_field(name="poll -poll message-", value="Create a poll!")

        embed.add_field(name="randomnum -min number- -max number-", value="Sends a random number between and "
                                                                          "including the 1st and 2nd argument.",
                )

        embed.add_field(name="r/ -subreddit name-", value="Sends a link to the specified subreddit.")

        embed.add_field(name="reverse", value="Reverses a string.")

        embed.add_field(name="role -role name-", value="Assigns yourself the specified role name.")

        embed.add_field(name="send_roles", value="Sends a list of all possible roles.")

        embed.add_field(name="send_rules", value="Sends the server's rules.")

        embed.add_field(name="sort_alphabetically -words-", value="abcdefghijklmnopqrstuvwxyz in that order.")

        embed.add_field(name="stock_price", value="r/wallstreetbets")

        embed.add_field(name="user_info", value="For stalking someone.")

        embed.add_field(name="whoami", value="Yeah, who **are** you?")

        embed.add_field(name="wikipedia_scrapper", value="Why is your English teacher outside your house?")

        embed.add_field(name="world_population", value="Use contraception, kids.")

        embed.add_field(name="**Note:**", value="Stuff enclosed with asterisks are optional.")

        embed.add_field(name="WIP", value="WIP")

        await ctx.author.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Help(bot))