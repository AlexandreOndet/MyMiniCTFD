from dataclasses import dataclass
from datetime import datetime

from app.Challenge import Challenge



@dataclass
class Submission:
    userId: int
    challenge: Challenge
    timestamp: datetime

    def __init__(self, userId, challenge, timestamp=datetime.now()):
        self.userId = userId
        self.challenge = challenge
        self.timestamp = timestamp


class ValidSubmission(Submission):
    def __init__(self, userId, challenge, timestamp=datetime.now()):
        super().__init__(userId, challenge, timestamp)


class InvalidSubmission(Submission):
    def __init__(self, userId, challenge, timestamp=datetime.now()):
        super().__init__(userId, challenge, timestamp)


class DuplicatedSubmission(Submission):
    def __init__(self, userId, challenge, timestamp=datetime.now()):
        super().__init__(userId, challenge, timestamp)
