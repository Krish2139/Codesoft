def addition(num1, num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1, num2, result))

def subtraction(num1, num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1, num2, result))

def multiplication(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1, num2, result))

def division(num1, num2):
    if num2 == 0.0:
        print("we can't perform the division operation")
    else:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1, num2, result))

