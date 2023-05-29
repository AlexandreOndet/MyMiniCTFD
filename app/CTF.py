import datetime
from typing import List

from app.Challenge import Challenge
from app.Scoreboard import Scoreboard


class CTF:
    name: str
    start: datetime
    end: datetime
    challenges: List[Challenge]
    scoreboard: Scoreboard

    def __init__(self, name, start=datetime.now(), end=datetime.now() + datetime.timedelta(days=1), challenges=[]):
        self.name = name
        self.start = start
        self.end = end
        self.challenges = challenges
        self.scoreboard = Scoreboard()

    def add_challenge(self, challenge: Challenge):
        self.challenges.append(challenge)

    def remove_challenge(self, challenge: Challenge):
        self.challenges.remove(challenge)
