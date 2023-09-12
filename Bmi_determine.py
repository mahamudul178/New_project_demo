height=float(input("Enter your hight in m: "))
weight=float(input("Enter your weight in kg: "))

bmi=round(weight/(height**2),2)

if(bmi<18.5):
    print(f"Your MBI is {bmi} They are underweight")
elif(bmi>18.5 and bmi<25):
    print(f"Your MBI is {bmi}, They have a normal weight")
elif(bmi>=25 and bmi<30):
    print(f"Your MBI is {bmi} ther are overweight")
elif(bmi>=30 and bmi<35):
    print(f"Your MBI is {bmi} They are obese")
else:
    print(f"Your MBI is {bmi} They are clinically obese")
