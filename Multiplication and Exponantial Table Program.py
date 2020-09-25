print("Welcome to the Multiplication/Exponent Table Program")
name = input("\nHello, what is your name: ")
num = float(input("What number would you like to work with: "))
message=name+", Math is cool!"

print("\nMultiplication Table For "+str(num))
for i in range(1,10):
	print("\t"+str(i)+".0 * "+str(num)+" = "+str(round(i*num,4)))

print("\nExponent Table For "+str(num))
for i in range(1,10):
	print("\t"+str(num)+" ** "+str(i)+" = "+str(round(num**i,4)))

print("\n"+message)
print("\t"+message)
print("\t\t"+message)
print("\t\t\t"+message)
print("\t\t\t\t"+message)