import random 
word_list=["Akon","Rifath","Mahmudul","arafat","Masud"]
chosen_word=random.choice(word_list)
print(f"passt, The solution is {chosen_word}")
display=[]
for i in range(len(chosen_word)):
        display+="_"
print(display)
end_of_game=False
while not end_of_game:
        guess=input("Guess a letter: ").lower()
        for position in range(len(chosen_word)):
                letter=chosen_word[position]
                # print(f"Current position : {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter==guess:
                        display[position]=letter
        print(display)
        
        if "_" not in display:
                end_of_game=True
                print("You win.")
