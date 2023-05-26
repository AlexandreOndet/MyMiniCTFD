from typing import List

from app.Submission import Submission
from app.SubmissionCreator import SubmissionCreator
from app.User import User


class Scoreboard:
    solves: List[Submission]
    users: List[User]
    instance = None

    def __init__(self, solves=[], users=[]):
        if self.instance is not None:
            raise Exception("Scoreboard is a singleton!")
        else:
            self.solves = solves
            self.users = users
            self.instance = self

    def getInstance(self):
        if self.instance is None:
            self.instance = Scoreboard()
        return self.instance

    def submitFlag(self, flag, challenge, user):
        if challenge.checkFlag(flag):
            submission = SubmissionCreator.create_valid_submission(user, challenge)
            self.addSolve(submission)
        else:
            SubmissionCreator.create_invalid_submission(user, challenge)

    def addSolve(self, solve: Submission):
        self.solves.append(solve)
        self.updateScoreboard()

    def addUser(self, user: User):
        self.users.append(user)
        self.updateScoreboard()

    def updateScoreboard(self):
        for user in self.users:
            user.score = 0
            for solve in self.solves:
                if solve.user.name == user.name:
                    user.score += solve.challenge.points
        self.users.sort(key=lambda x: x.score, reverse=True)

    def printScoreboard(self):
        for rank in range(len(self.users)):
            print("%s. %s (%s)" % (rank + 1, self.users[rank].name, self.users[rank].score))

