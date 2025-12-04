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

# Keep running the roll finding routine until we don't find any rolls that can be removed
rolls_removed, movable_rolls = 0, 1
while movable_rolls > 0:
    movable_rolls, removed_rolls = 0, []

    # Check each space to see if it is a roll and if it is how many rolls are adjascent
    for y in range(len(input)):
        for x in range(len(input[y])):
            if space_contents(x, y) == "@" and adjacent_rolls(x, y) < 4:
                movable_rolls += 1
                removed_rolls.append((x, y))
    
    # Now we know which rolls can be removed - remove them before we go round again
    for (x, y) in removed_rolls:
        list_string = list(input[y])
        list_string[x] = "."
        input[y] = "".join(list_string)

    # Update the total rolls removed value
    rolls_removed += movable_rolls

print(f"Movable rolls: {rolls_removed}")