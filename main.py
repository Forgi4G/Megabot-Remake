import discord
from discord.ext import commands
import os
import traceback
from pymongo import MongoClient
from secrets import TOKEN, MURL


client = commands.Bot(command_prefix="!", case_insensitive=True)
mcli = MongoClient(MURL)


client.load_extension('jishaku')


db = mcli.feedback
count = db["suggestions"].count_documents({})


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                           name=f"{count} suggestions!"))
    print(f"Currently in {len(list(client.guilds))} guilds.")


if __name__ == '__main__':
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{file[:-3]}")
            except (discord.ClientException, ModuleNotFoundError):
                print(traceback.format_exc())


client.run(TOKEN)
