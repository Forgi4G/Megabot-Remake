import discord
from discord.ext import commands
from datetime import datetime


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
            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")
        else:
            try:
                embed = discord.Embed(title=content, description=None, color=0x3499DB)
                embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                embed.add_field(name="Opinion", value="0", inline=True)
                embed.add_field(name="Votes", value="0", inline=True)
                embed.add_field(name="Comments", value="0", inline=True)
                embed.set_footer(text=f"Category • {datetime.today().strftime('%m-%d-%Y')}")
                await ctx.send(embed=embed)
            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")


def setup(client: commands.Bot):
    client.add_cog(Feedback(client))
