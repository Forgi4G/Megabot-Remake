import discord
from discord.ext import commands
import os
import traceback
from secrets import TOKEN
# import json


client = commands.Bot(command_prefix="!", case_insensitive=True)


if __name__ == '__main__':
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{file[:-3]}")
            except (discord.ClientException, ModuleNotFoundError):
                print(traceback.format_exc())


client.run(TOKEN)
