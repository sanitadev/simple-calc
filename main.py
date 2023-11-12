import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Console-based calculator function
def console_calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)

    else:
        print("Invalid Input")

# Tkinter GUI calculator
def on_click(button_value):
    current_text = entry.get()
    new_text = current_text + str(button_value)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def gui_calculator():
    root = tk.Tk()
    root.title("Simple Calculator")

    entry = tk.Entry(root, width=20, font=('Arial', 16), justify='right')
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        tk.Button(root, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    tk.Button(root, text='C', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
    tk.Button(root, text='=', width=5, height=2, command=calculate).grid(row=row_val, column=col_val + 1, columnspan=2)

    root.mainloop()

# Let the user choose between console and GUI versions
print("Choose calculator version:")
print("1. Console-based Calculator")
print("2. Tkinter GUI Calculator")

choice = input("Enter choice (1/2): ")

if choice == '1':
    console_calculator()
elif choice == '2':
    gui_calculator()
else:
    print("Invalid Input")

