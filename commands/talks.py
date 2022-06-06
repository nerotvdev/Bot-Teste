import discord
from discord.ext import commands


class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi", help="Fale oi pra alguém")
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = "Olá, " + name

        await ctx.send(response)

    @commands.command(name="send", help="Envie uma mensagem através do bot")
    async def send_msg(self, ctx, message):

        embed = discord.Embed(
            title="Anuncio",
            # description=message,
            color=0xca1cce,
        )

        embed.add_field(
            name="",
            value=message,
            inline=True,
        )

        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar_url)

        embed.set_footer(text=f"Mensagem enviada por" + {ctx.author.name},
                         icon_url=ctx.author.avatar_url)

       # embed.set_image(url=url_hug)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Talks(bot))
