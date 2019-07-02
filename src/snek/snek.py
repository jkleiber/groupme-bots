
from src.bot import Bot

# GroupMe Bot ID

class Snek(Bot):

    def __init__(self, id):
        """ Create a snek bot """
        super().__init__(id)
    
    def sendSnek(self, message):
        if not self.sender_is_bot(message):
            self.reply("No step on snek")