f = open("Ressources/InputDay2.txt", 'r')

input = f.readlines()

limiters = []
chars = []
passwords = []

for i in input:
    limiter, char, password = i.split(" ")
    limiters.append(limiter)
    chars.append(char[0])
    passwords.append(password.strip())

validPasswords = 0

for (password, char, limiter) in zip(passwords, chars, limiters):
    if int(limiter.split('-')[0]) <= password.count(char) <= int(limiter.split('-')[1]):
        validPasswords += 1

print(validPasswords)