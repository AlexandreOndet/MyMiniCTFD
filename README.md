# MyMiniCTFd
Le projet est réalisé dans le cadre du cours MGL802 à l'ÉTS.

L'idée est de faire une sorte de mini CTFd local, en ligne de commande. 
Le but est plus d'implémenter des patrons/style architecturaux qu'autre chose, on ne cherche pas à faire quelque chose utilisable en pratique (tant qu'il ne marche pas en réseau, il ne sert pas à grand-chose).

Cependant, la conception de MyMiniCTFd se veut la plus propre possible et le code le plus facile à comprendre possible.

## Style/Patrons
- Singleton (Observateur du scoreboard)
- Fabrique (Création des challenges)
- Observateur (Scoring)
- Proxy si rien d'autre (gestion des accès)
- MVC (Modèle Vue Contrôleur)

## Exigences minimales
- L'administrateur doit pouvoir créer un CTF
- L'administrateur doit pouvoir ajouter/supprimer/modifier un challenge
- Un joueur doit pouvoir rejoindre un CTF (un joueur doit pouvoir se connecter)
- Un joueur doit pouvoir consulter le scoreboard
- Un joueur doit pouvoir consulter les challenges
- Un joueur doit pouvoir soumettre un flag

