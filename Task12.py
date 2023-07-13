# To print max numbers in given 3 numbers

def maximum(a,b,c):
    list = [a,b,c]
    return max(list)
x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = int(input("Enter third number"))
print("maximum number is ::>",maximum(x,y,z))

