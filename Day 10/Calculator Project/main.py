def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations= {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

#print(operations['*'](4,8))

continue_calculator = True

while continue_calculator:
    first_number = float(input("Type the first number: "))
    operation_choice = input("Choose a mathematical operator: +, -, * or / : ")
    second_number = float(input("Type the second number: "))


    result_number = operations[operation_choice](first_number, second_number)


    should_continue = input(f"Type y to continue with {result_number} or n to reinitialize calculator: ")
    y_to_continue = False
    if should_continue == "y":
        y_to_continue = True
        while y_to_continue:
            first_number = result_number
            operation_choice = input("Choose a mathematical operator: +, -, * or / : ")
            second_number = float(input("Type the second number: "))


            result_number = operations[operation_choice](first_number, second_number)

            should_continue2 = input(f"Type y to continue with {result_number} or n to reinitialize calculator: ")
            if should_continue2 == 'n':
                y_to_continue = False
    else:
        y_to_continue = False
