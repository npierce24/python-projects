import time 
#Solve
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b)+ " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b)+ " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b)+ " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b)+ " = " + str(answer))

#Choices
while True:
    print("\nA. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    #inputs
    choice = input("\nInput your choice: ")

    if choice == "a" or choice == "A":
        print("Using Addition")
        a = int(input("\nInput First Number: "))
        b = int(input("Input Second Number: "))
        add(a, b)
        time.sleep(3)

    elif choice == "b" or choice == "B":
        print("Using Subtraction")
        a = int(input("\nInput First Number: "))
        b = int(input("Input Second Number: "))
        sub(a, b)
        time.sleep(3)

    elif choice == "c" or choice == "C":
        print("Using Multiplication")
        a = int(input("\nInput First Number: "))
        b = int(input("Input Second Number: "))
        mul(a, b)
        time.sleep(3)

    elif choice == "d" or choice == "D":
        print("Using Division")
        a = int(input("\nInput First Number: "))
        b = int(input("Input Second Number: "))
        div(a, b)
        time.sleep(3)

    elif choice == "e" or choice == "E":
        print("\nThe Program Has Ended")
        print("closing in...")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        quit()