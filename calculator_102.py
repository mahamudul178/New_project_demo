
#addition
def add(n1,n2):
    return n1+n2

#substraction
def subtract(n1,n2):
    return n1-n2

#Multiplication
def muliply(n1,n2):
    return n1*n2

#division
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":muliply,
    "/":divide
}

num1=int(input("What is the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol=input("Pick and operation from the above line: ")
num2=int(input("What is the second number?: "))

function=operations[operation_symbol]
print(function(num1,num2))
