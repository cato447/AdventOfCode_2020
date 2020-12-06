f = open("Ressources/Test.txt", 'r')

input = ""

for line in f:
    if not line.isspace():
        input += line
    else:
        input += 'ü'

input = input.replace("\n", "")

passports = input.split('ü')

requiered = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

minValueCm = ["1920", "2010", "2020", "150", "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", "amb blu brn gry grn hzl oth", "^0\d{8}$"]
maxValueIn = ["2002", "2020", "2030", "193", "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", "amb blu brn gry grn hzl oth", "^0\d{8}$"]
minValueIn = ["1920", "2010", "2020", "59", "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", "amb blu brn gry grn hzl oth", "^0\d{8}$"]
maxValueIn = ["2002", "2020", "2030", "76", "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", "amb blu brn gry grn hzl oth", "^0\d{8}$"]

minValueCmDict = dict(zip(requiered, minValueCm))
maxValueInDict = dict(zip(requiered, maxValueIn))
minValueInDict = dict(zip(requiered, minValueIn))
maxValueInDict = dict(zip(requiered, maxValueIn))


valid = 0

for passport in passports:
    matches = 0
    
    keys = passport.split

    # for requierdInfo in requiered:
    #     if requierdInfo in passport:
    #         matches += 1
    # if matches == len(requiered):
    #     valid += 1

print(valid)