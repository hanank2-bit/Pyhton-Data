def perform_calculation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        raise ValueError("Invalid operator")


def write_equation_to_file(equation):
    with open('equations.txt', 'a') as file:
        file.write(equation + '\n')


def calculator():
    while True:
        option = input("Choose an option:\n1. Enter a new equation\n2. Read equations from a file\nEnter your choice: ")

        if option == '1':
            try:
                num1 = float(input("Enter the first number: "))
                operator = input("Enter the operator (+, -, *, /): ")
                num2 = float(input("Enter the second number: "))

                result = perform_calculation(num1, num2, operator)
                equation = f"{num1} {operator} {num2} = {result}"

                print("Result:", result)
                write_equation_to_file(equation)
                print("Equation written to file.")
            except (ValueError, ZeroDivisionError) as e:
                print("Invalid input:", e)
                continue

        elif option == '2':
            file_name = input("Enter the name of the text file: ")
            try:
                with open(file_name, 'r') as file:
                    equations = file.readlines()
                    for equation in equations:
                        print(equation.strip())
            except FileNotFoundError:
                print("File not found. Please try again.")
            except Exception as e:
                print("An error occurred while reading the file:", e)
            else:
                break

        else:
            print("Invalid option. Please try again.")


calculator()
