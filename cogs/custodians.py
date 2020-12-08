import discord
from discord.ext import commands
from pymongo import MongoClient
from secrets import MURL


mcli = MongoClient(MURL)
db = mcli.feedback
col = db.suggestions


def repemb(title, description, auth, icon):
    embed = discord.Embed(title=title, description=description, color=0x3499DB)
    embed.set_author(name=auth, icon_url=icon)
    embed.add_field(name="Opinion", value="0", inline=True)
    embed.add_field(name="Votes", value="0", inline=True)
    embed.add_field(name="Comments", value="0", inline=True)
    embed.add_field(name="Additional Info", value="This suggestion is normal", inline=False)
    embed.set_footer(text="Category • What date goes here?")
    return embed


class Custodians(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="info")
    @commands.guild_only()
    @commands.has_role(767921468272934972)
    async def info(self, ctx: commands.Context, suggestion: int):
        fb = db.suggestions.find_one(
            {"fid": int(suggestion)}
        )
        fbtitle = fb["title"]
        fbdesc = fb["description"]
        author = ctx.message.author.display_name
        icon = ctx.message.author.avatar_url

        if fbdesc == 0:
            msg = await ctx.send(embed=repemb(fbtitle, None, author, icon))
        else:
            msg = await ctx.send(embed=repemb(fbtitle, fbdesc, author, icon))

        await msg.add_reaction("<:upvote:767964478570496030>")
        await msg.add_reaction("<:downvote:767964478574690304>")
        await msg.add_reaction("<:report:767964478293278781>")


def setup(client: commands.Bot):
    client.add_cog(Custodians(client))
