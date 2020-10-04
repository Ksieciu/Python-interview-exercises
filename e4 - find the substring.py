'''
We define the following:

String s consists of lowercase letters in the range ascii[a-z].
String x consists of lowercase letters and may also contain a single wild-card character *, that represents any one character.
Given s and x, we want to know the zero-based index of the first occurrence of x in s. For example, if s = xabcdey and x = ab*de, the index is 1.

Function Description: Complete the function firstOccurence.
The function must return an integer denoting the zero-based index of the first occurrence of string x in s.
If x is not in s return -1 instead.
firstOccurence has the following parameter(s):
s: a string of lowercase letters. x: a string of lowercase letter which may contain 1 instance of wild-card character *
'''

# suerly not the best solution, probably can do it with some loop with enumeration - will try it later

def firstOccurence(s: str, x: str):
    try:
        x1, x2 = x.split('*')
    except:
        index = s.find(x)
        return index
    x1_start = 0
    x2_start = 0
    while True:
        x1_index = s.find(x1, x1_start)
        x2_start = x1_index + len(x1) + 1
        if x1_index < 0:
            return -1
        elif s.find(x2, x2_start) == x2_start:
            return x1_index
        x1_start = x2_start

s = input("Lowercase input[a-z]: ")
x = input("String with one wild-card *: ")

print(firstOccurence(s, x))
