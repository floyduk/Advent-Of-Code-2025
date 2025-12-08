from itertools import combinations
from math import sqrt

# open and read the input file into a list of strings
input = open("day8/input.txt", "r").read().split("\n")
box_count = len(input)

# Import all the juntion box locations
boxes, circuits = [], {}
for i, line in enumerate(input):
    x, y, z = [int(n) for n in line.split(",")]
    boxes.append((x, y, z))
    circuits[(x, y, z)] = i

# Calculate the distances between all the combinations of boxes
distances = {}
for b1, b2 in combinations(boxes, 2):
    distance = sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2)
    distances[distance] = (b1, b2)

# Make a sorted list of the distances lowest to highest
sorted_distance_keys = sorted(distances.keys())

# Keep connecting until there's box_count-1 connections which is enough for them all to be on the same circuit
connections = 0
while connections < (box_count-1):
    # Pop the shortest distance and grab the associated boxes
    b1, b2 = distances[sorted_distance_keys.pop(0)]

    # If these two boxes aren't already on the same circuit then connect them by moving box 2 onto
    # box 1's circuit together with any other boxes that were on box 2's circuit
    if circuits[b1] != circuits[b2]:
        b2c = circuits[b2]
        connections += 1
        circuits[b2] = circuits[b1]
        for box, circuit in circuits.items():
            if circuit == b2c:
                circuits[box] = circuits[b1]

# Print the result
print(f"X-coordinates of last 2 boxes {b1[0]}, {b2[0]} Product is: {b1[0] * b2[0]}")