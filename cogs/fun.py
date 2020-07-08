import discord
import random

from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member: discord.Member):

        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f'Banning {member.mention}...')

    @commands.command(aliases=['cuteimg'])
    async def cute_image(self, ctx):

        file_names = ['dog0.jpg', 'dog1.jpg', 'dog2.jpg', 'dog3.jpg', 'dog4.jpg',
                      'dog5.jpg', 'dog6.jpg', 'dog7.jpg', 'dog8.jpg', 'dog9.jpg',
                      'dog10.jpg', 'dog11.jpg', 'dog12.jpg', 'dog13.jpg', 'dog14.jpg']

        rdm_file = random.choice(file_names)
        file = discord.File(f"./images/{rdm_file}", filename=rdm_file)
        embed = discord.Embed()
        embed.set_image(url=f"attachment://{rdm_file}")

        await ctx.channel.purge(limit=1)
        await ctx.send(file=file, embed=embed)

    @commands.command(aliases=['cutevid'])
    async def cute_video(self, ctx):

        file_names = ['dog0.mp4', 'dog1.mp4', 'dog2.mp4', 'dog3.mp4', 'dog4.mp4'
                                                                      'cat0.mp4', 'cat1.mp4',
                      'seal0.mp4',
                      'squirrel0.mp4',
                      'turtle0.mp4']
        rdm_file = random.choice(file_names)
        file = discord.File(f"./videos/{rdm_file}", filename=rdm_file)
        await ctx.channel.purge(limit=1)
        await ctx.send(file=file)

    @commands.command()
    async def eat_dog(self, ctx):

        await ctx.channel.purge(limit=1)
        await ctx.send("https://www.youtube.com/watch?v=CgHVNA8olaE")

    @commands.command()
    async def hamburger(self, ctx):

        await ctx.channel.purge(limit=1)
        await ctx.send("https://youtu.be/El1BhIQFMfs")
        await ctx.send("hambuga chesbuga begmac whapa")

    @commands.command()
    async def pi(self, ctx):

        channel_id = self.bot.get_channel(709669976390500422)

        await ctx.channel.purge(limit=1)
        await channel_id.send(
            "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241965285022210661186306744278622039194945047123713786960956364371917287467764657573962413890865832645995813390478027...")
        await channel_id.send(f"{ctx.author.mention}")

    @commands.command()
    @commands.has_any_role('Big pp')
    async def ping_multiple(self, ctx, member: discord.Member, loops):

        await ctx.channel.purge(limit=1)

        loopz = int(loops)
        num = 0
        while num < loopz + 1:
            await ctx.send({member.mention})
            loopz += 1

    @commands.command()
    async def random_song(self, ctx):

        await ctx.channel.purge(limit=1)

def setup(bot):
    bot.add_cog(Fun(bot))
