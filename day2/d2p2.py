# open and read the input file into a list of strings
ranges = open("day2/input.txt", "r").read().rstrip().split(",")

# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), 
# and 1111111 (1 seven times) are all invalid IDs.
def check_is_invalid(val):
    string_length = len(val)

    for pieces in range(2, string_length+1):
        # Skip over any cases where the string doesn't break evenly into pieces
        if string_length % pieces == 0:
            # Calculate how long each piece must be. So for val of "123456", pieces could be 6, 3 or 2. 
            # Or for "12345", pieces could only be 5.
            breakpoint = string_length // pieces

            # Compare that piece of the string multiplied pieces times with the original val
            if val[:breakpoint]*pieces == val:
                return True

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