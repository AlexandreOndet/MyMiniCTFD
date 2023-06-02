import requests

APIURL = "https://localhost:8000/users/"

if __name__ == "__main__":
    name = input("Quel est votre nom ?").lower()
    
    #post : name if name existe déjà récupération du score
    requests.post("APIURL",name)
    print(f"Bonjour {name}, voici la liste des challenges disponibles")
    
    
    