'''
1. make a for loop and put a variable in.
2. keep the first letter uncaptitalized.
3. replace the vowels with something.
'''

def print_other_letter(statement):
    a_str = ''
    cap = False
    for letter in statement:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            if cap:
                a_str += letter.upper()
                cap = False
            else:
                a_str += letter.lower()
                cap = True
        else:
            a_str += letter
    print(a_str)
    return a_str
print_other_letter(input("Enter something here: "))

def rep_vowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "#")
    a_str = ''
    cap = False
    for letter in string:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            if cap:
                a_str += letter.upper()
                cap = False
            else:
                a_str += letter.lower()
                cap = True
        else:
            a_str += letter
    print(a_str)
    print(string)
    return string
rep_vowel(input("Enter one more time: "))

def check_parentheses(my_string):
    brackets = ['()']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string
   
# Driver code
string2 = input("Enter one last time: ")
if check_parentheses(string2):
    print("Balanced: " + "True")
else:
    print("Balanced: " + "False")
a_str = ''
cap = False
for letter in string2:
    if letter in "abcdefghijklmnopqrstuvwxyz":
        if cap:
            a_str += letter.upper()
            cap = False
        else:
            a_str += letter.lower()
            cap = True
    else:
        a_str += letter
