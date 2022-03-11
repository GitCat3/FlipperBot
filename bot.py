from discord.ext import commands
import discord
from flipapi import getFlippers

bot = commands.Bot(command_prefix='f!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="flippers")
async def flippers(ctx):
    flippers = getFlippers()
    shipped, gotten = flippers.split()
    embed = discord.Embed(title="Flippers Shipped", url="https://ship.flipp.dev/", description="Values taken directly from Flipper Zero live count website", color=discord.Color.orange())
    embed.add_field(name="Flippers Shipped", value=f"The number of Flippers that have been shipped is: {shipped}", inline=False)
    embed.add_field(name="Flippers Received", value=f"The number of Flippers that have been received is: {gotten}", inline=False)
    await ctx.send(embed=embed)


bot.run("OTUxODQ4NTYxOTY2OTgxMTMw.YitcDQ.ESgBjlChugxw8DUol00FpVzE6MM")
