import uvicorn
from fastapi import FastAPI, APIRouter
from typing import List

from app.CTF import CTF

class Server:
    ctf: CTF
    router: APIRouter

    def __init__(self):
        print("Initializing Server...")
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
        print("CTF %s created!" % self.ctf.name)
        print("CTF Start: %s" % self.ctf.start)
        print("CTF End: %s" % self.ctf.end)
        print("Importing challenges...")
        self.importChallengeFromJson("challenges.json")
        print("Initializing API Router...")
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_info, methods=["GET"])

    def get_info(self):
        return {"Hello": "World!"}

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
        print("Challenges imported from %s!" % filename)

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