def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiple(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def modules(mum1,num2):
    return num1%num2

print( " select operation ")
print( " + for addition ")
print( " - for subtract ")
print( " * for multiple ")
print( " / for divide ")
print( " % for modules ")


while True:
    choice = input("choose the operation + , - , * , / , %  \n ")
    
    if choice in ("+","-","*","/","%" ):
        try:
            num1 = float(input("enter the first number "))
            num2 = float(input("enter the second number"))
        except error:
            print("invalide inplut ...... please give valide input ")
            continue
    
    
        if choice == "+":
            print(num1, "+", num2, "=",add(num1,num2))
    
        if choice == "-":
            print(num1, "+-", num2, "=",subtract(num1,num2))

        if choice == "*":
            print(num1, "*", num2, "=",multiple(num1,num2))    
        
        if choice == "/":
            print(num1, "/", num2, "=",divide(num1,num2))
        
        if choice == "%":
            print(num1, "%", num2, "=",modules(num1,num2))
            
        next_calculation = input(" could you want to do next calculation yes/no \n\n\n")
        if next_calculation == "no":
            break 
    
    else:
        print("invalide input ")