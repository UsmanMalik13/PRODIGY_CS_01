# Optimized Caesar Cipher Program

# Encryption/Decryption Function
def caesar_cipher(text, shift, mode):
    result = ""
    
    # Adjust the shift for decryption
    if mode == 'D':
        shift = -shift
    
    for char in text:
        if char == " ":
            result += char  # Retain spaces
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabet characters remain unchanged
    
    return result

# Main logic
def main():
    print("\n*** CAESAR CIPHER PROGRAM/ PRODIGY INFOTECH_TASK 1 ***\n")
    print("Choose an option:")
    print("1. Encrypt Text")
    print("2. Decrypt Text")

    while True:
        user_input = input('Enter E for Encrypt or D for Decrypt: ').upper()

        if user_input in ['E', 'D']:
            shift = int(input("Enter the shift value: "))  # No range validation
            text = input('Enter the text: ')
            result = caesar_cipher(text, shift, user_input)
            
            if user_input == 'E':
                print(f"\nEncrypted text: {result}")
            else:
                print(f"\nDecrypted text: {result}")
            break
        else:
            print("Invalid option. Please enter 'E' or 'D'.")

# Run the program
main()
