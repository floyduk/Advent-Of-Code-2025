# open and read the input file into a list of strings
input = open("day7/input.txt", "r").read().split("\n")

# Iterate the input skipping over odd numbered lines
split_count, beams = 0, set([input[0].index("S")])
for line_no, line in enumerate(input[2:]):
    if line_no%2 == 0:
        for i, ch in enumerate(line):
            if ch == "^" and i in beams:    
                # If we find a splitter and there's a beam hitting it then split it
                split_count += 1
                beams.remove(i)
                beams.add(i-1)
                beams.add(i+1)

# Print the result
print(f"Number of beams: {len(beams)} Split count: {split_count}")