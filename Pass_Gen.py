import random
import string

def gen_pass(length, use_upper=True, use_num=True, use_spe_char=True):
    char_pool = string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_num:
        char_pool += string.digits 
    if use_spe_char:
        char_pool += string.punctuation 
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_num = input("Include numbers? (y/n): ").lower() == 'y'
        use_spe_char = input("Include special characters? (y/n): ").lower() == 'y'
        password = gen_pass(length, use_upper, use_num, use_spe_char)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
