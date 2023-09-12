print("Welcome to python Pizzz Deleveries!")

size=input("what size pizza so you want? S, M, OR , L: ")
add_perperoni=input("Do you want to pepperoni? Y or N: ")
extra_chess= input("Do you want extra chess? Y or N: ")

small_pizza=15
mudium_pizza=20
large_pizza=25

perperoni_small=2
perperoni_medium_large=3

extra=1

if (size=='L'):
    large_pizza=25
    if(add_perperoni=='Y'):
        perperoni_medium_large=3
        if(extra_chess=='Y'):
            extra=1
            bill=(large_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
        elif(extra_chess=='N'):
            extra=0
            bill=(large_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
    elif(add_perperoni=='N'):
        perperoni_medium_large=0
        if(extra_chess=='Y'):
            extra=1
            bill=(large_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
        elif(extra_chess=='N'):
            extra=0
            bill=(large_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
elif(size=='M'):
    mudium_pizza=20
    if(add_perperoni=='Y'):
        perperoni_medium_large=3
        if(extra_chess=='Y'):
            extra=1
            bill=(mudium_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
        elif(extra_chess=='N'):
            extra=0
            bill=(mudium_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
    elif(add_perperoni=='N'):
        perperoni_medium_large=0
        if(extra_chess=='Y'):
            extra=1
            bill=(mudium_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
        elif(extra_chess=='N'):
            extra=0
            bill=(mudium_pizza+perperoni_medium_large+extra)
            print(f"Your final bill is $: {bill}")
elif(size=='S'):
    small_pizza=15
    if(add_perperoni=='Y'):
        perperoni_small=2
        if(extra_chess=='Y'):
            extra=1
            bill=(small_pizza+perperoni_small+extra)
            print(f"Your final bill is $: {bill}")
        elif(extra_chess=='N'):
            extra=0
            bill=(small_pizza+perperoni_small+extra)
            print(f"Your final bill is $: {bill}")
    elif(add_perperoni=='N'):
        perperoni_small=0
        if(extra_chess=='Y'):
            extra=1
            bill=(small_pizza+perperoni_small+extra)
            print(f"Your final bill is $: {bill}")
        elif(extra_chess=='N'):
            extra=0
            bill=(small_pizza+perperoni_small+extra)
            print(f"Your final bill is $: {bill}")