from datetime import datetime, timedelta
import json
from typing import List

from app.Challenge import Challenge
from app.Scoreboard import Scoreboard


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

    def addChallenge(self, challenge: Challenge):
        self.challenges.append(challenge)

    def removeChallenge(self, challenge: Challenge):
        self.challenges.remove(challenge)

    def exportChallengesAsJson(self, filename):
        with open("data/" + filename, 'w') as outfile:  # unsafe
            json.dump([challenge.__dict__ for challenge in self.challenges], outfile)

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
