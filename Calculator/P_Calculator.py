from P_Cal_Function import *

while True:
    print("what do you want to do?")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("press the key Q for exit")

    choice = input("Enter your choice : ")

    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("Enter the num1 : "))
    num2 = float(input("Enter the num2 : "))

    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Invalid choice")

    print("\n")
