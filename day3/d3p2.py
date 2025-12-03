# open and read the input file into a list of strings
input = open("day3/input.txt", "r").read().split("\n")

# Return the index of the first, highest digit in the row. 
# Looks for 9s then looks for 8s and so on
def find_digit(line, start, end):
    for c in range(9, 0, -1):
        if str(c) in line[start:end]:
            return line.index(str(c), start, end)

# Our running total joltage
joltage_total = 0

# Read in the input lines one by one and follow their instructions
for line in input:
    # We can only choose our next battery from those to the right of this
    last_battery_index = -1
    joltage_value = ""

    # Loop for the number of batteries we need to turn on
    for batteries_needed in range(12, 0, -1):
        # Find the first digit
        this_battery_index = find_digit(line, last_battery_index + 1, len(line) - batteries_needed + 1)
        joltage_value += line[this_battery_index]
        last_battery_index = this_battery_index
    
    # Add the number we made to our running total
    joltage_total += int(joltage_value)

# Print the result                   
print(f"Total joltage: {joltage_total}")
