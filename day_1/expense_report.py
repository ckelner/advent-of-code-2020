lines = []
with open('./input') as f:
    lines = f.read().splitlines()

match_two = False
match_three = False
for x in range(len(lines)):
    num_one = int(lines[x])
    for y in range(len(lines)):
        num_two = int(lines[y])
        if num_one + num_two == 2020 and match_two is False:
            print("Two numbers: {} * {}:".format(num_one, num_two))
            print(num_one * num_two)
            match_two = True
            print("-"*20)
        for z in range(len(lines)):
            num_three = int(lines[z])
            if num_one + num_two + num_three == 2020 and match_three is False:
                print("Three numbers: {} * {} * {}:".format(num_one, num_two, num_three))
                print(num_one * num_two * num_three)
                match_three = True
    if match_two is True and match_three is True:
        break
