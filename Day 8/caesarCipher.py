import art
print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    shift=shift%25
    if direction=="encode":
        cipherText=""
        for letter in text:
            if letter in alphabet:
                position=alphabet.index(letter)
                newposition=position +shift
                newletter=alphabet[newposition%26]
                cipherText+=newletter
            else:
                cipherText+=letter
        print(cipherText)
    elif direction=="decode":
        uncipherText=""
        for letter in text:
            position=alphabet.index(letter)
            newposition=position -shift
            newletter=alphabet[newposition]
            uncipherText+=newletter
        print(uncipherText)
    else:
        print("error")
    



res = True
while res:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    print("want to restart the cipher program?")
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if restart!="yes":
        res=False
