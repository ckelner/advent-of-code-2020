def getCountLetterString(input):
    # get range
    space_index = input.find(" ")
    range = input[0:space_index]
    hyphen_index = input.find("-")
    start = range[0:hyphen_index]
    end = range[hyphen_index + 1:]

    # get letter
    colon_index = input.find(":")
    letter = input[space_index + 1:colon_index]

    # get password string
    password = input[colon_index + 1:]

    # Debug
    #print("Range: {} to {}; Letter: {}; Password: {}".format(start, end, letter, password))
    return [int(start), int(end), letter, password]

lines = []
with open('./input') as f:
    lines = f.read().splitlines()

valid_pass_count = 0
for input in lines:
    count_letter_string = getCountLetterString(input)
    start = count_letter_string[0]
    end = count_letter_string[1]
    letter = count_letter_string[2]
    password = count_letter_string[3]

    first_letter = password[start]
    second_letter = password[end]

    if first_letter is letter and second_letter is not letter:
        valid_pass_count += 1
    elif first_letter is not letter and second_letter is letter:
        valid_pass_count += 1

print("There are {} valid passwords".format(valid_pass_count))
