alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

dictator = """

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⡀⢉⣹⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣄⣴⠟⣿⡿⠉⣸⡟⠁⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠃⣠⣴⣄⡾⠋⣿⠁⠀⣿⣁⣠⣿⣷⠶⠟⠙⢛⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣇⣼⠟⢹⣿⠀⢠⣿⣤⣼⣿⣿⠉⠉⠙⠻⣶⡾⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠏⢿⡏⠀⣸⣿⡶⠿⠿⣤⣀⣀⣙⣿⡿⠟⠛⠋⠁⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⣼⣿⣟⠋⠙⢷⣦⣤⣬⣿⡏⠉⠉⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿
⣿⣿⡿⠛⣙⢿⣏⡈⠙⣷⣶⣶⣿⠏⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿
⣿⣿⣷⣾⣿⣧⠉⠛⠻⠿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠐⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠈⠛⠷⢶⣤⣤⣤⣤⣄⣠⣤⣤⣤⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""
print(logo)
print(dictator)

direction = input("Enter the direction to encode or decode: ").lower()
text = input("Enter the text to be: ").lower()
shift = int(input("Enter the shift number: "))


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        shifted = alphabet.index(letter) + shift
        new_shifted = shifted % 26
        cipher_text += alphabet[new_shifted]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(cipher_text, shift):
    decrypt_text = ""
    for letter in cipher_text:
        alphabet_position = alphabet.index(letter) - shift
        newly_shifted = alphabet_position % 26
        decrypt_text += alphabet[newly_shifted]
    print(f"Here is the decoded result: {decrypt_text}")

if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift=shift)
else:
    print("Invalid direction. Please type 'encode' or 'decode'.")