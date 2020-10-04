'''
Given a string and a character. Find the first index of the character in the string
'''
def check_letter_index(text, letter):
    for index, value in enumerate(text):
        if letter == value:
            return index
    return None

text = input("Write string: ")
letter = input("Give letter: ")

print(check_letter_index(text, letter))

