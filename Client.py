import requests

APIURL = "http://localhost:8000/"

if __name__ == "__main__":
    nom = input("Quel est votre nom ?").lower()
    page = requests.post(APIURL + "users", params={"name":nom})
    print(page)
    print(f"Bonjour {nom}, voici la liste des challenges disponibles")
        
    