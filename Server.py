from typing import List

from app.CTF import CTF


class Server:
    ctf: CTF

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


if __name__ == "__main__":
    serv = Server()

    while True:
        print("1. Print CTF")
        print("2. Print Scoreboard")
        print("3. Add Challenge")
        print("4. Remove Challenge")
        print("5. Import Challenges from JSON")
        print("6. Export Challenges to JSON")
        print("7. Display Challenges")
        print("8. Exit")
        choice = input("Choice: ")
        if choice == "1":
            serv.printCTF()
        elif choice == "2":
            serv.printScoreboard()
        elif choice == "3":
            name = input("Name: ")
            description = input("Description: ")
            flag = input("Flag: ")
            points = input("Points: ")
            category = input("Category: ")
            serv.createChallenge(name, description, category, points, flag)
        elif choice == "4":
            name = input("Name: ")
            serv.removeChallenge(name)
        elif choice == "5":
            filename = input("Filename: ")
            serv.importChallengeFromJson(filename)
        elif choice == "6":
            filename = input("Filename: ")
            serv.exportChallengesAsJson(filename)
        elif choice == "7":
            serv.displayChallenges()
        elif choice == "8":
            break
        else:
            print("Invalid choice!")
