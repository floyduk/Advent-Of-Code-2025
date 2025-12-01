# open and read the input file into a list of strings
input = open("day1/input.txt", "r").read().split("\n")

# The arrow starts pointing at 50
arrow = 50
times_at_zero = 0

# Read in the input lines one by one and follow their instructions
for line in input:
    direction = line[0]
    count = line[1:]

    if direction == "L":
        arrow = (arrow - int(count))%100
    else:
        arrow = (arrow + int(count))%100
    
    if arrow == 0:
        times_at_zero += 1

    print(f"Arrow: {arrow}")
    
print(f"Times at zero: {times_at_zero}")