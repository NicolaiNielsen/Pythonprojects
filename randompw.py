#Generate password

import string
import random


characters = list(string.ascii_letters + string.digits + "!@¤%#")

def generate():
    password_lenght = 10

    random.shuffle(characters)
    password = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password) #joins all items in list together with no spaces ""

    print(password)

generate()

