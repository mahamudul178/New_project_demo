import random

stages=['''
   +----+
   |    |
   O    |
  /|\   |
  / \   |
        |
==========
''','''

   +----+
   |    |
   O    |
  /|\   |
  /     |
        |
==========
''','''
   +----+
   |    |
   O    |
  /|\   |
        |
        |
==========
''','''
   +----+
   |    |
   O    |
  /|    |
        |
        |
==========
''','''
   +----+
   |    |
   O    |
   |    |
        |
        |
==========
''','''
   +----+
   |    |
   O    |
        |
        |
        |
==========
''','''
   +----+
   |    |
        |
        |
        |
        |
==========
'''
]

word_list=["ardavrk","baboon","camel"]
chosen_word=random.choice(word_list)
word_length=len(chosen_word)

lives=6
print(f"psst, the solution is {chosen_word}.")
display=[]
for i in range(word_length):
    display+="_"
print(display)
end_of_game=False
while not end_of_game:
        guess=input("Guess a letter: ")
        for position in range(word_length):
                letter=chosen_word[position]
                if letter==guess:
                        display[position]=letter
        if guess not in chosen_word:
                lives-=1
                if lives==0:
                        end_of_game=True
                        print("you Lose")
        # print(display)
        print(f"{' '.join(display)}")    
                
        if "_" not in display:
                end_of_game=True
                print("You win.")
        print(stages[lives])
