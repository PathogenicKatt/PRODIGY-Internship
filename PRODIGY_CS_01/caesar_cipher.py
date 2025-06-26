# I have to create a python program that can encrypt and decrypt text using the Caesar Cipher algorithm.
# It should allow users to input a message and a shift value to perform encryption and decryption.

def caesar_cipher(text, shift, mode='encrypt'):
  result = ""
  for char in text:
      if char.isalpha():  # Only process letters
          # Convert letter to 0-25 (A=0, B=1, etc.)
          x = ord(char.upper()) - ord('A')
          # Apply encryption/decryption formula
          if mode == 'encrypt':
              shifted = (x + shift) % 26
          elif mode == 'decrypt':
              shifted = (x - shift) % 26
          # Convert back to a letter
          new_char = chr(shifted + ord('A'))
          # Preserve original case
          result += new_char.lower() if char.islower() else new_char
      else:
          result += char  # Leave non-letters unchanged
  return result
#---
if __name__ == "__main__":
  text = input("Enter the text: ")
  shift = int(input("Enter the shift value: "))
  result = caesar_cipher(text, shift, mode='encrypt')
  print("Encrypted text:", result)
    # Uncomment the following lines to test decryption
  #result = caesar_cipher(text, shift, mode='decrypt')
  #print("Decrypted text:", result)
