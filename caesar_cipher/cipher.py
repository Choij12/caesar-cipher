import re
from caesar_cipher.corpus import names_list, words_list

char = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plain,key):
    encrypted_text = ""
 
    for i in range(len(plain)):
        char = plain[i]
 
        if (char.isupper()):
          encrypted_text += chr((ord(char) + key-65) % 26 + 65)
 
        elif (char.islower()):
          encrypted_text += chr((ord(char) + key - 97) % 26 + 97)

        elif char == " ":
          encrypted_text += char

        else:
          encrypted_text += char

 
    return encrypted_text
 
def decrypt(encrypted, key):
    return encrypt(encrypted, -key)

def crack(encrypted):
  for i in range(26):
      word_count = 0
      words = encrypt(encrypted, i)
      list = words.split()
      for text in list:
          if text in names_list or text.lower() in words_list:
              word_count += 1
      
      if (word_count/len(list)) > .5:
          return " ".join(list)

  return ""


