
from src.bot import Bot

class ProjectManager(Bot):

    def __init__(self, id):
        """ Create a project manager bot """
        super().__init__(id)

    def manage_project(self, message = None):
        pass