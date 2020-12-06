passports = []
tmp_passport = ""

with open('./input') as fp:
    for line in fp:
        # new passport if we encounter a new line
        if line == "\n" or line == "":
            passports.append(tmp_passport)
            tmp_passport = ""
        else:
            # passports can be on multiple lines, here we combine them into a single
            # string that is space delimited
            tmp_passport += " " + line.rstrip()

valid_passport_count = 0
for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and \
        "hgt" in passport and "hcl" in passport and "ecl" in passport and \
        "pid" in passport:
        valid_passport_count += 1

print("Valid passport count: {}".format(valid_passport_count))
