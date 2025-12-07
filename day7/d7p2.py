# open and read the input file into a list of strings
input = open("day7/input.txt", "r").read().split("\n")
cols = len(input[0])

# Make an array of counts the same width as the grid and 
# set the initial beam.
beam_counts = []
for i in range(cols):
    beam_counts.append(0)
beam_counts[input[0].index("S")] += 1

# Iterate the lines in the input looking for splitters and
# where we find one take ALL the beams hitting that column
# and split them into adjascent columns.
for line_no, line in enumerate(input[2:]):
    if line_no%2 == 0:
        print(f"{line_no}")
        for i, ch in enumerate(line):
            if ch == "^":
                beam_counts[i-1] += beam_counts[i]
                beam_counts[i+1] += beam_counts[i]
                beam_counts[i] = 0

# Print the result
print(f"Number of paths: {sum(beam_counts)}")