import uvicorn
from fastapi import FastAPI, APIRouter
from typing import List
from termcolor import colored

from app.CTF import CTF

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
        self.router.add_api_route("/", self.get_info, methods=["GET"])
        self.router.add_api_route("/challenges", self.get_challenges, methods=["GET"])
        self.router.add_api_route("/scoreboard", self.get_scoreboard, methods=["GET"])
        self.router.add_api_route("/submit", self.post_submit, methods=["POST"])

    # API
    def get_info(self):
        return {"Hello": "World!"}
    
    # API
    def get_challenges(self):
        return self.ctf.exportChallengesAsJsonForUsers()

    # API
    def get_scoreboard(self):
        return self.ctf.scoreboard.exportScoreboardAsJsonForUsers()

    # API
    def post_submit(self):
        pass

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