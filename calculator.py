condition=True
while condition:
    def calculator_result(frist,operator,second):
        match operator:
            case '+':
                result=frist+second
                print(f"{frist} + {second} = {result} ")
            case '-':
                result=frist-second
                print(f"{frist} - {second} = {result} ")
            case '*':
                result=frist*second
                print(f"{frist} * {second} = {result} ")
            case '/':
                result=frist/second
                print(f"{frist} * {second} = {result} ")
        condition2=True
        while condition2:
            type=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculaton: " )
            operator2=input("Pick and operation: ") 
            num2=float(input("What is the next number?: "))
            if type=='y':
                match operator2:
                    case '+':
                        result2=result+num2
                        print(f"{result} + {num2} = {result2} ")
                    case '-':
                        result2=result-num2
                        print(f"{result} - {num2} = {result2} ")
                    case '*':
                        result2=result*num2
                        print(f"{result} * {num2} = {result2} ")
                    case '/':
                        result2=result/num2
                        print(f"{result} / {num2} = {result2} ")
            elif type=='n':
                condition2=False

    first_number=float(input("what is the frist number?: "))
    ope={
        "+":'addition',
        "-":'Substraction',
        "*":'Multiplication',
        "/":'Division'
    }
    for letter in ope:
        print(letter)
    operator1=input("Pick an opertor: ")
    second_number=float(input("What is the next number?: "))

    calculator_result(frist=first_number,operator=operator1,second=second_number)