import discord
from discord.ext import commands

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■ Ping ■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class PingCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Ping test to the bot.
        """
        embedPing = discord.Embed(title=f'{round(self.bot.latency * 1000)}ms',
                                    description="Ping of LethalCompagnion bot.",
                                    colour=discord.Colour.from_rgb(240, 128, 128))
        
        # embedPing.set_footer(text="By nous",
        #                     icon_url="https://i.goopics.net/encbhm.png")
        

        await ctx.send(embed=embedPing)

async def setup(bot):
    await bot.add_cog(PingCommand(bot))