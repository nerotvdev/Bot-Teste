import discord
from discord.ext import commands

class Images(commands.Cog):
    """Works with images"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hug", help="Abrace Alguém")
    async def send_hug(self, ctx):
        url_hug = "https://picsum.photos/1920/1080"

        embed = discord.Embed(
            title=" Fulano Abraçou Ciclano.",
            description="Powered By GIPHY",
            color=0xca1cce,
        )
        
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por" + self.bot.user.name, icon_url=self.bot.user.avatar_url)
        
        embed.set_image(url=url_hug)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Images(bot))
