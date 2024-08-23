print("\nPython Terminal Calculator for Two Operands")

eval_option = input("""
Select an operation:
 1. Addition
 2. Subtraction
 3. Multiplication
 4. Division
 5. Exponential
\n """)

first_number = input("\nEnter first number: ")
second_number = input("Enter second number: ")


def evaluate(operator_symbol):
    # Using eval to evaluate the expression
    eval_result = eval(f"{first_number} {operator_symbol} {second_number}")
    print(f"Result of {first_number} {operator_symbol} {
          second_number} = {eval_result}")


if eval_option == "1":
    evaluate("+")
elif eval_option == "2":
    evaluate("-")
elif eval_option == "3":
    evaluate("*")
elif eval_option == "4":
    if int(second_number) == 0:
        print(f"{first_number} cannot be divided by {second_number}.")
    else:
        evaluate("/")
elif eval_option == "5":
    evaluate("**")
else:
    print("Operation is not defined")
