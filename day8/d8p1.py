from itertools import combinations
from math import sqrt, prod

# open and read the input file into a list of strings
input = open("day8/input.txt", "r").read().split("\n")

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

# Select the n shortest connections
n = 1000
for connections in range(n):
    # Pop the shortest distance and grab the associated boxes
    b1, b2 = distances[sorted_distance_keys.pop(0)]

    # If these two boxes aren't already on the same circuit then connect them by moving box 2 onto
    # box 1's circuit together with any other boxes that were on box 2's circuit
    if circuits[b1] != circuits[b2]:
        b2c = circuits[b2]
        circuits[b2] = circuits[b1]
        for box, circuit in circuits.items():
            if circuit == b2c:
                circuits[box] = circuits[b1]

# Find the 3 largest circuits
circuit_sizes = {}
for c in circuits.values():
    circuit_sizes[c] = circuit_sizes.get(c, 0) + 1
sorted_circuit_sizes = sorted(circuit_sizes.values(), reverse=True)

# Print the result
print(f"Solution: {prod(sorted_circuit_sizes[:3])}")