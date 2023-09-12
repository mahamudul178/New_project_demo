alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(alphabet)

while True:
    types=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if types=="encode":
        def encrypt(plain_text,shift_amount):
            cliper_text=""
            for letter in plain_text:
                position=alphabet.index(letter)
                new_position=position+shift_amount
                cliper_text=cliper_text+alphabet[new_position]
            print(f"The encode text is {cliper_text}")
        text=input("Type your message:\n").lower()
        shift=int(input("Type the shift number:\n"))
        encrypt(plain_text=text,shift_amount=shift)

    elif types=="decode":
        def decrypt(plain_text2,shift_amount2):
            cliper_text2=""
            for letter2 in plain_text2:
                position2=alphabet.index(letter2)
                new_position2=position2-shift_amount2
                cliper_text2=cliper_text2+alphabet[new_position2]
            print(f"The decode text is {cliper_text2}")

        text2=input("Cliper your message: \n").lower()
        shift2=int(input("Type the reverse shift number:\n"))
        decrypt(plain_text2=text2, shift_amount2=shift2)