from PIL import Image
#--
def show_menu():
    print("\nImage Encryption Tool")
    print("1. Encrypt using XOR")
    print("2. Decrypt using XOR")
    print("5. Exit")
    return input("Enter your choice (1-5): ")
#--
def xor_operation(image_path, key, output_path):
    """Perform XOR encryption/decryption"""
    img = Image.open(image_path)
    pixels = img.load() # creates a pixel access object
    for k in range(img.width):
        for j in range(img.height):
            r,g,b = pixels[k, j][:3] # This helps work with RGB only
            pixels[k, j] = (r^key, g^key, b^key)
    img.save(output_path)
    print(f"Operation completed. Result saved to {output_path}")
def main():
    while True:
        choice = show_menu()
        #--
        if choice == '1':  # XOR Encrypt
            image_path = input("Enter image path to encrypt: ")
            key = int(input("Enter XOR key (0-255): "))
            output_path = input("Enter output file path: ")
            xor_operation(image_path, key, output_path)
        #--
        elif choice == '2':  # XOR Decrypt
            image_path = input("Enter image path to decrypt: ")
            key = int(input("Enter XOR key (0-255): "))
            output_path = input("Enter output file path: ")
            xor_operation(image_path, key, output_path)
        #--   
        elif choice == '3':
            print("Exiting program...")
            break
        #--   
        else:
            print("Invalid choice. Please try again.")
#--
if __name__ == "__main__":
    main()
