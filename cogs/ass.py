import discord
import random
from discord.ext import commands

class Ass:
    """Vagina related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ass(self, *, user : discord.Member):
        """Detects user's ass depth

        This is 99% accurate."""
        state = random.getstate()
        random.seed(user.id * 2)
        dong = "({{}}){}O".format("=" * random.randint(0, 30))
        random.setstate(state)
        await self.bot.say("Depth: " + dong)


def setup(bot):
    bot.add_cog(Ass(bot))
