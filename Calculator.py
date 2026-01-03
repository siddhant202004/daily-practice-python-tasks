#Build a simple calculator that performs multiple operations until the user exits.

def calculator():
    
    while True:
        number1 = int(input("Enter num1: "))
        operator = input( "Enter Operator : + , - , * , / , % , ** : "  )
        
        if operator == "exit":
            print("Calculator closed Thank you  ")
            break
        
        number2 = int(input("Enter num2: "))
        if operator == "+":
            addition = number1 + number2
            print(f"Answer : {addition}")
        elif operator == "-":
            substraction = number1 - number2
            print(f"Answer : {substraction}")
        elif operator == "/":
            divide = number1 / number2
            print(f"Answer : {divide}")
        elif operator == "%":
            mod = number1 % number2
            print(f"Answer : {mod}")
        elif operator == "*":
            mult = number1 * number2
            print(f"Answer : {mult}")
        elif operator == "**":
            power = number1 ** number2
            print(f"Answer : {power}")
        else:
            print("Invalid Input: please enter the input again ") 
        
               
            
            
calculator()

