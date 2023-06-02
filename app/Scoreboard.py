from typing import List
import json

from app.Submission import Submission
from app.SubmissionCreator import SubmissionCreator
from app.User import User

class Scoreboard:
    solves: List[Submission]
    users: List[User]
    instance = None

    def __init__(self, solves=None, users=None):
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

    def submitFlag(self, flag, challenge, userId):
        user = None
        for u in self.users:
            if u.id == userId:
                user = u
                break
        if user is None:
            raise Exception("User not found!")

        if not challenge.checkFlag(flag):
            s = SubmissionCreator.create_invalid_submission(userId, challenge)
            user.submissions.append(s)
            return
        for submission in user.submissions:
            if (submission.challenge == challenge) and (submission.challenge.checkFlag(flag)):
                s = SubmissionCreator.create_duplicated_submission(userId, challenge)
                user.submissions.append(s)
                return
        s = SubmissionCreator.create_valid_submission(userId, challenge)
        self.addSolve(s)
        user.submissions.append(s)

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

    def exportScoreboardAsJsonForUsers(self):
        scoreboard = []
        for rank in range(len(self.users)):
            scoreboard.append({"rank": rank+1, "name": self.users[rank].name, "score": self.users[rank].score})
        return json.dumps(scoreboard)
    
    def importUserFromJson(self, filename):
        with open("data/" + filename) as userfile:
            data = json.load(userfile)
            for user in data:
                self.addUser(User(user['name'], user['description'], user['submissions']))

        

