import re

def getValue(string, key):
    list = string.split(" ")
    value = ""
    for kv in list:
        if key in kv:
            value = kv.split(":")[1]
            break
    return value

passports = []
tmp_passport = ""

with open('./input') as fp:
    for line in fp:
        # new passport if we encounter a new line
        if line == "\n" or line == "" or not line or line == None:
            passports.append(tmp_passport)
            tmp_passport = ""
        else:
            # passports can be on multiple lines, here we combine them into a single
            # string that is space delimited
            tmp_passport += line.rstrip() + " "

# append the very last passport, we don't catch above
passports.append(tmp_passport)

valid_passport_count = 0
for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and \
        "hgt" in passport and "hcl" in passport and "ecl" in passport and \
        "pid" in passport:
        byr = getValue(passport, "byr")
        iyr = getValue(passport, "iyr")
        eyr = getValue(passport, "eyr")
        hgt = getValue(passport, "hgt")
        hcl = getValue(passport, "hcl")
        ecl = getValue(passport, "ecl")
        pid = getValue(passport, "pid")

        is_valid = True

        hgt_unit_index = hgt.find('in')
        hgt_unit = "in"
        if hgt_unit_index == -1:
            hgt_unit_index = hgt.find("cm")
            if hgt_unit_index == -1:
                is_valid = False
            else:
                hgt_unit = "cm"

        if is_valid == True:
            hgt_val = int(hgt[0:hgt_unit_index])
            if hgt_unit == "in":
                if hgt_val < 59 or hgt_val > 76:
                    is_valid = False
            else:
                if hgt_val < 150 or hgt_val > 193:
                    is_valid = False

        if is_valid == True:
            if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
                is_valid = False
            elif len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
                is_valid = False
            elif len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
                is_valid = False

        if is_valid == True:
            if hcl[0:1] != "#" or len(hcl) != 7:
                is_valid = False
            else:
                match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl)
                if match == False:
                    is_valid = False

        if is_valid == True:
            ecl_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if ecl not in ecl_values:
                is_valid = False

        if is_valid == True:
            if len(pid) != 9:
                is_valid = False
            else:
                if pid.isdecimal() == False:
                    is_valid = False

        if is_valid == True:
            valid_passport_count += 1

print("Valid passport count: {}".format(valid_passport_count))
