'''
A ransom note can be formed by cutting words out of a magazine to form a new
sentence. How would you figure out if a ransom note (string) can be formed from a given
magazine (string)?
'''
from collections import Counter

def check_messages(magazine_let, ransom_let):
    for key, value in ransom_let.items():
        try:
            if value > magazine_let[key]:
                return False
        except:
            return False
    return True

magazine = input("Write text from magazine: ")
ransom_msg = input("Write ransom message: ")
magazine_letters = dict(Counter(magazine))
ransom_letters = dict(Counter(ransom_msg))
print(check_messages(magazine_letters, ransom_letters))