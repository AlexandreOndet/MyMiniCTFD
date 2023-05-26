from typing import List

from app.Solve import Solve
from app.User import User


class Scoreboard:
    solves: List[Solve]
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

    def addSolve(self, solve: Solve):
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

