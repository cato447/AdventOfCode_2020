f = open("Ressources/InputDay4.txt", 'r')

input = ""

for line in f:
    if not line.isspace():
        input += line
    else:
        input += 'ü'

input = input.replace("\n", "")

passports = input.split('ü')

requiered = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid = 0

for passport in passports:
    matches = 0
    for requierdInfo in requiered:
        if requierdInfo in passport:
            matches += 1
    if matches == len(requiered):
        valid += 1

print(valid)