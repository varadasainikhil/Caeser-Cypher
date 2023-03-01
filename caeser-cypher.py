from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caeser(text, shift,direction):
    output_text=""
    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            x = alphabet.index(letter)
            if(direction == "encode"):
                shift = shift%26
                if(x+shift > len(alphabet)):
                    x = x+shift - len(alphabet)
                    output_text +=alphabet[x]
                else:
                    output_text +=alphabet[x+shift]
            else:
                if(x-shift < 0):
                    x = x-shift + len(alphabet)
                    output_text +=alphabet[x]
                else:
                    output_text +=alphabet[x-shift]
    print(f"The encoded text is {output_text}")
    
iterate = 1
while(iterate == 1):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text,shift,direction)
    cont = input("Do you want to continue ,Type yes to continue or press anything to exit: ")
    if(cont == "yes"):
        iterate = 1
    else:
        iterate = 0

