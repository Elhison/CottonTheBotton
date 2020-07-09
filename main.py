#!/usr/bin/local/python

import discord
import random
import datetime
import time
import os

from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix=commands.when_mentioned_or('69'))
bot.remove_command('help')

status = cycle([' with your little sister', ' with your big brother', ' with your mom',
                ' with myself', ' with my stepsister', ' with my step brother', 'with you'])

print("Booting...")


@bot.event
async def on_ready():
    change_status.start()
    print(f'Logged in at {time.ctime()}')
    print('------')


@bot.event
async def on_member_join(member):

    # Add more welcome stuff
    welcomes = (f'Bienvenue, {member.mention}! Amusez-vous bien! 😘',
                f'Bienvenu, {member.mention} ! Amusez-vous bien! 😘',
                f'Welcome, {member.mention}! Enjoy your stay. ☺️',
                f'Wilkommen, {member.mention}!',
                f'Välkommen, {member.mention}!',
                f'Tervetuloa, {member.mention}!',
                f'Bine ai venti, {member.mention}! Să te simți bine aici! 😜',
                f'어서오세요, {member.mention}! 여기서 잘 지내세요. 😙',
                f'Benvenuto, {member.mention}. Goditi la permanenza nel gruppo',
                f'नमस्ते ,{member.mention}. मज़े करो!',
                f'Vitaj, {member.mention} Uži si pobyt.')

    guild = member.guild
    unverified_role = discord.utils.get(guild.roles, name="Unverified")
    channel = bot.get_channel(705295704251301899)
    rules_channel = bot.get_channel(705296662914138215)
    roles_list_channel = bot.get_channel(712521240052498444)
    bot_spam_channel = bot.get_channel(709669976390500422)
    print(f'{member} has joined.')

    embed = discord.Embed(title="Welcome to the server! uwu", description="| (• ◡•)|   (❍ᴥ❍ʋ)")
    embed.add_field(name="Please read the rules, master. Thank you :3", value=f"{rules_channel.mention}", inline=True)
    embed.add_field(name="Ask any of the Cardinals, the Pope, or Pyrocynical's Brother to give you the \"Carbon-based life form role.\"", value="I chose not to have an automatic verification system because it's vulnerable to bot raids. Thank you for your patience. ʕ•ᴥ•ʔ", inline=True)
    embed.add_field(name="When you get verified,", value=f"assign yourself some rules by typing `69role <role name>` in {bot_spam_channel.mention} (｡◕‿◕｡)", inline=True)
    await member.send(embed=embed)
    await member.add_roles(unverified_role)
    await channel.send(f"{random.choice(welcomes)}")


@bot.event
async def on_member_remove(member):
    # Add more farewells
    channel = bot.get_channel(713995293833822208)
    farewells = (f'Goodbye, {member}/{member.id}. We will miss you! :(',
                 f'Auf Wiedersehen, {member}/{member.id}. :(',
                 f'Farväl, {member}/{member.id}. :(',
                 f'Jäähyväiset, {member}/{member.id}. :(',
                 f'La revedere, {member}/{member.id}. O să te lipsim.',
                 f'잘 가세요, {member}. 우리는 당신이 그리울 거예요:(',
                 f'अलविदा {member}/{member.id}, हम आपको याद करेंगे',
                 f'Dovidenia {member}/{member.id} Budeš nám chýbať')

    print(f'{member} has left.')
    await channel.send(random.choice(farewells))


@bot.event
async def on_message(message):

    bad_words = ('dumb', 'stupid', 'ugly')
    if not message.author.bot:

        if message.content.startswith("69"):
            await message.channel.send("nice.")

        elif "hamburger" in message.content.lower():

            await message.channel.send("https://youtu.be/El1BhIQFMfs")

        elif message.content.startswith("Josh") or message.content.startswith("josh"):

            await message.channel.send("hi")

        elif "turtles" in message.content.lower() or "turtle" in message.content.lower():

            emoji = "\U0001F422"
            await message.add_reaction(emoji)

        elif message.content.startswith("fuck you") or message.content.startswith("Fuck you"):

            await message.channel.send("No thanks :p")

        elif message.content.startswith("fuck") and not message.content.startswith("fucking") or message.content.startswith("Fuck") and not message.content.startswith("Fucking") or message.content.startswith("FUCK") and not message.content.startswith("FUCKING"):

            await message.channel.send("you. :3")

        elif "shit" in message.content.lower():

            await message.add_reaction("\U0001F4A9")

        elif "linux" in message.content.lower():

            await message.channel.send("i use arch, btw")

        elif "bitch" in message.content.lower():

            await message.add_reaction("♀")
            await message.add_reaction("🐕")

        elif "motherfucker" in message.content.lower():

            await message.channel.send("I will fuck your mother too!")

        elif "rasengan" in message.content.lower():

            await message.channel.send("Chidori!")

        elif "chidori" in message.content.lower():

            await message.channel.send("Rasengan!")
        
        elif "bye" in message.content.lower() or "adios" in message.content.lower() or "goodbye" in message.content.lower():
            await message.channel.send("Goodbye! uwu")

        else:
            pass

    await bot.process_commands(message)

# Wtf. This piece of shit ruins..!

@bot.event
async def on_command_error(ctx, error):

    user_id = bot.get_user(354568022977019906)
    suggestion_channel = bot.get_channel(709728865467105281)

    await ctx.channel.purge(limit=1)

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("CommandNotFound error. I don't know how to do that yet :/")
        await ctx.send(f"If you have any suggestions, you can do so in the {suggestion_channel.mention} channel :p")
        await ctx.send(error)
        print(error)

    else:
        await ctx.send(error)
        print(error)
        


# Tasks!!!


# Tasks!!!


@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@tasks.loop(hours=1)
async def conversation_starter():
    random_item = ["turtles", "dogs", "hamsters", "cats",
                    "pie", "cheese", "you ;)"]
    await bot.send(f"I like {random.choice(random_item)}")

# Cogs!!!


# Cogs!!!


@bot.command()
@commands.has_any_role('Big pp')
async def load(ctx, extension):

    bot.load_extension(f'cogs.{extension}')


@bot.command()
@commands.has_any_role('Big pp')
async def unload(ctx, extension):

    bot.unload_extension(f'cogs.{extension}')


@bot.command()
@commands.has_any_role('Big pp')
async def reload(ctx, extension):

    await ctx.channel.purge(limit=1)
    
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f"{extension} cog reloaded!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def test(ctx):

    await ctx.send(bot.all_commands)

bot.run('NzEwMDYxMDAzNjY0MjYxMjAx.Xv0raw.AtFldn0QCjBu2KgRxz9-1YrLYe8')
