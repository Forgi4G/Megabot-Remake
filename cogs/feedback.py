import discord
from discord.ext import commands
from datetime import datetime
from pymongo import MongoClient
from secrets import MURL


mcli = MongoClient(MURL)
db = mcli.feedback


class Feedback(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="suggest"
    )
    async def suggest(self, ctx: commands.Context, *content: str):
        if "|" in content:
            try:
                stri = " ".join(content)
                indx = stri.find("|")
                title = stri[0:indx]
                description = stri[indx + 1:len(stri) + 1]
                embed = discord.Embed(title=title, description=description, color=0x3499DB)
                embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=f"Category • {datetime.today().strftime('%m-%d-%Y')}")
                await ctx.send(embed=embed)
                suggestion = {
                    title: title,
                    description: description
                }
                db.suggestions.insert_one(suggestion)
                # channel = 768231762705907743
                # fb_id = fb.get("_id")
                # embed_2 = discord.Embed(title=title, description=description, color=0x3499DB)
                # embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                # embed.add_field(name="Opinion", value="0", inline=True)
                # embed.add_field(name="Votes", value="0", inline=True)
                # embed.add_field(name="Comments", value="0", inline=True)
                # embed.set_footer(text=f"Category • Suggestion ID: {fb_id}")
                # await channel.send(embed=embed_2)
            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")
        else:
            try:
                stri = " ".join(content)
                embed = discord.Embed(title=stri, description=None, color=0x3499DB)
                embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                embed.add_field(name="Opinion", value="0", inline=True)
                embed.add_field(name="Votes", value="0", inline=True)
                embed.add_field(name="Comments", value="0", inline=True)
                embed.set_footer(text=f"Category • {datetime.today().strftime('%m-%d-%Y')}")
                await ctx.send(embed=embed)
            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")

    # @commands.command(
    #     name="info"
    # )
    # async def info(self, ctx: commands.Context):

def setup(client: commands.Bot):
    client.add_cog(Feedback(client))
