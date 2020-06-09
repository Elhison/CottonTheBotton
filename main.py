#!/usr/bin/env python

import discord
import random
import datetime
import time
import os

from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix=commands.when_mentioned_or('69'))

status = cycle([' with your little sister', ' with your brother', ' with your mom',
                ' with myself', ' with my stepsister', ' with my step brother'])

print("Booting...")


@bot.event
async def on_ready():
    change_status.start()
    print(f'Logged in at {time.ctime()}')
    print('------')


@bot.event
async def on_member_join(member):

    channel = bot.get_channel(705295704251301899)
    guild = discord.utils.get(bot.guilds, name="Cotton's Nursery")
    role_id = discord.utils.get(guild.roles, name="Carbon-based life form")
    # Add more welcome stuff
    welcomes = (f'Bienvenue, {member.mention}! Amusez-vous bien! 😘',
                f'Bienvenu, {member.mention} ! Amusez-vous bien! 😘',
                f'Welcome, {member.mention}! Enjoy your stay. ☺️',
                f'Wilkommen, {member.mention}!',
                f'Välkommen, {member.mention}!',
                f'Tervetuloa, {member.mention}!',
                f'Bine ai venti, {member.mention}! Să te simți bine aici! 😜')

    print(f'{member} has joined.')
    await channel.send(random.choice(welcomes))
    await member.add_roles(role_id)


@bot.event
async def on_member_remove(member):
    # Add more farewells
    channel = bot.get_channel(713995293833822208)
    farewells = (f'Goodbye, {member.name}/{member.id}. We will miss you! :(',
                 f'Auf Wiedersehen, {member.name}/{member.id}. :(',
                 f'Farväl, {member.name}/{member.id}. :(',
                 f'Jäähyväiset, {member.name}/{member.id}. :(',
                 f'La revedere, {member.name}/{member.id}. O să te lipsim.')

    print(f'{member} has left.')
    await channel.send(random.choice(farewells))


@bot.event
async def on_message(message):
    bad_words = ('dumb', 'stupid', 'ugly')

    if message.content.startswith("69"):

        await message.channel.send("nice.")

    elif "hamburger" in message.content.lower():

        await message.channel.send("https://youtu.be/El1BhIQFMfs")

    elif "turtles" in message.content.lower() or "turtle" in message.content.lower():

        emoji = "\U0001F422"
        await message.add_reaction(emoji)

    elif message.content.startswith(f"turtles are {bad_words}"):

        await message.channel.send("no u")

    elif message.content.startswith("fuck you") or message.content.startswith("Fuck you"):

        await message.channel.send("No thanks :p")

    elif message.content.startswith("fuck") or message.content.startswith("Fuck"):

        await message.channel.send("you.")

    elif "shit" in message.content.lower():

        await message.add_reaction("\U0001F4A9")

    elif "linux" in message.content.lower():

        await message.channel.send("i use arch, btw")

    elif "bitch" in message.content.lower():

        await message.add_reaction("♀")
        await message.add_reaction("🐕")

    elif "motherfucker" in message.content.lower():

        await message.channel.send("I will fuck your mother too!")

    else:
        pass

    await bot.process_commands(message)


# @bot.event
# async def on_command_error(ctx, error):
#
#     await ctx.channel.purge(limit=1)
#
#     suggestion_channel = bot.get_channel(709728865467105281)
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("I don't know how to do that yet :/")
#         await ctx.send(f"If you have any suggestions, you can do so in the {suggestion_channel.mention} channel :p")

# Tasks!!!


# Tasks!!!


@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


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

    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# Commands!!!


# Commands!!!


@bot.command()
async def test(ctx):

    await ctx.send("How'd you discover this? :P")


@bot.command()
@commands.has_any_role('Big pp')
async def give_role(ctx, member: discord.Member, *, role_name):

    guild = discord.utils.get(bot.guilds, name="Cotton's Nursery")
    role_id = discord.utils.get(guild.roles, name=role_name)
    await ctx.channel.purge(limit=2)
    await ctx.send(f"Gave {member} a {role_id} role!")
    await member.add_roles(role_id)


@bot.command(aliases=['cuteimg'])
async def cute_image(ctx):

    file_names = ['dog0.jpg', 'dog1.jpg', 'dog2.jpg', 'dog3.jpg', 'dog4.jpg'
                 , 'dog5.jpg', 'dog6.jpg', 'dog7.jpg', 'dog8.jpg', 'dog9.jpg'
                 , 'dog10.jpg', 'dog11.jpg', 'dog12.jpg', 'dog13.jpg', 'dog14.jpg']
    rdm_file = random.choice(file_names)
    file = discord.File(f"./images/{rdm_file}", filename=rdm_file)
    embed = discord.Embed()
    embed.set_image(url=f"attachment://{rdm_file}")
    await ctx.channel.purge(limit=1)
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['cutevid'])
async def cute_video(ctx):

    file_names = ['dog0.mp4', 'dog1.mp4', 'dog2.mp4', 'dog3.mp4', 'dog4.mp4'
                  'cat0.mp4', 'cat1.mp4',
                  'seal0.mp4',
                  'squirrel0.mp4',
                  'turtle0.mp4']
    rdm_file = random.choice(file_names)
    file = discord.File(f"./videos/{rdm_file}", filename=rdm_file)
    await ctx.channel.purge(limit=1)
    await ctx.send(file=file)


# Embed-related commands!!!


# Embed-related commands!!!


@bot.command()
@commands.has_any_role('Big pp')
async def send_embed(ctx):

    await ctx.channel.purge(limit=1)

    embed = discord.Embed(title="Server Rules:", color=0x00fff9)
    embed.add_field(name="Rule #1",
                    value="You can joke about anything as long as you don't offend other people. If you do offend someone, apologize.",
                    inline=False)
    embed.add_field(name="Rule #2", value="NSFW content is allowed in the appropriate channels.", inline=False)
    embed.add_field(name="Rule #3",
                    value="Bestiality, child porn, torture, etc. are not allowed and will result in an immediate ban.",
                    inline=False)
    embed.add_field(name="Rule #4",
                    value="We are all equal and we accept everyone — regardless of race, gender, or sexuality.",
                    inline=False)
    embed.add_field(name="Rule #5",
                    value="You can only advertise your works (video, project, product, etc.) in the advertisement channel.",
                    inline=False)
    embed.add_field(name="Rule #6", value="Swearing is allowed as long as you don't offend anyone.", inline=False)
    embed.set_footer(text=f"Rules are bound to change. We will notify you.\nLast updated: {time.ctime()}")
    await ctx.send(embed=embed)


@bot.command()
async def first_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #1:", value="You can joke about anything as long as you don't offend other people."
                    " If you do offend someone, apologize.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@bot.command()
async def second_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #2", value="NSFW content is allowed in the appropriate channels.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@bot.command()
async def third_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #3",
                    value="Bestiality, child porn, torture, etc. are not allowed and will result in an immediate ban.",
                    inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@bot.command()
async def fourth_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #4",
                    value="We are all equal and we accept everyone — regardless of race, gender, or sexuality.",
                    inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@bot.command()
async def fifth_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #5", value="You can only advertise your works (video, project, product, etc.) in the advertisement channel.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@bot.command()
async def sixth_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #6", value="Swearing is allowed as long as you don't offend anyone.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@bot.command()
async def poll(ctx, *, message):
    embed = discord.Embed(color=0xffff00)
    channel = bot.get_channel(717715772268609589)
    emoji0 = '👍'
    emoji1 = '👎'
    turtle = "%B %d, %Y"
    embed.add_field(name=f"Poll created by {ctx.author} on {datetime.date.today().strftime(turtle)}", value=f"{message}")
    await ctx.channel.purge(limit=1)
    embed_id = await channel.send(embed=embed)
    await embed_id.add_reaction(emoji0)
    await embed_id.add_reaction(emoji1)


@bot.command()
async def user_info(ctx, member: discord.Member):

    embed = discord.Embed(title=" ")
    embed.add_field(name="Username", value=f"{member.name}", inline=True)
    embed.add_field(name="User ID", value=f"{member.id}", inline=True)
    embed.add_field(name="Join Date", value=f"{member.joined_at}", inline=True)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)








bot.run('NzEwMDYxMDAzNjY0MjYxMjAx.XtcNLA.bAsYY5ngS2OxpoHNrxJDRQHz3TY')
