from typing import List

from app.Submission import Submission


class User:
    name: str
    score: int
    submissions: List[Submission]

    def __init__(self, name, score=0, submissions=[]):
        self.name = name
        self.score = score
        self.submissions = submissions
