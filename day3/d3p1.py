# open and read the input file into a list of strings
input = open("day3/input.txt", "r").read().split("\n")

# Return the index of the first, highest digit in the row. 
# Looks for 9s then looks for 8s and so on
def find_digit(line):
    for c in range(9, 0, -1):
        if str(c) in line:
            return line.index(str(c))

# Our running total joltage
joltage_total = 0

# Read in the input lines one by one and follow their instructions
for line in input:
    # Find the first digit
    first_char_index = find_digit(line[:-1])
    
    # Find the second digit
    second_char_index = find_digit(line[first_char_index + 1:]) + first_char_index + 1

    # Add the number we made to our running total
    joltage_total += int(line[first_char_index] + line[second_char_index])

# Print the result                   
print(f"Total joltage: {joltage_total}")
