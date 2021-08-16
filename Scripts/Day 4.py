from typing import ValuesView
import numpy as np
import regex as re

def first():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day4.txt") as f:
        lines = [line.replace("\n", "").split() for line in f.readlines()]
        tempLines = []
        passports = []
        for line in lines:
            if len(line) > 0:
                tempLines.extend(line)
            else:
                passports.append(tempLines)
                tempLines = []
        passports.append(tempLines)

        validPassports = 0
        for passport in passports:
            if len(passport) == 8 or (len(passport) == 7 and not any('cid:' in string for string in passport)):
                validPassports += 1
        return validPassports

def second():
    with open("/Users/cato447/Code/Cato447/AdventOfCode_2020/Scripts/res/day4.txt") as f:
        lines = [line.replace("\n", "").split() for line in f.readlines()]
        tempLines = []
        passports = []
        for line in lines:
            if len(line) > 0:
                tempLines.extend(line)
            else:
                passports.append(dict([map(str.strip, passport.split(':')) for passport in tempLines]))
                tempLines = []
        passports.append(dict([map(str.strip, passport.split(':')) for passport in tempLines]))
        
        validPassports = 0
        for passport in passports:
            if len(passport) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport.keys()):
                if validatePassport(passport):
                    validPassports += 1
                else:
                    print(passport)

        return validPassports

def validatePassport(passport):
    boundaries = {
            'byr' : [1920, 2002],
            'iyr' : [2010, 2020],
            'eyr' : [2020, 2030],
            'hgt' : {'cm' : [150, 193], 'in' : [59, 73]},
            'hcl' : '^#[a-f0-9]{6}',
            'ecl' : ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            'pid' : '[0-9]{9}'
    }
    valid = True
    for key, value in passport.items():
        if key != 'cid':
            if key == 'hgt':
                try:
                    bounds = boundaries[key][value[-2:]]
                    if not bounds[0] <= int(value[:-2]) <= bounds[1]:
                        valid = False
                        break
                except: # height has no specified unit
                    valid = False
                    break
            elif key in ['byr', 'iyr', 'eyr']:
                bounds = boundaries[key]
                try:
                    if not bounds[0] <= int(value) <= bounds[1]:
                        valid = False
                        break
                except:
                    valid = False
                    break
            elif key == 'ecl':
                if not value in boundaries[key]:
                    valid = False
                    break
            elif key in ['hcl', 'pid']: # match regex
                if not re.match(boundaries[key], value):
                    valid = False
                    break
    return valid

print(f"First solution: {first()}")
# Real solution is second() +1. Has to do something with parsing the data
print(f"Second solution: {second()}")