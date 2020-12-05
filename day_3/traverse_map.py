def treeCount(right, down):
    horizontal_count = right
    count = 0
    tree_count = 0

    for line in massaged_lines:
        # skip first row of map
        if count is 0:
            count += 1
            continue
        else:
            if count % down == 0:
                map_space = line[horizontal_count]

                if map_space == "#":
                    tree_count += 1

                horizontal_count += right

            count += 1

    print("Number of trees for right {} down {}: {}".format(right, down, tree_count))
    return tree_count


lines = []
with open('./input') as f:
    lines = f.read().splitlines()

# kelnerhax to make map wide enough
massaged_lines = []
for input in lines:
    massaged_lines.append(input * 100)

total = treeCount(1,1) * treeCount(3,1) * treeCount(5,1) * treeCount(7,1) * treeCount(1,2)

print("Total: {}".format(total))
