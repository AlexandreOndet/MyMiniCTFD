from typing import List
import json

from app.Submission import Submission


class User:
    id: int = 0
    name: str
    score: int
    submissions: List[Submission]

    def __init__(self, name, score=0, submissions=[]):
        self.name = name
        self.score = score
        self.submissions = submissions
        self.id += 1
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getScore(self):
        return self.score
    
    def setScore(self, score):
        self.score = score
    
    def getSubmission(self):
        return self.submissions

    def addSubmission(self, submission : Submission):
        self.submissions.append(submission)
    
    def exportUserInJson(self, filename):
         with open("data/" + filename, 'w') as userfile:
            json.dump([self.__dict__], userfile)

    
    
        
