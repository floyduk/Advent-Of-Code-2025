from math import prod

# open and read the input file into a list of strings
input = open("day6/input.txt", "r").read().split("\n")

# First just read in all the data split into values
rows = len(input)
numbers = []
for line in input:
    numbers.append(line.split())
cols = len(numbers[0])

# Now swap the direction of the data to turn it into sums
sums, total = [], 0
for i in range(cols):
    s = []
    for j in range(rows):
        if numbers[j][i] != "*" and numbers[j][i] != "+":
            s.append(int(numbers[j][i]))
        else:
            s.append(numbers[j][i])
    sums.append(s)
    
    # Now do the maths
    if s[-1] == "+":
        total += sum(s[:-1])
    else:
        total += prod(s[:-1])

# Print the answer
print(f"Total: {total}")


