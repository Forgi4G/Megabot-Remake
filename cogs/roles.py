import discord
from discord.ext import commands


class Roles(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="test",
        aliases=["t"]
    )
    # @commands.dm_only
    async def buy_role(self, ctx:commands.context):
        embed = discord.Embed(title="MegaBot Store", color=0x9AD2C9)
        embed.add_field(name="** **", value="**1**: Custodians - 150 EXP \n **2**: Record Keeper - 350 EXP \n **3**: "
                                            "Book Keeper - 750 EXP \n **4**: Librarian - 1500 EXP \n **5**: Vizier - "
                                            "2400 EXP \n **6**: Grand Vizier - 4770 EXP" , inline=False)
        embed.add_field(name="** **", value="*Use* `!buy roles role-number` *to buy a role*")
        embed.set_footer(text="MegaBot Remake v1.0.0")
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Roles(client))