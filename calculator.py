print("Welcome to my Calculator project")
print("========================================================")
number1=int(input("Enter your first number: "))
number2=int(input("Enter your second number: "))
operator=input("Enter your operator: ")
if operator=="+":
    sum=number1+number2
    print(f"The sum of {number1} and {number2} is {sum}")
elif operator=="-":
    diff=number1-number2
    print(f"The difference of {number1} and {number2} is {diff}")
elif operator=="*":
    multi=number1*number2
    print(f"The multiplication of {number1} and {number2} is {multi}")
elif operator=="/":
    div=number1/number2
    print(f"The division of {number1} and {number2} is {div}")
else:
    print("Invalid operator")