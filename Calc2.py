print("The user is Required to Input Numbers: ")
num1=float(input("Enter the First Number: "))
num2=float(input("Enter the Second Number: "))

def Add(num1,num2):
    return num1+num2

def Sub(num1,num2):
    return num1-num2

def Mult(num1,num2):

    return num2*num1

def Div(num1,num2):
    if num2==0:
        return "Error Occured"

    return num1/num2

print("Addition are: ",Add(num1,num2))
print("Subtraction: ",Sub(num1,num2))
print("Mutiplication: " ,Mult(num1,num2))
print("Division: ",Div(num1,num2))