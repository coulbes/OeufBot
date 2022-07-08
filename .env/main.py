import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.members = True
bot = commands.Bot(command_prefix="!", intents=default_intents)


@bot.event
async def on_ready():
    print("Le bot est prêt")


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Ixtali")
    await member.add_roles(role)
    log: commands.TextChannel = bot.get_channel(993440601158717530)
    await log.send(content=f"@{member.display_name} joined the server")


@bot.event
async def on_member_remove(member):
    log: commands.TextChannel = bot.get_channel(993440601158717530)
    await log.send(content=f"@{member.display_name} left the server")


# ~~~~~~~~~~ COMMAND BOT ~~~~~~~~~~


@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nb: int):
    nb += 1
    messages = await ctx.channel.history(limit=nb).flatten()
    for message in messages:
        await message.delete()

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    log: commands.TextChannel = bot.get_channel(993440601158717530)
    await log.send(content=f"{user} has been kicked for : {reason}")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    log: commands.TextChannel = bot.get_channel(993440601158717530)
    await log.send(content=f"{user} has been baned for : {reason}")

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            log: commands.TextChannel = bot.get_channel(993440601158717530)
            await log.send(f"{user} is now unban for : {reason}")
            return
    await log.send(f"{user} not found")


replique=[
    "\"You may now appreciate me.\"",
    "\"Congratulations, you have Qiyana. The other side, they have no Qiyana.\"",
    "\"Oh, good, servants. Carry my panoply to the battle, would you?\"",
    "\"I don't mean to sound arrogant, but I'm extremely good, at everything.\""
    "\"Is that all they brought to face us? My omele could defeat them, and she is 85.\"",
    "\"Cover the ground behind me. None may tread where I have stepped.\"",
    "\"I can tell by your expressions you've never met a superior being.\"",
    "\"Some people are just born better.\"",
    "\"I'm not arrogant, I'm right.\"",
    "\"My enemies try their best. That is what is so sad.\"",
    "\"It's not a ring blade, it's an ohmlatl! Idiots.\"",
    "\"No more hiding in the wilderness. I demand to be seen!\"",
    "\"If they want to worship me... hmph, I will not stop them.\"",
    "\"Some wait their turn, and some take what they deserve.\"",
    "\"If talent were an element, perhaps I could throw some at them.\"",
    "\"Empress Qiyana...' I do like the sound of that.\"",
    "\"I do not lack empathy. Other people just need to be better.\"",
    "\"You know what's hard about being a princess? Nothing.\"",
    "\"I cannot wait to be empress.\"",
    "\"Hard work is for those who possess no talent.\"",
    "\"Those who find Ixtal do not live to speak of it.\"",
    "\"I will grant this place the privilege of being conquered by me.\"",
    "\"There will always be someone who is better, and that person is me.\"",
    "\"Things do what I tell them to. Right, rocks?\"",
    "\"The secrets of my enemies carry far on the wind.\"",
    "\"Of course I've mastered fire... I just don't like to show off.\"",
    "\"Ee-shao-can! They will all learn to say it.\"",
    "\"One throne, nine sisters. Nine tragic accidents waiting to happen.\"",
    "\"This place will be a lovely addition to my empire.\""]

emojies=[
    "https://cdn.discordapp.com/emojis/970656430132703232.png",
    "https://cdn.discordapp.com/emojis/976866217690296389.png",
    "https://cdn.discordapp.com/emojis/970656443869048851.png",
    "https://cdn.discordapp.com/emojis/976568447272116224.png",
    "https://cdn.discordapp.com/emojis/970656374415577148.png",
    "https://cdn.discordapp.com/emojis/976568389705297951.png",
    "https://cdn.discordapp.com/emojis/976568683851829298.png",
    "https://cdn.discordapp.com/emojis/976568683851829298.png",
    "https://cdn.discordapp.com/emojis/976568641099292752.png"]

@bot.command()
@commands.has_permissions(ban_members = True)
async def live(ctx, *, message="Qiyana part au combat ! Venez admirer votre Impératrice et montrer votre dévouement !"):
    role = discord.utils.get(ctx.guild.roles, name="Apprenti")
    embed = discord.Embed(title = "**QUE LE LIVE COMMENCE**", description = "Clique sur le liens au-dessus !", url = "https://www.twitch.tv/sollahtv", color = 0xd3ffce)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url= random.choice(emojies))
    embed.add_field(name= "●▬▬๑۩۩๑▬▬●", value= message, inline= True)
    embed.set_footer(text = random.choice(replique))

    annonce: commands.TextChannel = bot.get_channel(959919810819543083)
    await annonce.send(f"{role.mention}", embed = embed)
    
bot.run(os.getenv("TOKEN"))