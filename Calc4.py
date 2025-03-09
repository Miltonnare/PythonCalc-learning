def Add(num1,num2):
    return num1*num2

def Sub(num1,num2):
    return num1-num2
def Mult(num1,num2):
    return num1*num2
def Div(num1,num2):
    if num2==0:
        return "Num2 should not be 0"
    return num1/num2

def Calc():
    print("Perform the Calculations: ")
    num1Input=float(input("Enter Num1: "))
    operator=(input("Enter Operator: "))
    num2Input=float(input("Enter Num2: "))
    if operator =="+":
        print("Result: ",Add(num1Input,num2Input))
    elif operator =="-":
        print("Result: ",Sub(num1Input,num2Input))
    elif operator =="*":
        print("Result: ",Mult(num1Input,num2Input))
    elif operator=="/":
       print("Result: ",Div(num1Input,num2Input))
    else:
        print("Enter a Valid Operator")
Calc()

while True:
    print("Do you want to proceed with the Calcualtions?")
    inputQ=input("Yes or No: ").strip().lower()
    if inputQ =="yes":
        # print("Debugging", inputQ)343
        Calc()
    elif inputQ=="no":
        break
    else:
        print("Invalid Input!! Please type YES OR NO ")
        

        
