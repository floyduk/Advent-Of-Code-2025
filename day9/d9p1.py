from itertools import combinations

# open and read the input file into a list of strings
input = open("day9/input.txt", "r").read().split("\n")

# Read the input into a list of tuples for (x, y). Calculate the sizes rectangle for all pairs of red tiles. Print the max()
print(max([abs(t1[0] - t2[0] + 1) * abs(t1[1] - t2[1] + 1) for t1, t2 in combinations([tuple([int(a) for a in line.split(",")]) for line in input], 2)]))