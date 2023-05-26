from typing import List

from app.CTF import CTF
from app.User import User


class Server:
    ctf: CTF
    users: List[User]

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
        print("CTF %s created!" % name)
        print("CTF Start: %s" % start)
        print("CTF End: %s" % end)

    def registerUser(self, user: User):
        self.users.append(user)
        print("User %s registered!" % user.name)
        