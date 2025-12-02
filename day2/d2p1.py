# open and read the input file into a list of strings
ranges = open("day2/input.txt", "r").read().rstrip().split(",")

# Return true if the val passed in is a string made up of two identical series of chars
def check_is_invalid(val):
    string_length = len(val)
    midpoint = string_length//2
    if string_length%2 == 0:
        # Even numbers
        if val[:midpoint] == val[midpoint:]:
            return True
    else:
        # Odd numbers - can't ever be made up of two identical series of chars
        return False

# Our total of invalid IDs
invalid_id_total = 0

# Read in the input lines one by one and follow their instructions
for r in ranges:
    range_start, range_end = [int(a) for a in r.split("-")]

    # Iterate the list of values we're checking one by one and record the ones that are invalid
    for value in range(range_start, range_end+1):
        if check_is_invalid(str(value)):
            invalid_id_total += value

# Print our final result
print(f"Total of invalid IDs: {invalid_id_total}")