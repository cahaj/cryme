from commands.slash.help import Help
from commands.slash.wse import Wse

def setup(bot):
    bot.add_cog(Help(bot))
    bot.add_cog(Wse(bot))