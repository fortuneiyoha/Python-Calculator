print("\nCalculator Version 1.0.0")
print("""
Select an operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponential
""")

eval_option = int(input(""))
first_number = int(input("\nEnter first number: "))
second_number = int(input("Enter second number: "))
eval_result = int()


if eval_option == 1:
    eval_result = first_number + second_number
    print(f"Result of {first_number} + {second_number} = {eval_result}")
elif eval_option == 2:
    eval_result = first_number - second_number
    print(f"Result of {first_number} - {second_number} = {eval_result}")
elif eval_option == 3:
    eval_result = first_number * second_number
    print(f"Result of {first_number} * {second_number} = {eval_result}")
elif eval_option == 4:
    if second_number == 0:
        print(f"{first_number} cannot be divided by {second_number}.")
    else:
        eval_result = first_number / second_number
        print(f"Result of {first_number} / {second_number} = {eval_result}")
elif eval_option == 5:
    eval_result = first_number ** second_number
    print(f"Result of {first_number} ** {second_number} = {eval_result}")
else:
    print("Operation is not defined")
