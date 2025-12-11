from functools import cache

# open and read the input file into a list of strings
input = open("day11/input.txt", "r").read().split("\n")

# Read in the input
servers = {}
for line in input:
    server, o = line.split(": ")
    outputs = o.split()
    servers[server] = outputs
servers["out"] = []

# Recursive function to traverse all paths. Add to count whenever we reach destination.
@cache
def find_routes(this_server, dac, fft):
    global destination_server

    new_routes = 0
    for next_server in servers[this_server]:
        new_routes += find_routes(next_server, True if this_server == "dac" else dac, True if this_server == "fft" else fft)

    if this_server == destination_server and dac and fft:
        return new_routes + 1
    else:
        return new_routes

# Main program - call the recursive function then print the result
this_server = "svr"
destination_server = "out"
print(find_routes(this_server, False, False))
