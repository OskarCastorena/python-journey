import pyfiglet

print(pyfiglet.figlet_format('CALCULATOR', font='big'))

a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))

operation = input('''
which operation would you like to perform?

+---+----------------+
| + | Addition       |
| - | Subtraction    |
| * | Multiplication |
| / | Division       |
+---+----------------+

Enter the symbol:
''')

if operation == '+':
    print(f"the sum of {a} and {b} is {a + b}")
elif operation == '-':
    print(f"the subtraction of {a} and {b} is {a - b}")
elif operation == '*':
    print(f"the multiplication of {a} and {b} is {a * b}")
elif operation == '/':
    if a == 0 or b == 0:
        print("It is impossible to calculate a division by zero")
    else:
        print(f"the division of {a} and {b} is {a / b}")
else:
    print("Invalid operation")
