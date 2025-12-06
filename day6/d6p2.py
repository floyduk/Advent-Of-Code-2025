from math import prod

# open and read the input file into a list of strings
input = open("day6/input.txt", "r").read().split("\n")
rows = len(input)

# First find the blank columns
blank_column_indexes = []
for i in range(len(input[0])):
    if "".join([input[r][i] for r in range(rows)]) == (" " * rows):
        blank_column_indexes.append(i)

# Now form the sums which are a grid of chars
sums, last_col = [], 0
for bc in blank_column_indexes:
    sums.append([input[r][last_col:bc] for r in range(rows)])
    last_col = bc+1
sums.append([input[r][last_col:] for r in range(rows)])

# Now we've got a list of sums that are grids of chars. 
# We can now parse each sum according to cephalopod maths.
# This code looks down the columns in the sum (which is a grid of chars)
# and makes numbers out of each column. Then looks at the operator 
# which is always the bottom left char to perform the operation.
total = 0
for s in sums:
    numbers = []
    for c in range(len(s[0]),0,-1):
        n = int("".join([s[r][c-1] for r in range(rows-1)]))
        numbers.append(n)
    if s[rows-1][0] == "+":
        # print(f"{numbers}\nsum: {sum(numbers)}")
        total += sum(numbers)
    else:
        # print(f"{numbers}\nprod: {prod(numbers)}")
        total += prod(numbers)

# Print the answer
print(f"Total: {total}")


