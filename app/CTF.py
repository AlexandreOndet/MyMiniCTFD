import datetime
from typing import List

from app.Challenge import Challenge


class CTF:
    name: str
    start: datetime
    end: datetime
    challenges: List[Challenge]

    def __init__(self, name, start=datetime.now(), end=datetime.now() + datetime.timedelta(days=1), challenges=[]):
        self.name = name
        self.start = start
        self.end = end
        self.challenges = challenges

    def add_challenge(self, challenge: Challenge):
        self.challenges.append(challenge)
