print("Welcome to the Love Calculator")
name1=input("What is your name? \n")
name2=input("WWhat is there name? \n")
combine_string=name1+name2
total=0
for i in (combine_string):
    if('T'==i or 't'==i):
        total+=1
    if('R'==i or 'r'==i):
        total+=1
    if('U'==i or 'u'==i):
        total+=1
    if('E'==i or 'e'==i):
        total+=1
total1=0   
for i in (combine_string):
    if('L'==i or 'l'==i):
        total1+=1
    if('O'==i or 'o'==i):
        total1+=1
    if('V'==i or 'v'==i):
        total1+=1
    if('E'==i or 'e'==i):
        total1+=1 
love=str(total)+str(total1)
love=int(love)

if(love<10 or love>90):
    print(f"Your Score is {love}, You go together like coke and mentos.")
elif(love>=40 and love<=50):
    print(f"Your score is {love}, You are alright together.")
else:
    print(f"Your score is {love}.")