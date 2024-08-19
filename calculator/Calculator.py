from art import logo


def adding(a,b):
    result = a + b
    return result
def substract(a,b):
    result = a - b
    return result
def multiplication(a,b):
    result = a * b
    return result
def division(a,b):
    if b == 0:
        return "Error: Division by zero"
    result = a / b
    return result
def power (a,b):
    result = a ** b
    return result
def elem(a,b):
    if b == 0:
        return "Error: Division by zero"
    result = a ** (1/b)
    return result

operations = {
    "+": adding,
    "-": substract,
    "*": multiplication,
    "/": division,
    "**": power,
    "//": elem,
}



def action(a):
    """Jest to test docsting"""
    action = input("Pick action you wanna use:\n'+'\n'-'\n'*'\n'\n'/'\n'^'\n'//'\n")
    b = float(input("Second number: "))
    function = operations[action]
    a = function(a,b)
    # if action == '+':
    #     a = adding(a,b)
    # elif action == '-':
    #     a = substract(a,b)
    # elif action == '*':
    #     a = multiplication(a,b)
    # elif action == '/':
    #     a = division(a,b)
    # elif action == '^':
    #     a = power(a,b)
    # elif action == '//':
    #     a = elem(a,b)
    print(a)
    return a

def calculator():
    print(logo)
    a = float(input("First number: "))
    c= action(a)
    a = c
    calculate = True
    while calculate:
        cont = input("Do you wonna continue? 'y'/'n'").lower()
        if cont in ['y', 'yes']:
            action(a)
        else:
            new_calc = input("Do you wonna new calculation? 'y'/'n'").lower()
            if new_calc in ['y', 'yes']:
                calculator()
            else:
                calculate = False
calculator()