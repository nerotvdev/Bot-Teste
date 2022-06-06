from discord.ext import commands

class Manager(commands.Cog):
    """Manager the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Estou pronto! Estou conectado como {self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "palavrão" in message.content:
            await message.channel.send(
                f"Por favor, {message.author.name}, não ofenda os demais usuários! "
            )

            await message.delete()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "!send" in message.content:
            await message.delete()        


def setup(bot):
    bot.add_cog(Manager(bot))
