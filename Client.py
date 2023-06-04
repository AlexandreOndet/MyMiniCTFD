import requests
import json

APIURL = "http://localhost:8000/"
USER = ""
ID = 0

def printJSON(data: bytes):
    print(json.dumps(json.loads(data.content.decode()), indent=6))

def displayMenu():
    print("####################################")
    print("1 - Afficher les informations du CTF")
    print("2 - Afficher les challenges")
    print("3 - Afficher le classement")
    print("4 - Soumettre un flag")
    print("####################################")

def displayCTF():
    return requests.get(APIURL)

def displayChallenges():
    return requests.get(APIURL + "challenges")

def displayScoreboard():
    return requests.get(APIURL + "scoreboard")

def submitFlag(challenge: str, flag: str):
    return requests.post(APIURL + "submit", params={"id":ID, "challenge": challenge, "flag": flag})

if __name__ == "__main__":
    USER = input("Quel est votre nom ? ").lower()
    page = requests.post(APIURL + "users", params={"name":USER})
    ID = json.loads(page.content.decode())["id"]
    printJSON(page)
    print(f"Bonjour {USER} (uid = {ID}), voici la liste des challenges disponibles")
    printJSON(displayChallenges())
    while(True):
        displayMenu()
        userInput = input("> ")
        match int(userInput):
            case 1:
                printJSON(displayCTF())
            case 2:
                printJSON(displayChallenges())
            case 3:
                printJSON(displayScoreboard())
            case 4:
                print("---------Submit---------")
                challenge = input("-> Saisissez le nom du challenge : ")
                flag = input("-> Saisissez le flag : ")
                print("------------------------")
                printJSON(submitFlag(challenge, flag))
            case _:
                print("Choix non reconnu !")