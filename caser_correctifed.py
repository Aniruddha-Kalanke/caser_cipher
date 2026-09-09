alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

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