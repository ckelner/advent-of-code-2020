lines = []
with open('./input') as f:
    lines = f.read().splitlines()

match = False
for x in range(len(lines)):
    num_one = int(lines[x])
    for y in range(len(lines)):
        num_two = int(lines[y])
        if num_one + num_two == 2020:
            print(num_one * num_two)
            match = True
            break
    if match is True:
        break
