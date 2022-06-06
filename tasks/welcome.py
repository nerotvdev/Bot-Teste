from discord.ext import commands

class welcome(commands.Cog):
    """Work with date"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        # canal = member.guid.get_channel(827855376283598850)
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)


def setup(bot):
    bot.add_cog(welcome(bot))