from commands.slash.help import Help

def setup(bot):
    bot.add_cog(Help(bot))