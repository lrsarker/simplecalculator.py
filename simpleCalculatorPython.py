# Make a Simple Calculator using Python if statement!

x = int(input("Enter 1st Number: "))
z = input("Enter Oparetor: (+, -, *, /, %) ")
y = int(input("Enter 2nd Number: "))

if z == '+':
    print('Total', x + y)
elif z == '-':
    print('Total', x - y)
elif z == '*':
    print('Total', x * y)
elif z == '/':
    print('Total', x / y)
elif z == '%':
    print('Total', x % y)
else:
    print("Operator Missing")