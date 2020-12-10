answers = []
tmp_answers = ""
with open('./input') as fp:
    for line in fp:
        # new passport if we encounter a new line
        if line == "\n" or line == "" or not line or line == None:
            answers.append(tmp_answers)
            tmp_answers = ""
        else:
            # answers are on multiple lines, here we combine them into a
            # single string
            tmp_answers += line.rstrip()

# strip duplicates
tmp_answers = "".join(set(tmp_answers))
# append the very last answer set, we don't catch above
answers.append(tmp_answers)

yes_sum = 0
for answer_set in answers:
    yes_sum += len(answer_set)

# Part 1
print("Sum of all yes answers: {}".format(yes_sum))
