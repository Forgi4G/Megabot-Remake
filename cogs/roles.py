import discord
from discord.ext import commands


roleids = {
    "1": 767921468272934972,
    "2": 767922049443954719,
    "3": 767921943184932904,
    "4": 767921702314573834,
    "5": 767922513664802827,
    "6": 767921509867454504
}

rolenames = {
    "1": "Custodian",
    "2": "Record Keeper",
    "3": "Book Keeper",
    "4": "Librarian",
    "5": "Vizier",
    "6": "Grand Vizier"
}


class Roles(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="test",
        aliases=["t"]
    )
    @commands.dm_only()
    async def buy_role(self, ctx: commands.Context, rnumber=None):
        if rnumber:
            role = discord.utils.get(ctx.guild.roles, name=rolenames[rnumber])
            if role in ctx.author.roles:
                await ctx.send("You already have this role.")
            else:
                try:
                    await self.client.http.add_role(guild_id=767915067478900746, user_id=ctx.message.author.id,
                                                    role_id=roleids[rnumber])
                    await ctx.send(f"Role added")  # add context
                except discord.HTTPException as err:
                    await ctx.send(f"Error: {err.text}")
        else:
            try:
                embed = discord.Embed(title="MegaBot Store", color=0x9AD2C9)
                embed.add_field(name="** **", value="**1**: Custodians - 150 EXP \n **2**: Record Keeper - 350 EXP \n "
                                                    "**3**: Book Keeper - 750 EXP \n **4**: Librarian - 1500 EXP \n "
                                                    "**5**: Vizier - 2400 EXP \n **6**: Grand Vizier - 4770 EXP",
                                inline=False)
                embed.add_field(name="** **", value="*Use* `!buy roles role-number` *to buy a role*")
                embed.set_footer(text="MegaBot Remake v1.0.0")
                await ctx.send(embed=embed)
            except discord.HTTPException as err:
                await ctx.send(f"Error: {err.text}")


def setup(client: commands.Bot):
    client.add_cog(Roles(client))
