# open and read the input file into a list of strings
input = open("day5/input.txt", "r").read().split("\n")

def is_fresh(ID):
    for (start, end) in fresh_ranges:
        if start <= ID <= end:
            return True
    return False

fresh_ranges = []
fresh_items = 0
for line in input:
    if line != "":
        if "-" in line:
            # If there's a - then it's a range
            range_start, range_end = line.split("-")
            fresh_ranges.append((int(range_start), int(range_end)))
        else:
            # If there's not a - then it's an inventory item ID
            if is_fresh(int(line)):
                fresh_items += 1
                print(f"Item {line} is Fresh")

print(f"Fresh items: {fresh_items}")