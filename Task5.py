# To print even or odd for a given number from CMD/CLA

num=int(input("Enter a number"))
if(num % 2) == 0:
    print("{0}is Even number".format(num))
else:
    print("{0}is Odd number".format(num))