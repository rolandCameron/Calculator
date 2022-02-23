import time #Used for better text readability
import sys #used to end the program once the user is finished

def Is_Float(string): #Determines if the input is able to be turned into a float
    try:
        string = float(string)
        return True
    except:
        return False

def Is_Int(string): #Determines if the input is able to be turned into an integer
    try:
        string = int(string)
        return True
    except:
        return False

def Get_Inputs(operation): #Returns a list of all the numbers that the user wishes to input into the function
    digits = [] #Initialises the list of user inputs
    gettingLen = True #Starts the "gettingLen" loop
    while gettingLen:
        numOfNums = input("How many numbers would you like to " + operation + "? ") #Asks how many numbers the user would like to input
        if Is_Int(numOfNums): #Ensures that the input is a whole number
            gettingLen = False
            digits = Get_X_Inputs(numOfNums)
        else: #Runs if the user doesn't input a whole number
            print("Please enter an integer. (Non decimal or negative number)")
            continue #restarts the "gettingLen" loop
    return digits

def Get_X_Inputs(x):
    digits = []
    for i in range(int(x)):  # Runs "x" times
        gettingNum = True  # Starts the "gettingNum" loop
        while gettingNum:
            num = input("Enter number " + str(i + 1) + ":")
            if Is_Float(num):  # Checks that the user's input is a float
                digits.append(num)  # Adds the users input to the list of inputs
                gettingNum = False  # Ends the "gettingNum" loop
            else:  # Runs if the user hasn't entered a float
                print("Please enter a number.")
                continue
    return digits


def Add(digits): #Adds together the list that is inputed
    output = 0
    for i in digits:
        output += float(digits[int(i) - 1])
    return output

def Subtract(digits): #Subtracts the first input from the second
    return digits[0] - digits[1]

def Multiply(digits): #Multiplies together the list that is inputed
    output = 0
    for i in digits:
        output *= float(digits[int(i)])
    return output

def Divide(digits): #Divides the first number inputed by the second
    try:
        return float(digits[0])/float(digits[1])
    except:
        return "undefined, a number cannot be divided by 0"

#MAIN
while True:
    gettingOperation = True
    while gettingOperation:
        gettingOperation = False
        operator = input("What operation would you like the calculator to perform? (1 Add, 2 Subtract,3 Multiply, 4 Divide)")

        if operator == "1": #Runs if the user wants addition
            digits = Get_Inputs("add")
            print("Your answer is " + str(Add(digits)) + ".")
        elif operator == "2": #Runs if the user wants subtraction
            digits = Get_X_Inputs(2)
            print("Your answer is " + str(Subtract(digits)) + ".")
        elif operator == "3": #Runs if the user wants multiplication
            digits = Get_Inputs("multiply")
            print("Your answer is " + str(Multiply(digits)) + ".")
        elif operator == "4": #Runs if the user wants division
            digits = Get_X_Inputs(2)
            print("Your answer is {}.".format(Divide(digits)))
        else: #Runs if the input isn't a recognised operator
            print("Please enter a valid operator (" + operator + " is not valid)")
            gettingOperation = True
            continue

    if input("Move on to next equation? (y/n)").lower() == "y": #Asks the user if they want to play again
        print("\n \n \n ---------------------------------------------------------------- \n \n \n \n") #Clears the screen if they want to continue
        continue
    else: #Ends the program if the user is done
        print("Turning off...")
        time.sleep(1)
        sys.exit()