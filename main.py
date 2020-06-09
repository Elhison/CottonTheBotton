#!/usr/bin/env python

import discord
import random
import datetime
import time

from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix=commands.when_mentioned_or('69'))
client.remove_command("help")

status = cycle([' with your little sister', ' with your brother', ' with your mom',
                ' with myself', ' with my stepsister', ' with my step brother'])

print("Booting...")


@client.event
async def on_ready():
    change_status.start()
    print(f'Logged in at {time.ctime()}')
    print('------')


@client.event
async def on_member_join(member):

    channel = client.get_channel(705295704251301899)
    guild = discord.utils.get(client.guilds, name="Cotton's Nursery")
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


@client.event
async def on_member_remove(member):
    # Add more farewells
    channel = client.get_channel(713995293833822208)
    farewells = (f'Goodbye, {member.name}/{member.id}. We will miss you! :(',
                 f'Auf Wiedersehen, {member.name}/{member.id}. :(',
                 f'Farväl, {member.name}/{member.id}. :(',
                 f'Jäähyväiset, {member.name}/{member.id}. :(',
                 f'La revedere, {member.name}/{member.id}. O să te lipsim.')

    print(f'{member} has left.')
    await channel.send(random.choice(farewells))


@client.event
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

    await client.process_commands(message)


@client.event
async def on_command_error(ctx, error):

    await ctx.channel.purge(limit=1)

    suggestion_channel = client.get_channel(709728865467105281)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I don't know how to do that yet :/")
        await ctx.send(f"If you have any suggestions, you can do so in the {suggestion_channel.mention} channel :p")

# Tasks!!!


# Tasks!!!


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# Commands!!!


# Commands!!!


@client.command()
async def test(ctx):

    await ctx.channel.purge(limit=2)
    while True:
        msg = input("Enter message to send: ")
        if msg == "|":
            break
        await ctx.send(msg)

@client.command()
async def whoami(ctx):
    await ctx.send(f'{ctx.author} / {ctx.author.mention} / {ctx.author.nickname}')


@client.command()
async def bot_ping(ctx):
    await ctx.send(f'{client.latency * 1000}ms')


@client.command(aliases=['love'])
async def affection(ctx):
    hugs = ['༼ つ ◕_◕ ༽つ', '(づ｡◕‿‿◕｡)づ', '(づ￣ ³￣)づ', '༼ つ  ͡° ͜ʖ ͡° ༽つ', '😘',
            '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)', '♥‿♥', '😽', '😙', '😚', '\u2665', '\u2764']
    await ctx.channel.purge(limit=2)
    await ctx.send(random.choice(hugs))


@client.command(aliases=['8ball'])
async def eight_ball(ctx, *, question):

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
async def sort_alphabetically_error(ctx, error):

    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You forgot to tell me the words you want to sort alphabetically. -,-")


@client.command()
async def reverse(ctx, *, message):

    await ctx.channel.purge(limit=1)
    msg = ctx.message.content
    message = msg[10:]
    await ctx.send(message[::-1])


@reverse.error
async def reverse_error(ctx, error):

    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You forgot to tell me what word you want to reverse. -,-")


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


@client.command()
async def role(ctx, *, role_name):

    guild = discord.utils.get(client.guilds, name="Cotton's Nursery")
    role_id = discord.utils.get(guild.roles, name=role_name)
    await ctx.channel.purge(limit=1)
    if role_name == "Cardinal" or role_name == "Cardinal" or role_name == "Small pp" or role_name == "Big pp" or role_name == "Pope" or role_name == "Stik" or role_name == "God" or role_name == "Jesus Christ":
        ctx.send("Not allowed!")
    else:
        await ctx.send(f"Gave {ctx.author} a {role_id} role!")
        await ctx.author.add_roles(role_id)



@client.command(aliases=['members'])
async def members_count(message):

    guild_id = client.get_guild(693377457243553873)
    await message.channel.purge(limit=2)
    await message.channel.send(f"There are {guild_id.member_count - 4} virgins on this server.")


@client.command(aliases=['cuteimg'])
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


@client.command(aliases=['cutevid'])
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


@client.command()
@commands.has_any_role('Big pp')
async def ping_multiple(ctx, member: discord.Member, loops):

    await ctx.channel.purge(limit=1)

    loopz = int(loops)
    num = 0
    while num < loopz+1:

        await ctx.send({member.mention})
        loopz += 1


@client.command()
async def invite(ctx):

    await ctx.channel.purge(limit=1)
    await ctx.send('https://discord.com/invite/QrZgbhk')


@client.command()
async def eat_dog(ctx):

    await ctx.send("https://www.youtube.com/watch?v=CgHVNA8olaE")

# Embed-related commands!!!


# Embed-related commands!!!


@client.command()
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

@client.command()
async def poll(ctx, *, message):
    embed = discord.Embed(color=0xffff00)
    channel = client.get_channel(717715772268609589)
    emoji0 = '👍'
    emoji1 = '👎'
    turtle = "%B %d, %Y"
    embed.add_field(name=f"Poll created by {ctx.author} on {datetime.date.today().strftime(turtle)}", value=f"{message}")
    await ctx.channel.purge(limit=1)
    embed_id = await channel.send(embed=embed)
    await embed_id.add_reaction(emoji0)
    await embed_id.add_reaction(emoji1)


@client.command()
async def user_info(ctx, member: discord.Member):

    embed = discord.Embed(title=" ")
    embed.add_field(name="Username", value=f"{member.name}", inline=True)
    embed.add_field(name="User ID", value=f"{member.id}", inline=True)
    embed.add_field(name="Join Date", value=f"{member.joined_at}", inline=True)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@client.command()
async def hamburger(ctx):

    await ctx.channel.purge(limit=1)
    await ctx.send("https://youtu.be/El1BhIQFMfs")
    await ctx.send("hambuga chesbuga begmac whapa")


client.run('NzEwMDYxMDAzNjY0MjYxMjAx.XtcNLA.bAsYY5ngS2OxpoHNrxJDRQHz3TY')
