f = open("Ressources/InputDay2.txt", 'r')

input = f.readlines()

indexes = []
chars = []
passwords = []

for i in input:
    index, char, password = i.split(" ")
    indexes.append(index)
    chars.append(char[0])
    passwords.append(password.strip())

validPasswords = 0

for (password, char, index) in zip(passwords, chars, indexes):
    if (password[int(index.split('-')[0])-1] == char) ^ (password[int(index.split('-')[1])-1] == char):
        validPasswords += 1

print(validPasswords)