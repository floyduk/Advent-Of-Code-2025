# open and read the input file into a list of strings
input = open("day4/input.txt", "r").read().split("\n")

# dx,dy values for the 8 directions
directions = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

def space_contents(x, y):
    if 0 <= y < len(input) and 0 <= x < len(input[y]):
        return input[y][x]
    else:
        return "." # Out of bounds spaces are empty

def adjacent_rolls(x, y):
    # Keep track of how many spaces around this roll contain other rolls
    adjacent_rolls = 0

    # Check in each direction
    for (dx, dy) in directions:
        if space_contents(x+dx, y+dy) == "@":
            adjacent_rolls += 1
    
    # Return the number of adjascent rolls
    return adjacent_rolls

# Count of movable rolls
movable_rolls = 0

# Look at each space and count the surrounding rolls
for y in range(len(input)):
    for x in range(len(input[y])):
        if space_contents(x, y) == "@" and adjacent_rolls(x, y) < 4:
            movable_rolls += 1

# Print the result
print(f"Movable rolls: {movable_rolls}")