import math

def getRow(row_code_list, index, lower, upper):
    row = 0
    if row_code_list[index] == "F":
        if index == 6:
            return lower
        else:
            new_upper = math.floor((upper + lower)   / 2)
            row = getRow(row_code_list, index + 1, lower, new_upper)
    else:
        if index == 6:
            return upper
        else:
            new_lower = math.ceil((upper + lower) / 2)
            row = getRow(row_code_list, index + 1, new_lower, upper)

    return row

def getSeat(seat_code_list, index, lower, upper):
    seat = 0
    if seat_code_list[index] == "L":
        if index == 2:
            return lower
        else:
            new_upper = math.floor((upper + lower)   / 2)
            seat = getSeat(seat_code_list, index + 1, lower, new_upper)
    else:
        if index == 2:
            return upper
        else:
            new_lower = math.ceil((upper + lower) / 2)
            seat = getSeat(seat_code_list, index + 1, new_lower, upper)

    return seat

lines = []
with open('./input') as f:
    lines = f.read().splitlines()

seat_ids = []
highest_seat = 0
for seat in lines:
    row_code = seat[0:7]
    row_code_list = [char for char in row_code]
    row = getRow(row_code_list, 0, 0, 127)

    seat_code = seat[7:10]
    seat_code_list = [char for char in seat_code]
    seat = getSeat(seat_code_list, 0, 0, 7)

    seat_id = (row * 8) + seat
    seat_ids.append(seat_id)
    if seat_id > highest_seat:
        highest_seat = seat_id

# part 1
print("Highest seat: {}".format(highest_seat))

seat_ids.sort() # lowest to highest - CHEATS :)
my_seat_id = 0
count = 0
last_seat_id = 0
for id in seat_ids:
    if last_seat_id == 0:
        last_seat_id = id
        continue
    if id - last_seat_id > 1:
        my_seat_id = last_seat_id + 1
        break
    last_seat_id = id

# part 2
print("My seat id: {}".format(my_seat_id))
