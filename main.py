#!/usr/bin/env python

import discord
import random

from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='69')
client.remove_command("help")

status = cycle([' with your little sister', ' with my stepsister',
                ' with your mom', ' with myself', ' with your brother', 'with my stepbrother'])

print("Booting...")


@client.event
async def on_ready():
    change_status.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):

    channel = client.get_channel(705295704251301899)
    guild = discord.utils.get(client.guilds, name="Cotton's Nursery")
    role_id = discord.utils.get(guild.roles, name="Carbon-based life form")
    # Add more welcome stuff
    welcomes = (f'Bienvenue, {member.mention} ! Amusez-vous bien!',
                f'Bienvenu, {member.mention} ! Amusez-vous bien!',
                f'Welcome, {member.mention}! Enjoy your stay. ☺️',
                f'Wilkommen, {member.mention}!',
                f'Välkommen, {member.mention}!',
                f'Tervetuloa, {member.mention}!')

    print(f'{member} has joined.')
    await channel.send(random.choice(welcomes))
    await member.add_roles(role_id)


@client.event
async def on_member_remove(member):
    # Add more farewells
    channel = client.get_channel(713995293833822208)
    farewells = (f'Goodbye, {member.mention}. We will miss you! :(',
                 f'Auf Wiedersehen, {member.mention}. :(',
                 f'Farväl, {member.mention}. :(',
                 f'Jäähyväiset, {member.mention}. :(')

    print(f'{member} has left.')
    await channel.send(random.choice(farewells))


@client.event
async def on_message(message):
    bad_words = ('dumb', 'stupid', 'ugly')

    if message.content.startswith("69"):
        await message.channel.send("nice.")

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
        await message.add_reaction("\U0000FE0F")
        await message.add_reaction("\U0001F415")

    elif "motherfucker" in message.content.lower():
        await message.channel.send("I will fuck your mother too!")

    else:
        pass

    await client.process_commands(message)


# Tasks!!!

# Tasks!!!


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# Commands!!!

# Commands!!!


@client.command()
async def whoami(ctx):
    await ctx.send(f'{ctx.author} / {ctx.author.mention} / {ctx.author.nickname}')


@client.command()
async def botping(ctx):
    await ctx.send(f'{client.latency * 1000}ms')


@client.command(aliases=['love'])
async def affection(ctx):
    hugs = ['༼ つ ◕_◕ ༽つ', '(づ｡◕‿‿◕｡)づ', '(づ￣ ³￣)づ', '༼ つ  ͡° ͜ʖ ͡° ༽つ', '😘',
            '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)', '♥‿♥', '😽', '😙', '😚', '\u2665', '\u2764']
    await ctx.channel.purge(limit=2)
    await ctx.send(random.choice(hugs))


@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    answer = ["Yes", "Of course", "Always",
              "Maybe", "Probably",
              "No", "Never", "In your dreams!"]
    await ctx.channel.purge(limit=1)
    if question == "":
        await ctx.send(f'Ask me a question. Lmaoooooo')
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answer)}')


@client.command(aliases=['randomnumber', 'rdmnum'])
async def random_number(ctx, num1: int, num2: int):
    value = str(random.randint(num1, num2)) + "\n"

    await ctx.channel.purge(limit=1)
    await ctx.send(value)


@client.command()
async def sort_alphabetically(ctx, *messages):
    print(type(messages))
    msgs = list(messages)
    print(type(sorted(msgs)))
    await ctx.channel.purge(limit=1)
    for entry in sorted(msgs):
        await ctx.send(entry)


@client.command()
async def reverse(ctx, *, message):
    msg = ctx.message.content
    message = msg[10:]
    await ctx.channel.purge(limit=1)
    await ctx.send(message[::-1])


@client.command()
async def ban(ctx, member: discord.Member):
    await ctx.channel.send(f'Banning {member.mention}...')


@client.command()
@commands.has_any_role('Big pp')
async def give_role(ctx, member: discord.Member, *, role_name):
    guild = discord.utils.get(client.guilds, name="Cotton's Nursery")
    role_id = discord.utils.get(guild.roles, name=role_name)
    await ctx.channel.purge(limit=2)
    await ctx.send(f"Gave {member} a {role_id} role!")
    await member.add_roles(role_id)


@client.command(aliases=['members'])
async def members_list(message):
    guild_id = client.get_guild(693377457243553873)
    await message.channel.purge(limit=2)
    await message.channel.send(f"There are {guild_id.member_count - 2} virgins on this server.")


@client.command()
async def sendimg(ctx):
    file_names = ['dog0.jpg', 'dog1.jpg', 'dog2.jpg', 'dog3.jpg', 'dog4.jpg'
                 , 'dog5.jpg', 'dog6.jpg', 'dog7.jpg', 'dog8.jpg', 'dog9.jpg'
                 , 'dog10.jpg', 'dog11.jpg', 'dog12.jpg', 'dog13.jpg', 'dog14.jpg']
    rdmfile = random.choice(file_names)
    file = discord.File(f"./images/{rdmfile}", filename=rdmfile)
    embed = discord.Embed()
    embed.set_image(url=f"attachment://{rdmfile}")
    await ctx.channel.purge(limit=2)
    await ctx.send(file=file, embed=embed)


@client.command()
async def invite(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send('https://discord.com/invite/QrZgbhk')


# Embed-related commands!!!

# Embed-related commands!!!


@client.command()
@commands.has_any_role('Big pp')
async def sendembed(ctx):
    embed = discord.Embed(title="Server Rules:", color=0x00fff9)
    embed.add_field(name="Rule #1", value="You can joke about anything as long as you don't offend other people. If you do offend someone, apologize.", inline=False)
    embed.add_field(name="Rule #2", value="NSFW content is allowed in the appropriate channels.", inline=False)
    embed.add_field(name="Rule #3", value="Bestiality, child porn, torture, etc. are not allowed and will result in an immediate ban.", inline=False)
    embed.add_field(name="Rule #4", value="We are all equal and we accept everyone — regardless of race, gender, or sexuality.", inline=False)
    embed.add_field(name="Rule #5", value="You can only advertise your works (video, project, product, etc.) in the advertisement channel.", inline=False)
    embed.add_field(name="Rule #6", value="Swearing is allowed as long as you don't offend anyone.", inline=False)
    embed.set_footer(text="Rules are bound to change. We will notify you.")
    await ctx.send(embed=embed)


@client.command()
async def first_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #1:", value="You can joke about anything as long as you don't offend other people."
                    " If you do offend someone, apologize.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@client.command()
async def second_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #2", value="NSFW content is allowed in the appropriate channels.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@client.command()
async def third_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #3",
                    value="Bestiality, child porn, torture, etc. are not allowed and will result in an immediate ban.",
                    inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@client.command()
async def fourth_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #4",
                    value="We are all equal and we accept everyone — regardless of race, gender, or sexuality.",
                    inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@client.command()
async def fifth_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #5", value="You can only advertise your works (video, project, product, etc.) in the advertisement channel.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


@client.command()
async def sixth_rule(ctx):
    embed = discord.Embed(title=" ", color=0x00fff9)
    embed.add_field(name="Rule #6", value="Swearing is allowed as long as you don't offend anyone.", inline=False)
    await ctx.channel.purge(limit=3)
    await ctx.send(embed=embed)


client.run('')
