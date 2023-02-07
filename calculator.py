#define functions, add, sub, mul, div
def add(a, b):
    answer = a + b
    print(str(a) + '+' + str(b) + '=' + answer)

def sub(a, b):
    answer = a - b
    print(str(a) + '-' + str(b) + '=' + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + '*' + str(b) + '=' + answer)

def div(a, b):
    answer = a / b
    print(str(a) + '/' + str(b) + '=' + answer)

#print options to users
def options():
    while True:
        choice = input("do you want to add, sub, mul or div? or exit")
        
        if choice == "sub":
            a = input("Input first number")
            b = input("Input first number")
            
            sub(int(a), int(b))
        if choice == "exit":
            print("Program stopped")
            quit()

options()
#ask for values
#call the functions
#while loop to continue program and prints