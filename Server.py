import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from typing import List
from termcolor import colored

from app.CTF import CTF
from app.User import User
from app.Submission import ValidSubmission, InvalidSubmission, DuplicatedSubmission


class Server:
    ctf: CTF
    router: APIRouter

    def __init__(self):
        print(colored("Initializing Server...", "blue"))
        name = input("CTF Name: ")
        define_a_start = input("Define a start time? (y/n): ")
        if define_a_start == "y":
            start = input("CTF Start Time (YYYY-MM-DD HH:MM:SS): ")
        else:
            start = None
        define_an_end = input("Define an end time? (y/n): ")
        if define_an_end == "y":
            end = input("CTF End Time (YYYY-MM-DD HH:MM:SS): ")
        else:
            end = None
        self.ctf = CTF(name, start, end)
        print(colored("CTF %s created!" % self.ctf.name, "green"))
        print(colored("CTF Start: %s" % self.ctf.start, "green"))
        print(colored("CTF End: %s" % self.ctf.end, "green"))
        print(colored("Importing challenges...", "blue"))
        self.importChallengeFromJson("challenges.json")
        print(colored("Initializing API Router...", "blue"))
        self.router = APIRouter()
        self.router.add_api_route("/", self.getInfo, methods=["GET"])
        self.router.add_api_route("/challenges", self.getChallenges, methods=["GET"])
        self.router.add_api_route("/scoreboard", self.getScoreboard, methods=["GET"])
        self.router.add_api_route("/submit", self.postSubmit, methods=["POST"])
        self.router.add_api_route("/users", self.postUser, methods=["POST"])
        self.router.add_api_route("/createChallenges", self.postChallenge, methods=["POST"])

    # API
    def getInfo(self):
        return self.ctf.exportInfoAsJsonForUsers()

    # API
    def getChallenges(self):
        return self.ctf.exportChallengesAsJsonForUsers()

    # API
    def getScoreboard(self):
        return self.ctf.scoreboard.exportScoreboardAsJsonForUsers()

    # API
    def postSubmit(self, id: int, challenge: str, flag: str):
        chall = None
        for c in self.ctf.challenges:
            if c.name == challenge:
                chall = c
                break
        if chall is None:
            return {"warning": "The challenge doesn't exist"}
        submission = self.ctf.scoreboard.submitFlag(flag, chall, id)
        if type(submission) == ValidSubmission:
            return {"message": "Correct flag"}
        elif type(submission) == DuplicatedSubmission:
            return {"message": "Flag already submitted"}
        else:
            return {"message": "Flag incorrect"}

    # API
    def postUser(self, name: str):
        for user in self.ctf.scoreboard.users:
            if user.getName() == name:
                return {"message": "Existing user", "id": user.id}
        user = User(name=name)
        self.ctf.scoreboard.addUser(user)
        return {"message": "User added", "id": user.id}

    # API
    def postChallenge(self, name: str, description: str, category: str, points: int, flag: str):
        self.ctf.createChallenge(name, description, category, points, flag)
        return {"message": f"Challenge {name} added"}

    def printScoreboard(self):
        self.ctf.scoreboard.printScoreboard()

    def createChallenge(self, name, description, category, points, flag):
        self.ctf.createChallenge(name, description, category, points, flag)
        print("Challenge %s created!" % name)

    def removeChallenge(self, challenge):
        self.ctf.removeChallenge(challenge)
        print("Challenge %s removed!" % challenge.name)

    def importChallengeFromJson(self, filename):
        self.ctf.importChallengeFromJson(filename)
        print(colored("Challenges imported from %s!" % filename, "green"))

    def exportChallengesAsJson(self, filename):
        self.ctf.exportChallengesAsJson(filename)
        print("Challenges exported to %s!" % filename)

    def displayChallenges(self):
        self.ctf.displayChallenges()

    def printCTF(self):
        self.ctf.printCTF()


serv = Server()
app = FastAPI()
app.include_router(serv.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
