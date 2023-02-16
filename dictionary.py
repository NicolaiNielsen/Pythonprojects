dictionary = {
    "Word": "Definition",
    "Cat": "Definition",
    "Dog": "Definition"
}


while True:
    word = input("Enter word ")

    if word in dictionary:
        print(word, ":", dictionary[word])
    else:
        break