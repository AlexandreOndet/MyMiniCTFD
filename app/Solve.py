from datetime import datetime

from app.Challenge import Challenge
from app.User import User


class Solve:
    user: User
    challenge: Challenge
    timestamp: datetime

    def __init__(self, user, challenge, timestamp=datetime.now()):
        self.user = user
        self.challenge = challenge
        self.timestamp = timestamp

