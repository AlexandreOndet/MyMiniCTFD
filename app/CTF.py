from datetime import datetime, timedelta
import json
from typing import List

from app.Challenge import Challenge
from app.Scoreboard import Scoreboard
from termcolor import colored


class CTF:
    name: str
    start: datetime
    end: datetime
    challenges: List[Challenge]
    scoreboard: Scoreboard

    def __init__(self, name, start=datetime.now(), end=datetime.now() + timedelta(days=1), challenges=[]):
        self.name = name
        self.start = start
        self.end = end
        self.challenges = challenges
        self.scoreboard = Scoreboard()
        print(colored("Importing users...", "blue"))
        self.scoreboard.importUserFromJson("users.json")

    def addChallenge(self, newChall: Challenge):
        for chall in self.challenges:
            if chall.name == newChall.name:
                raise Exception("Challenge already exists")
                return
        self.challenges.append(newChall)

    def createChallenge(self, name: str, description: str, category: str, points: int, flag: str):
        self.addChallenge(Challenge(name, description, category, points, flag))

    def removeChallenge(self, name: str):
        for challenge in self.challenges:
            if challenge.name == name:
                self.challenges.remove(challenge)

    def exportChallengesAsJson(self, filename):
        with open("data/" + filename, 'w') as outfile:
            json.dump([challenge.__dict__ for challenge in self.challenges], outfile)

    def exportChallengesAsJsonForUsers(self):
        challengesWithoutFlag = {}
        for challenge in self.challenges:
            challengesWithoutFlag[challenge.name] = {
                "name": challenge.name,
                "description": challenge.description,
                "category": challenge.category,
                "points": challenge.points
            }
        return json.dumps(challengesWithoutFlag)


    def importChallengeFromJson(self, filename):
        with open("data/" + filename) as json_file:
            data = json.load(json_file)
            for challenge in data:
                self.addChallenge(
                    Challenge(challenge['name'], challenge['description'], challenge['category'], challenge['points'],
                              challenge['flag']))

    def displayChallenges(self):
        """show all challenges by category"""
        for challenge in self.challenges:
            print(challenge.name, challenge.category, challenge.points, sep=" | ")

    def exportInfoAsJsonForUsers(self):
        info = {
            "Name": self.name,
            "Start time": self.start,
            "End time": self.end
        }
        return json.dumps(info)

    def printCTF(self):
        print("CTF Name: %s" % self.name)
        print("CTF Start: %s" % self.start)
        print("CTF End: %s" % self.end)
        print("Challenges:")
        self.displayChallenges()
        print("Scoreboard:")
        self.scoreboard.printScoreboard()