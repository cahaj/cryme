from commands.slash.help import Help
from commands.slash.wse import Wse
from commands.slash.lastbans import LastBans
from commands.slash.bancheck import BanCheck

def setup(bot):
    bot.add_cog(Help(bot))
    bot.add_cog(Wse(bot))
    bot.add_cog(LastBans(bot))
    bot.add_cog(BanCheck(bot))