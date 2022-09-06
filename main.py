from alphavet import latters
from art import logo

def caesar (start_text, shift_amount, chiper_derection):
    end_text=""
    if chiper_derection=="decode":
        shift_amount*=-1
  
    for char in start_text:
        if char in latters:
            position=latters.index(char)
            new_position=position+shift_amount
            end_text+=latters[new_position]
        else:
            end_text+=char
    print(f"Here is {chiper_derection} result {end_text}" )

print(logo)
should_end=False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, chiper_derection=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

        