from re import I
from tarfile import LENGTH_NAME
import math
import time
import sys

print("Triangle Solver")

#LINE 253

global ANGLE_A
global ANGLE_B
global ANGLE_C
global SIDE_A
global SIDE_B
global SIDE_C

def Check_If_Known(value):
    if value == "x":
        return False
    else:
        return True    

def Is_Float(string):
    try:
        string=float(string)
        return True
    except:
        return False

def Get_Input(string):
    gettingInput = True
    while gettingInput:
        recieve = input("What is {}? ('x' if unknown) ".format(string).lower())
        if Check_If_Known(recieve):
            if Is_Float(recieve):
                if float(recieve) > 0:
                    return recieve
                else:
                    print("Please enter a value greater than 0. (No angles or sides can be 0 in a triangle)")
                    continue
            else:
                print("Please enter a number. (OR 'x' if unknown)")
                continue
        else:
            return recieve

def Display(string, variable):
    try:
        print("{} is {}".format(string, round(variable, 2)))
    except:
        print("{} could not be found.".format(string))

            
def Simple_Solve_Angles(angleA, angleB, angleC):

    global ANGLE_A
    global ANGLE_B
    global ANGLE_C

    angleAKnown = Check_If_Known(angleA)
    angleBKnown = Check_If_Known(angleB)
    angleCKnown = Check_If_Known(angleC)

    if angleAKnown and angleBKnown and angleCKnown:
        pass
    elif angleAKnown and angleBKnown:
        ANGLE_C = (math.pi) - angleA - angleB
    elif angleAKnown and angleCKnown:
        ANGLE_B = (math.pi) - angleA - angleC
    elif angleBKnown and angleCKnown:
        ANGLE_A = (math.pi) - angleB - angleC

def Sine_Rule_Solve(angleA, angleB, angleC, side_a, side_b, side_c):

    global SIDE_A
    global SIDE_B
    global SIDE_C 

    sineRuleRatio = "x"

    angleAKnown = Check_If_Known(angleA)
    angleBKnown = Check_If_Known(angleB)
    angleCKnown = Check_If_Known(angleC)
    side_a_known = Check_If_Known(side_a)
    side_b_known = Check_If_Known(side_b)
    side_c_known = Check_If_Known(side_c)

    if angleAKnown and side_a_known:
        sineRuleRatio = side_a / (math.sin((angleA)))
    elif angleBKnown and side_b_known:
        sineRuleRatio = side_b / (math.sin((angleB)))
    elif angleCKnown and side_c_known:
        sineRuleRatio = side_c / (math.sin((angleC)))
    else:
        pass

    if Check_If_Known(sineRuleRatio):
        if angleAKnown and not side_a_known:
            SIDE_A = sineRuleRatio * (math.sin((angleA)))
        if angleBKnown and not side_b_known:
            SIDE_B = sineRuleRatio * (math.sin((angleB)))
        if angleCKnown and not side_c_known:
            SIDE_C = sineRuleRatio * (math.sin((angleC)))
        
def Inverse_Sine_Rule_Solve(angleA, angleB, angleC, side_a, side_b, side_c):

    global ANGLE_A
    global ANGLE_B
    global ANGLE_C

    inverseSineRuleRatio = "x"

    angleAKnown = Check_If_Known(angleA)
    angleBKnown = Check_If_Known(angleB)
    angleCKnown = Check_If_Known(angleC)
    side_a_known = Check_If_Known(side_a)
    side_b_known = Check_If_Known(side_b)
    side_c_known = Check_If_Known(side_c)

    if angleAKnown and side_a_known:
        inverseSineRuleRatio = (math.sin(angleA)) / side_a
    elif angleBKnown and side_b_known:
        inverseSineRuleRatio = (math.sin(angleB)) / side_b
    elif angleCKnown and side_c_known:
        inverseSineRuleRatio = (math.sin(angleC)) / side_c
    else:
        pass
    
    if Check_If_Known(inverseSineRuleRatio):
        if side_a_known and not angleAKnown:
            ANGLE_A = math.asin(inverseSineRuleRatio * side_a)
        if side_b_known and not angleBKnown:
            ANGLE_B = math.asin(inverseSineRuleRatio * side_b)
        if side_c_known and not angleCKnown:
            ANGLE_C = math.asin(inverseSineRuleRatio * side_c)

def Cosine_Rule_Solve(angleA, angleB, angleC, side_a, side_b, side_c):

    global SIDE_A
    global SIDE_B
    global SIDE_C 

    angleAKnown = Check_If_Known(angleA)
    angleBKnown = Check_If_Known(angleB)
    angleCKnown = Check_If_Known(angleC)
    side_a_known = Check_If_Known(side_a)
    side_b_known = Check_If_Known(side_b)
    side_c_known = Check_If_Known(side_c)

    if side_a_known and side_b_known and angleCKnown:
        if not side_c_known:
            SIDE_C = math.sqrt(side_a**2 + side_b**2 - 2*side_a*side_b*math.cos(angleC))
    if side_a_known and side_c_known and angleBKnown:
        if not side_b_known:
            SIDE_B = math.sqrt(side_a**2 + side_c**2 - 2*side_a*side_c*math.cos(angleB))
    if side_b_known and side_c_known and angleAKnown:
        if not side_c_known:
            SIDE_A = math.sqrt(side_b**2 + side_c**2 - 2*side_b*side_c*math.cos(angleA))

def Inverse_Cosine_Rule_Solve(angleA, angleB, angleC, side_a, side_b, side_c):

    global ANGLE_A
    global ANGLE_B
    global ANGLE_C

    angleAKnown = Check_If_Known(angleA)
    angleBKnown = Check_If_Known(angleB)
    angleCKnown = Check_If_Known(angleC)
    side_a_known = Check_If_Known(side_a)
    side_b_known = Check_If_Known(side_b)
    side_c_known = Check_If_Known(side_c)

    if side_a_known and side_b_known and side_c_known:
        if not angleAKnown:
            ANGLE_A = math.acos((side_b**2 + side_c**2 - side_a**2)/(2*side_b*side_c))
        if not angleBKnown:
            ANGLE_B = math.acos((side_a**2 + side_c**2 - side_b**2)/(2*side_a*side_c))
        if not angleCKnown:
            ANGLE_C = math.acos((side_a**2 + side_b**2 - side_c**2)/(2*side_a*side_b))

def Eval_Angles(angleA, angleB, angleC):

    angleAKnown = Check_If_Known(angleA)
    angleBKnown = Check_If_Known(angleB)
    angleCKnown = Check_If_Known(angleC)

    if angleAKnown and angleBKnown and angleCKnown:
        if angleA + angleB + angleC == (math.pi):
            return True
        else:
            print("These angles are impossible in a triangle. All the interior angles of a triangle must add to 180.")
            return False
    else:
        return True

def Eval_Sides(side_a, side_b, side_c):
    side_a_known = Check_If_Known(side_a)
    side_b_known = Check_If_Known(side_b)
    side_c_known = Check_If_Known(side_c)

    if side_a_known and side_b_known and side_c_known:
        if side_a + side_b < side_c:
            print("Two sides of a triangle's length cannot add to less than the length of the third side, or the edges would never meet.")
            return False
        elif side_a + side_c < side_b:
            print("Two sides of a triangle's length cannot add to less than the length of the third side, or the edges would never meet.")
            return False
        elif side_b + side_c < side_a:
            print("Two sides of a triangle's length cannot add to less than the length of the third side, or the edges would never meet.")
            return False
        else:
            return True
    else:
        return True

while True:
    gettingAng = True
    while gettingAng:
        print("Please enter all angles in degrees.\n")

        ANGLE_A = Get_Input("angle A")

        ANGLE_B = Get_Input("angle B")

        ANGLE_C = Get_Input("angle C")

        if Eval_Angles(ANGLE_A, ANGLE_B, ANGLE_C):
            gettingAng = False
        else:
            continue
    gettingSides = True
    while gettingSides:
        print("Please enter all lengths with the same unit of measurement.")

        SIDE_A = Get_Input("side a")

        SIDE_B = Get_Input("side b")

        SIDE_C = Get_Input("side c")

        if Eval_Sides(SIDE_A, SIDE_B, SIDE_C): #TRYING TO ENSURE WE RECIEVE ATLEAST ONE SIDE, NOTIFY THE USER IF WE DON'T
            gettingSides = False
        else:
            continue

    for i in range(2):
        Sine_Rule_Solve(ANGLE_A, ANGLE_B, ANGLE_C, SIDE_A, SIDE_B, SIDE_C)
        
        Inverse_Sine_Rule_Solve(ANGLE_A, ANGLE_B, ANGLE_C, SIDE_A, SIDE_B, SIDE_C)
        
        Cosine_Rule_Solve(ANGLE_A, ANGLE_B, ANGLE_C, SIDE_A, SIDE_B, SIDE_C)

        Inverse_Cosine_Rule_Solve(ANGLE_A, ANGLE_B, ANGLE_C, SIDE_A, SIDE_B, SIDE_C)

        Simple_Solve_Angles(ANGLE_A, ANGLE_B, ANGLE_C)

    Display("Angle A", math.degrees(ANGLE_A))
    Display("Angle B", math.degrees(ANGLE_B))
    Display("Angle C", math.degrees(ANGLE_C))

    Display("Side a", SIDE_A)
    Display("Side b", SIDE_B)
    Display("Side c", SIDE_C)

    time.sleep(1)

    if input("Would you like to solve another equation (y/n) ").lower() == "y":
        print("Starting again...")
        time.sleep(1)
    else:
        print("Shutting down...")
        time.sleep(1)
        sys.exit()

    print("\n \n \n \n --------------------------------------------------------------- \n \n \n \n ")