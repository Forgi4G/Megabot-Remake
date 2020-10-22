import discord
from discord.ext import commands
import datetime


class Feedback(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="suggest"
    )
    async def suggest(self, ctx:commands.Context, title: str, separator="|", description=None):
        try:
            user = ctx.message.author
            pf = user.avatar_url
            name = user.display_name
            embed = discord.Embed(title=title, description=description, color=0x3499DB)
            embed.set_author(name=name, icon_url=pf)
            embed.add_field(name="Opinion", value="0", inline=True)
            embed.add_field(name="Votes", value="0", inline=True)
            embed.add_field(name="Comments", value="0", inline=True)
            embed.add_field(name="Additional info", value="This suggestion is normal", inline=False)
            embed.set_footer(text=f"Category • {datetime.date.today()}")
            await ctx.send(embed=embed)
        except discord.HTTPException as err:
            await ctx.send(f"Error: {err.text}")


def setup(client: commands.Bot):
    client.add_cog(Feedback(client))
