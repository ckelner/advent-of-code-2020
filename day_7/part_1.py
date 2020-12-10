debug = True
my_bag = "shiny gold"

rules = []
with open('./input') as f:
    rules = f.read().splitlines()

bags = []
for rule in rules:
    held_bags_arr = []

    # get the "parent" bag type, e.g. "dark olive"
    bag_type = rule[0:rule.find(" bags contain")]
    if debug:
        print(bag_type)

    # get the "child" bag type(s) (or none) as an array of arrays
    # [[type, count],[type, count], etc]
    bags_held_list = rule[rule.find("contain ") + len("contain "):-1].split(", ")
    for sub_bag in bags_held_list:
        if sub_bag.find("no other bags") == -1:
            sub_bag_count = sub_bag[0:sub_bag.find(" ")]
            sub_bag_type = sub_bag[sub_bag.find(" ") + 1:sub_bag.find(" bag")]
            held_bags_arr.append([sub_bag_type, int(sub_bag_count)])
    if debug:
        print(held_bags_arr)
        print("")

    bags.append([bag_type, held_bags_arr])

# list structure:
'''
    [
        type,
        [
            [type, count],
            [type, count]
        ]
    ]
'''
outer_bag_counter = 0 # this really doesn't work, but left it cuz fuck it
outer_bag_list = []
bags_of_shiny_gold_holding = ""
keep_going = True

while keep_going:
    last_iteration_count = outer_bag_counter
    for bag in bags:
        count = 0
        for sub_bags in bag:
            # kelnerhax crap
            if count != 0:
                for sbag in sub_bags:
                    if sbag[0].find(my_bag) != -1:
                        if bag[0] not in outer_bag_list:
                            outer_bag_counter += 1
                            outer_bag_list.append(bag[0])
                            bags_of_shiny_gold_holding += bag[0] + ","

                    for boh in outer_bag_list:
                        if sbag[0].find(boh) != -1:
                            if bag[0] not in outer_bag_list:
                                outer_bag_counter += 1
                                outer_bag_list.append(bag[0])
            count += 1

    if last_iteration_count == outer_bag_counter:
        keep_going = False

if debug:
    print(outer_bag_list)
    print("")

print("Number of bags that can contain '{}': {}".format(my_bag, len(outer_bag_list)))
