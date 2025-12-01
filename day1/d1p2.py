# open and read the input file into a list of strings
input = open("day1/input.txt", "r").read().split("\n")

# The arrow starts pointing at 50
arrow = 50
times_at_zero = 0

# Read in the input lines one by one and follow their instructions
for line in input:
    direction = line[0]
    count = int(line[1:])

    # Turning 100 in either direction MUST pass 0 once and only once - so count all those first
    times_at_zero += (count//100)
    count = count%100

    # Direction LEFT
    if direction == "L":
        # If we start above zero (there is no below) and we move past it then increment taz
        # If this lands exactly on zero then it's caught by another IF below
        if (arrow > 0) and (arrow-count) < 0:
            times_at_zero += 1
    
        # Point the arrow at the new value
        arrow = (arrow - count)%100

    # Direction RIGHT
    else:
        # Only catches cases that go BEYOND the 0 (100). Ones that land exactly on 0 are caught by the IF below
        if (arrow+count) > 100:
            times_at_zero += 1

        # Point the arrow at the new value
        arrow = (arrow + count)%100

    # If we land on 0 then increment the times_at_zero
    if (count > 0) and (arrow == 0):
        times_at_zero += 1
    
print(f"Times at zero: {times_at_zero}")