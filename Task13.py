# Print min numbers in given 3 numbers - using ternary operator 

def minimum(a,b,c):
    list = [a,b,c]
    return min(list)
x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = int(input("Enter third number"))
print("minimum number is ::>",minimum(x,y,z))

