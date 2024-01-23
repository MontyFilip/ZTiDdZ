import base64

def encrypt(text):
    return base64.b64encode(text.encode()).decode()

def decrypt(encoded_text):
    return base64.b64decode(encoded_text).decode()

# Example usage
def main():
    user_input = input("Enter the text to encrypt: ")
    
    encrypted_text = encrypt(user_input)
    decrypted_text = decrypt(encrypted_text)

    print('\n')
    print('Original Text:', user_input)
    print('Encrypted Text:', encrypted_text)
    print('Decrypted Text:', decrypted_text)

if __name__ == "__main__":
  try:
      main()
  except KeyboardInterrupt:
      print("\n\nEncryption interrupted by user.")
