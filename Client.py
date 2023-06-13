import requests
import json

APIURL = "http://localhost:8000/"
USER = ""
ID = 0


def printJSON(data: bytes):
    try:
        print(json.dumps(json.loads(data.content.decode()), indent=6))
    except json.decoder.JSONDecodeError:
        print("The server didn't return a valid answer")


def displayMenu():
    print("####################################")
    print("1 - Display the CTF information")
    print("2 - Display the challenges")
    print("3 - Display the scoreboard")
    print("4 - Submit a flag")
    if USER == "admin":
        print("5 - Create a new challenge")
    print("####################################")


def getCTF():
    return requests.get(APIURL)


def getChallenges():
    return requests.get(APIURL + "challenges")


def displayChallenges(challenges):
    dict=eval(json.loads(challenges.content.decode())) # unsafe
    for challenge in dict.values():
        print("####################################")
        print(f"{challenge['name']} ({challenge['category']}) : {challenge['points']} points")
        print(f"Description : {challenge['description']}")



def getScoreboard():
    return requests.get(APIURL + "scoreboard")


def displayScoreboard(scoreboard):
    scoreboard_array=eval(json.loads(scoreboard.content.decode()))
    for rank in scoreboard_array:
        print(f"{rank['rank']} - {rank['name']} : {rank['score']} points")


def submitFlag(challenge: str, flag: str):
    return requests.post(APIURL + "submit", params={"id": ID, "challenge": challenge, "flag": flag})


def createChallenge(name: str, description: str, category: str, points: int, flag: str):
    return requests.post(APIURL + "createChallenges",
                         params={"name": name, "description": description, "category": category, "points": points,
                                 "flag": flag})


if __name__ == "__main__":
    USER = input("What is your name ? ").lower()
    page = requests.post(APIURL + "users", params={"name": USER})
    ID = json.loads(page.content.decode())["id"]
    printJSON(page)
    print(f"Hello {USER} (uid = {ID}), here is the list of challenges :")
    displayChallenges(getChallenges())
    while (True):
        displayMenu()
        userInput = input("> ")
        if USER == "admin":
            try:
                match int(userInput):
                    case 1:
                        printJSON(getCTF())
                    case 2:
                        displayChallenges(getChallenges())
                    case 3:
                        displayScoreboard(getScoreboard())
                    case 4:
                        print("---------Submit Flag---------")
                        challenge = input("-> Write the challenge name : ")
                        flag = input("-> Write the flag : ")
                        print("------------------------")
                        printJSON(submitFlag(challenge, flag))
                    case 5:
                        print("---------Submit Challenge---------")
                        name = input("-> Write the challenge name : ")
                        description = input("-> Write the challenge description : ")
                        category = input("-> Write the challenge category : ")
                        points = int(input("-> Write the number of points the challenge is worth : "))
                        flag = input("-> Write the flag : ")
                        print("------------------------")
                        printJSON(createChallenge(name, description, category, points, flag))
                    case _:
                        print("Invalid choice !")
            except ValueError:
                print("The input must be a number")
        else:
            try:
                match int(userInput):
                    case 1:
                        printJSON(getCTF())
                    case 2:
                        displayChallenges(getChallenges())
                    case 3:
                        displayScoreboard(getScoreboard())
                    case 4:
                        print("---------Submit Flag---------")
                        challenge = input("-> Write the challenge name : ")
                        flag = input("-> Write the flag : ")
                        print("------------------------")
                        printJSON(submitFlag(challenge, flag))
                    case _:
                        print("Invalid choice !")
            except ValueError:
                print("The input must be a number")
