from discord.ext import commands
import discord
import asyncio
import time
import keep_alive

keep_alive.keep_alive()

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot pret")
    await roles()


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, id=1127940982365753374)
    mention = member.mention
    message = f"╭─━━━━━─╯  ⋆⋅☆⋅⋆╰─━━━━━─╮\nSalutation jeune membre {mention}, Bienvenue parmis nous dans ce serveur, ici tu trouvera beaucoup de salon discussion sur plein de thème différent.\nJe t'invite a lire le règlement (pour éviter des sanctions inutile).\n\nEn tout cas mercie a toi de nous avoir rejoins amuse toi bien parmis nous\nhttps://media.tenor.com/_L5pbTv24qoAAAAS/aesthetic-cottagecore.gif"
    await channel.send(message)


@bot.tree.command(
    name="clear_all", description="tout effacer dans un salon, à éxécuter à l'intérieur"
)
async def clear_all(i: discord.Interaction):
    channel = i.channel
    messages = []
    async for message in channel.history(limit=None, oldest_first=True):
        messages.append(message)

    # Faites quelque chose avec la liste des messages récupérés, par exemple, les afficher
    for message in messages:
        await message.delete()


async def add_role(channel, user_id, role_id):
    role = discord.utils.get(
        channel.guild.roles, id=role_id
    )  # Remplacez RoleName par le nom du rôle
    member = channel.guild.get_member(user_id)
    await member.add_roles(role)


async def roles():
    channel = bot.get_channel(1127974431407480942)
    messages = []
    async for message in channel.history(limit=None, oldest_first=True):
        messages.append(message)

    for message in messages:
        await message.delete()

    emojis = ["🍥", "📚", "📕", "🎨", "📊", "🗳️"]
    msg = "Lecteur 📚 \nAnime 🍥 \nManga 📕 \nDessin 🎨 \nDébat 📊 \nSondage 🗳️"
    await channel.send(msg)
    msg = await channel.send("Voici les rôles:")
    for x in emojis:
        await msg.add_reaction(x)


@bot.event
async def on_reaction_add(reaction, user):
    channel_id = reaction.message.channel.id
    if channel_id == 1127974431407480942:
        guild = reaction.message.guild
        user = guild.get_member(user.id)
        channel = guild.get_channel(channel_id)
        emoji = reaction.emoji
        if emoji == "🍥":
            await add_role(channel, user.id, 1127979519911932005)
        elif emoji == "📚":
            await add_role(channel, user.id, 1127979346074808350)
        elif emoji == "📕":
            await add_role(channel, user.id, 1127979957260394616)
        elif emoji == "🎨":
            await add_role(channel, user.id, 1127980148591964251)
        elif emoji == "📊":
            await add_role(channel, user.id, 1127980293450637372)
        elif emoji == "🗳️":
            await add_role(channel, user.id, 1127980433267769526)


async def del_role(guild, user, role_id):
    role = discord.utils.get(guild.roles, id=role_id)
    member = guild.get_member(user.id)
    if role and member:
        await member.remove_roles(role)


@bot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    if channel.id == 1127974431407480942:
        emoji = reaction.emoji
        guild = reaction.message.guild

        if emoji == "🍥":
            await del_role(guild, user, 1127979519911932005)
        elif emoji == "📚":
            await del_role(guild, user, 1127979346074808350)
        elif emoji == "📕":
            await del_role(guild, user, 1127979957260394616)
        elif emoji == "🎨":
            await del_role(guild, user, 1127980148591964251)
        elif emoji == "📊":
            await del_role(guild, user, 1127980293450637372)
        elif emoji == "🗳️":
            await del_role(guild, user, 1127980433267769526)


bot.run("APIKEY")
