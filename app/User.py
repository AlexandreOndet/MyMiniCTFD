from typing import List

from app.Solve import Solve


class User:
    name: str
    score: int
    solved: List[Solve]

    def __init__(self, name, score=0, solved=[]):
        self.name = name
        self.score = score
        self.solved = solved
