alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   


def encrypt(start_text, shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")
    

def decrypt(start_text, shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")
    


continue_cipher = True

while continue_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  
    if direction == "encode":
        encrypt(start_text = text, shift_amount = shift)
    elif direction == "decode":
        decrypt(start_text = text, shift_amount = shift)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        continue_cipher = False
        print("Goodbye!")   
        
        

        