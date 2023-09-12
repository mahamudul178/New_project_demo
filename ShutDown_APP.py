from tkinter import *
import os 

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

def re_stra():
    os.system("B")


st=Tk()
st.title("ShutDown App")
st.geometry('500x500')
st.config(bg="blue")

r_button=Button(st, text="Restart", font=("Time new Roman",20,"bold"),relief=RAISED, cursor="plus", command="restart")
r_button.place(x=150,y=40, height=60,width=150)

rt_button=Button(st, text="Restart Time", font=("Time new Roman",20,"bold"),relief=RAISED, cursor="plus",command="restart_time")
rt_button.place(x=150,y=170, height=50,width=200)

lg_button=Button(st, text="Log-Out", font=("Time new Roman",20,"bold"),relief=RAISED, cursor="plus",command="logout")
lg_button.place(x=150,y=270, height=60,width=200)

st_button=Button(st, text="ShutDown", font=("Time new Roman",20,"bold"),relief=RAISED, cursor="plus",command="shutdown")
st_button.place(x=150,y=370, height=60,width=200)

st.mainloop()


# #import tkinter module
# import tkinter as tk

# #create window
# window = tk.Tk()

# #provide size to window
# window.geometry("600x600")

# #add text label
# tk.Label(text="Hello from Educative !!!").pack()

# window.mainloop()



# import re
# email_condition="^[a-z]+[\._]? [a-z 0-9]+ [@]\w+[.]\w{2,3}$"
# user_email=input("Enter Your emial: ")
# if re.search(email_condition,user_email):
#     print("Right  Email")
# else:
#     print("Wrong Email")