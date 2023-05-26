from dataclasses import dataclass
from datetime import datetime

from app.Challenge import Challenge
from app.User import User


@dataclass
class Submission:
    user: User
    challenge: Challenge
    timestamp: datetime

    def __init__(self, user, challenge, timestamp=datetime.now()):
        self.user = user
        self.challenge = challenge
        self.timestamp = timestamp
        user.submissions.append(self)


class ValidSubmission(Submission):
    def __init__(self, user, challenge, timestamp=datetime.now()):
        super().__init__(user, challenge, timestamp)


class InvalidSubmission(Submission):
    def __init__(self, user, challenge, timestamp=datetime.now()):
        super().__init__(user, challenge, timestamp)
