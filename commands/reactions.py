from discord.ext import commands

class Reactions(commands.Cog):
    """Work with Reactions"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
   # print(reaction.emoji)
            # FOLLOWER
        if reaction.emoji == "👍":
            role = user.guild.get_role(827865839193292810)
            await user.add_roles(role)
            # STREAMER
        elif reaction.emoji == "🎬":
            role = user.guild.get_role(827921751777345537)
            await user.add_roles(role)
            # LGBT      
        elif reaction.emoji == "🏳️‍🌈":
            role = user.guild.get_role(827921802550050857)
            await user.add_roles(role)

def setup(bot):
    bot.add_cog(Reactions(bot))
