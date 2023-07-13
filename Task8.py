# To print the greatest number in given three number

def maximum(a,b,c):
    list = [a,b,c]
    return max(list)
x = int(input("Enter First number"))
y = int(input("Enter Second number"))
z = int (input("Enter Third number"))
print("maximum number is ::>"   ,maximum(x,y,z))