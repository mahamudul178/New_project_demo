num=int(input("Enter the number:"))
sum=0
for i in range(num,0,-1):
    print(i, end="+")
    sum=sum+i
print(f" = {sum}")

student_height=input("Enter the number: ").split()
total_height=0
for i in ((student_height)):
    total_height=total_height+int(i)
print(total_height)

average_height=round(total_height/len(student_height))

print(average_height)

print(student_height)