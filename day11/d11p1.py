# open and read the input file into a list of strings
input = open("day11/input.txt", "r").read().split("\n")

# Read in the input
servers = {}
for line in input:
    server, o = line.split(": ")
    outputs = o.split()
    servers[server] = outputs

# Recursive function to traverse all paths. Add to count whenever we reach destination.
def find_routes(this_server):
    global destination_server

    if this_server == destination_server:
        return 1
    
    new_routes = 0
    for next_server in servers[this_server]:
        new_routes += find_routes(next_server)
    
    return new_routes
        
# Main program - call the recursive function then print the result
this_server = "you"
destination_server = "out"
print(find_routes(this_server))
