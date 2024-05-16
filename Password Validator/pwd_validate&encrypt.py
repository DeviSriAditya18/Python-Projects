import re
import string

pwd=input("Enter the Password: ")
pwd_len=len(pwd)
is_valid=False

while True:
    if pwd_len < 7 or pwd_len > 20: break
    elif not re.search('[A-Z]', pwd): break
    elif not re.search('[a-z]', pwd): break
    elif not re.search('[0-9]', pwd): break
    elif not re.search('[@#$%!]', pwd): break
    elif re.search('\\s',pwd): break
    else:
        is_valid = True
        break

def caesar(text,shift,alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:]+alphabet[:shift]

    shifted_alphabets=tuple(map(shift_alphabet,alphabets))
    final_alphabet=''.join(alphabets)
    final_shifted_alphabet=''.join(shifted_alphabets)
    table=str.maketrans(final_alphabet,final_shifted_alphabet)
    return text.translate(table)

if is_valid:
    print(f"Entered Password {pwd} is Valid...")
    print()
    print(f"Original Password: {pwd}")
    enc_pwd=caesar(pwd,5,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation])
    print(f"Encrypted Password: {enc_pwd}")
else:
    print(f"Entered Password {pwd} is NotValid...")

