import discord
import random
from discord.ext import commands

class Penis:
    """Penis related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def penis(self, *, user : discord.Member):
        """Detects user's penis length

        This is 100% accurate.

        2/5 更新:现在会随机伸缩了(在原来长度基础上)"""
        state = random.getstate()
        random.seed(user.id)
        avg_dong = random.randint(0, 30)
        random.seed()
        dong = "8{}D".format("=" * random.randint(max(0, avg_dong - 5), avg_dong + 5))
        random.setstate(state)
        await self.bot.say("Size: " + dong)


def setup(bot):
    bot.add_cog(Penis(bot))
