import random
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()\

random.shuffle(key)

# print(f"chars : {chars}")
# print(f"key : {key}")


#ENCRYPT
plain_text = input("Enter a Massage To encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"orinal massage : {plain_text} ")
print(f"encrypted massage : {cipher_text} ")

#DENCRYPT
cipher_text= input("Enter a Massage To encrypt : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted massage : {cipher_text} ")
print(f"orinal massage : {plain_text} ")