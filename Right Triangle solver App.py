import math
print("Welcome to the Right Triangle Solver App")
num1 = float(input("\nWhat is the first leg of the triangle: "))
num2 = float(input("What is the secound leg of the triangle: "))
side=round(math.sqrt(num1**2 +num2**2),3)
area=round(0.5*num1*num2,3)
print("\nFor a triangle with legs of "+str(num1)+" and "+str(num2)+" the hypotenuse is "+str(side)+".")
print("For a triangle with legs of "+str(num1)+" and "+str(num2)+" the area is "+str(area)+".")