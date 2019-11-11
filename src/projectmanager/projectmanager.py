
from random import randint

from src.bot import Bot

class ProjectManager(Bot):

    project_jargon = [
        "Everything is on schedule, keep working hard everyone!",
        "We are making progress toward our milestones, keep up the good work!",
        "According to our gantt chart, we are ahead of schedule, let's keep exceeding expectations!",
        "Our group synergy needs work, let's have a standup to discuss how we can improve efficiency",
        "Let's sync up on our goals to keep the project moving along smoothly",
        "The higher ups want a report by Friday, so let's prioritize the critical tasks",
        "This sprint we have made good progress on the critical path, so we are back on schedule",
        "Our burndown is coming along well, let's finish this sprint strong!"
    ]

    def __init__(self, id):
        """ Create a project manager bot """
        super().__init__(id)

    def manage_project(self, message = None):
        try:
            if "@Project Manager Bot" in message['text'] or "@PM" in message['text']:
                n = randint(0, len(self.project_jargon) - 1)
                self.reply(self.project_jargon[n])
        except KeyError:
            pass


    def status_report_reminder(self):
        self.reply("Remember to send your status reports in so the project can be managed!")