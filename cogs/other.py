import discord
from discord.ext import commands


class Other(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="ping"
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"<@!{ctx.message.author.id}>, Pong!")


def setup(client: commands.Bot):
    client.add_cog(Other(client))
