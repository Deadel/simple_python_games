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
'''Kiedyś może spróbuje'''
# operation_list = input("+'\n'-'\n'*'\n'\n'/'\n'^'\n'//'\nGive operation line for calcualtion\n")
#
# for latter in operation_list:
#     try:
#         a= int(latter)
#     except:
#         pass









# def action(a):
#     """Jest to test docsting"""
#     action = input("Pick action you wanna use:\n'+'\n'-'\n'*'\n'\n'/'\n'^'\n'//'\n")
#     b = int(input("Second number: "))
#     function = operations[action]
#     a = function(a,b)
#     print(a)
#     return a
#
# def calculator():
#     print(logo)
#     a = int(input("First number: "))
#     c= action(a)
#     a = c
#     calculate = True
#     while calculate:
#         cont = input("Do you wonna continue? 'y'/'n'").lower()
#         if cont in ['y', 'yes']:
#             action(a)
#         else:
#             calculate = False
# calculator()