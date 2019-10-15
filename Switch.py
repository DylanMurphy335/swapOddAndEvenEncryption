#1. get input
#2. store each character into an array
#3. convert to ascii
#4. change even to odd and odd to even
#5. convert from ascii to char
#6. convert array to string
#7. print string
#1
"""
print("#1")
text = input("Enter text for encryption or decryption")

#2
print("#2")
letters = []
character = text.split()
for character in text:
    print(character)
    letters.append(character)

#3
print("#3")
i=0
while(i<len(letters)):
    letters[i] = ord(letters[i])
    print(letters[i])
    i += 1

#4
print("#4")
i=0
while(i<len(letters)):
    check = letters[i] % 2
    if(check == 0):
        letters[i] -= 1
    else:
        letters[i] += 1
    i += 1

#5
print("#5")
i=0
while(i<len(letters)):
    print(letters[i])
    letters[i] = chr(letters[i])
    print(letters[i])
    i += 1

#6
print("#6")
word = ""
i=0
while(i<len(letters)):
    word = word + letters[i]
    i += 1

print(word)
"""
def get_input(text):
    letters = []
    character = text.split()
    for character in text:
        print(character)
        letters.append(character)
    return letters

def to_ascii(letters):
    i = 0
    while (i < len(letters)):
        letters[i] = ord(letters[i])
        print(letters[i])
        i += 1
    return letters

def encrypt(letters):
    i = 0
    while (i < len(letters)):
        check = letters[i] % 2
        if (check == 0):
            letters[i] -= 1
        else:
            letters[i] += 1
        i += 1
    return letters

def to_char(letters):
    i = 0
    while (i < len(letters)):
        print(letters[i])
        letters[i] = chr(letters[i])
        print(letters[i])
        i += 1
    return letters

def concatinate(letters):
    word = ""
    i = 0
    while (i < len(letters)):
        word = word + letters[i]
        i += 1
    return word

def encrypt_input(input):
    letters = []
    letters = get_input(input)
    letters = to_ascii(letters)
    letters = encrypt(letters)
    letters = to_char(letters)
    text = concatinate(letters)
    return text
