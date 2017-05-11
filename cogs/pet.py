import discord
import random
from discord.ext import commands

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
	print('ok')
except:
	soupAvailable = False
	print('error')
import aiohttp

class Paw:
	"""My custom cog that does stuff!"""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(name="paw", no_pm=True, pass_context=True)
	async def paw(self, ctx):
		if ctx.invoked_subcommand is None:
			await self.bot.say("I would do anything you like only if... (command: pat, lick, penis)")

	@paw.command(pass_context=True, name="pat")
	async def paw_pat(self, ctx, *, term: str=None):
		num = random.randint(1, 7)
		try:
			if num == 1:
				await self.bot.say("Meow Meow Meow ~")
			elif num == 2:
				await self.bot.say("What do ya want?")
			elif num == 3:
				await self.bot.say("Hey man, need a hug?")
			elif num == 4:
				await self.bot.say("The stars have judged you and found you wanting.")
			elif num == 5:
				await self.bot.say("*Paw cries on your shoulder*")
			elif num == 6:
				await self.bot.say("*Paw cries on your shoulder*")
			else:
				await self.bot.say("Nobody likes paw...")
		except:
			await self.bot.say("error")

	@paw.command(pass_context=True, name="lick")
	async def paw_lick(self, ctx, *, term: str=None):
		try:
			await self.bot.say("=A= paw doesn't like that.")
		except:
			await self.bot.say("error")

	@paw.command(pass_context=True, name="penis")
	async def paw_penis(self, ctx, *, term: str=None):
		try:
			await self.bot.say("...... not gonna tell you")
		except:
			await self.bot.say("error")

def setup(bot):
	if soupAvailable:
		bot.add_cog(Paw(bot))
	else:
		raise RuntimeError("You need to run `pip3 install beautifulsoup4`")