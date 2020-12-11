import discord
from discord.ext import commands
from datetime import datetime
from pymongo import MongoClient, ReturnDocument
from secrets import MURL, WURL
from discord_webhook import DiscordWebhook, DiscordEmbed


webhook = DiscordWebhook(url=WURL)
mcli = MongoClient(MURL)
db = mcli.feedback
col = db.suggestions


def sugembed(t, d, f, a, i):
    fbfd = db.suggestions.find_one({'_id': f.inserted_id})
    fid = fbfd["fid"]
    embed_2 = DiscordEmbed(title=t, description=d, color=0x4c2bbe)
    embed_2.set_author(name=f"{a}", icon_url=f"{i}")
    embed_2.add_embed_field(name="Opinion", value="0", inline=True)
    embed_2.add_embed_field(name="Votes", value="0", inline=True)
    embed_2.add_embed_field(name="Comments", value="0", inline=True)
    embed_2.set_footer(text=f"Category • Suggestion ID: {fid}")
    webhook.add_embed(embed_2)
    webhook.execute()


class Feedback(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="suggest")
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def suggest(self, ctx: commands.Context, *content: str):
        if "|" in content:
            try:
                stri = " ".join(content)
                indx = stri.find("|")
                title = stri[0: indx - 1]
                description = stri[indx + 2: len(stri) + 1]
                num = db.suggestions.count() + 1
                author = ctx.message.author.display_name
                icon = ctx.message.author.avatar_url

                channel = self.client.get_channel(768231762705907743)
                embed = discord.Embed(title=title, description=description, color=0x3499DB)
                embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=f"Category • {datetime.today().strftime('%m-%d-%Y')}")
                await ctx.send(embed=embed)

                suggestion = {
                    "fid": num,
                    "author": ctx.message.author.id,
                    "title": title,
                    "description": description,
                    "comments": [],
                }

                fb = db.suggestions.insert_one(suggestion)
                sugembed(title, description, fb, author, icon)
                msg = await channel.fetch_message(channel.last_message_id)
                await msg.add_reaction("<:upvote:767964478570496030>")
                await msg.add_reaction("<:downvote:767964478574690304>")

            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")
        else:
            try:
                stri = " ".join(content)
                title = stri
                num = db.suggestions.count() + 1
                author = ctx.message.author.display_name
                icon = ctx.message.author.avatar_url

                embed = discord.Embed(title=stri, description=None, color=0x3499DB)
                embed.set_author(
                    name=ctx.message.author.display_name,
                    icon_url=ctx.message.author.avatar_url,
                )
                embed.add_field(name="Opinion", value="0", inline=True)
                embed.add_field(name="Votes", value="0", inline=True)
                embed.add_field(name="Comments", value="0", inline=True)
                embed.set_footer(
                    text=f"Category • {datetime.today().strftime('%m-%d-%Y')}"
                )

                await ctx.send(embed=embed)
                suggestion = {"fid": num, "title": title, "description": 0, "comments": []}
                fb = db.suggestions.insert_one(suggestion)
                channel = self.client.get_channel(768231762705907743)
                sugembed(title, None, fb, author, icon)
                msg = await channel.fetch_message(channel.last_message_id)
                await msg.add_reaction("<:upvote:767964478570496030>")
                await msg.add_reaction("<:downvote:767964478574690304>")

            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")

    @commands.command(name="comment")
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def comment(self, ctx: commands.Context, *content: str):
        if "|" in content:
            try:
                stri = " ".join(content)
                indx = stri.find("|")
                idf = stri[0:indx]
                comment = stri[indx + 1: len(stri) + 1]

                commentobject = {
                    "author": f"{ctx.message.author.name}#{ctx.message.author.discriminator}",
                    "comment": comment.lstrip(),
                }

                db.suggestions.find_one_and_update(
                    {"fid": int(idf)},
                    {"$push": {"comments": commentobject}},
                    return_document=ReturnDocument.AFTER,
                )
                embed = discord.Embed(title="Comment added:", description=comment, color=0x3499DB)
                embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=f"Category • Suggestion ID: {idf}")
                await ctx.send(embed=embed)

            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")

    @commands.command(name="edit")
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def edit(self, ctx: commands.Context, *content):
        if "|" in content:
            try:
                stri = " ".join(content)
                indx = stri.find("|")
                idf = stri[0:indx]
                ncont = stri[indx + 1: len(stri) + 1]
                aut = db.suggestions.find_one({"author": int(idf)})

                if ctx.message.author.id == aut:
                    db.suggestions.find_one_and_update(
                        {"fid", int(idf)},
                        {"$push": {"description": ncont}}
                    )

            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")


def setup(client: commands.Bot):
    client.add_cog(Feedback(client))
