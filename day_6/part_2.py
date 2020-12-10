answers = []
tmp_answers = ""
#with open('./debug_input') as fp:
with open('./input') as fp:
    for line in fp:
        # new group if we encounter a new line
        if line == "\n" or line == "" or not line or line == None:
            answers.append(tmp_answers)
            tmp_answers = ""
        else:
            # groups answers are on multiple lines, here we combine them into a
            # single string that is space delimited
            tmp_answers += line.rstrip() + " "

# append the very last answer set, we don't catch above
answers.append(tmp_answers)

sum = 0
for answer_set in answers:
    # get the number of individuals in a group
    number_of_people = answer_set.count(" ")

    # split space delimited answer string into a list
    answer_list = answer_set.split(" ")

    # for each answer set (group) break it into individual's answers
    # for exactly one individual's answer, count each character across the whole list
    # compare
    count = 0
    for answer in answer_list:
        char_list = list(answer)
        for char in char_list:
            answer_count = answer_set.count(char)
            # debug
            #print("Number of people: {}".format(number_of_people))
            #print("Character: {}".format(char))
            #print("Number of Character: {}".format(answer_count))
            #print("")
            if answer_count == number_of_people:
                count += 1
        # we can break after the first iteration
        break

    # add everyone answered to total sum
    sum += count

# Part 2
print("Sum of questions where everyone in the group answered yes: {}".format(sum))
