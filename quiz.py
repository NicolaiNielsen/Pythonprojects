#add dictionary to store questions
#variable to track score
#loop through dictionary using key value
#display each question
#show final result


quiz = {
    "q1": {
        "q": "What is the capital of France?",
        "answer": "paris"
    },
    "q2": {
        "q": "What is the capital of Germany?",
        "answer": "berlin"
    }, 
    "q3": {
        "q": "What is the capital of Denmark?",
        "answer": "copenhagen"
    }
}


score = 0;

for key, value in quiz.items():
    print(value['q'])
    answer = input("Enter answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Player score: " + str(score))
    else:
        print("Wrong answer")

