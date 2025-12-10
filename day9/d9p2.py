from itertools import combinations

# Return true if any part of line is inside x1, y1, x2, y2 box
def lines_cross_box(x1, y1, x2, y2, line):
    if (line[4] == "h"):
        # Horizontal lines
        if y1 < line[1] < y2:
            for x in range(line[0], line[2]+1):
                if(x1 < x < x2):
                    return True
    else:
        # Vertical lines
        if x1 < line[0] < x2:
            for y in range(line[1], line[3]+1):
                if(y1 < y < y2):
                    return True
    return False

def is_inside_box(x1, y1, x2, y2, line):
    # Calculate the mid-point on the line
    mid_x, mid_y = line[0]+((line[2]-line[0])//2), line[1]+((line[3]-line[1])//2)
    
    # Step one space in the direction of outside
    if line[5] == "u": mid_y -= 1
    elif line[5] == "d": mid_y += 1
    elif line[5] == "l": mid_x -= 1
    elif line[5] == "r": mid_x += 1

    # Return true if that space is inside our box
    return (x1 <= mid_x <= x2) and (y1 <= mid_y <= y2)

# open and read the input file into a list of strings
input = open("day9/input.txt", "r").read().split("\n")

# Read the input into a list of tuples for (x, y).
red_tiles = [tuple([int(a) for a in line.split(",")]) for line in input]

# Findt the point nearest the top and on the right - so we know which side is outside
start_tile_y = min([t[1] for t in red_tiles])
start_tiles = [t for t in red_tiles if t[1] == start_tile_y]
start_tile_x = max(t[0] for t in start_tiles)

# Now walk the perimeter making lines that have start, end, orientation and outside
perimeter, lines, last_direction, outside = [(start_tile_x, start_tile_y)], [], "r", "u"
while red_tiles:
    if red_tiles_next := [t for t in red_tiles if t[0] > perimeter[-1][0] and t[1] == perimeter[-1][1]]:
        # Right
        if last_direction == "u": outside = "u" if outside == "l" else "d"
        else: outside = "d" if outside == "l" else "u"
        last_direction = "r"
        lines.append((perimeter[-1][0], perimeter[-1][1], red_tiles_next[0][0], red_tiles_next[0][1], "h", outside))
    elif red_tiles_next := [t for t in red_tiles if t[0] == perimeter[-1][0] and t[1] > perimeter[-1][1]]:
        # Down
        if last_direction == "r": outside = "r" if outside == "u" else "l"
        else: outside = "l" if outside == "u" else "r"
        last_direction = "d"
        lines.append((perimeter[-1][0], perimeter[-1][1], red_tiles_next[0][0], red_tiles_next[0][1], "v", outside))
    elif red_tiles_next := [t for t in red_tiles if t[0] < perimeter[-1][0] and t[1] == perimeter[-1][1]]:
        # Left
        if last_direction == "u": outside = "d" if outside == "l" else "u"
        else: outside = "u" if outside == "l" else "d"
        last_direction = "l"
        lines.append((red_tiles_next[0][0], red_tiles_next[0][1], perimeter[-1][0], perimeter[-1][1], "h", outside))
    elif red_tiles_next := [t for t in red_tiles if t[0] == perimeter[-1][0] and t[1] < perimeter[-1][1]]:
        # Up
        if last_direction == "r": outside = "l" if outside == "u" else "r"
        else: outside = "r" if outside == "u" else "l"
        last_direction = "u"
        lines.append((red_tiles_next[0][0], red_tiles_next[0][1], perimeter[-1][0], perimeter[-1][1], "v", outside))

    perimeter.append(red_tiles_next[0])
    red_tiles.remove(red_tiles_next[0])

biggest_box, biggest_box_size = (), 0
for t1, t2 in combinations(perimeter, 2):
    # Get the top left and bottom right coords of the t1, t2 box
    x1, y1, x2, y2 = min(t1[0], t2[0]), min(t1[1], t2[1]), max(t1[0], t2[0]), max(t1[1], t2[1])
    box_size = ((x2 - x1 + 1) * (y2 - y1 + 1))

    # Only bother checking for validity if it's the biggest box we've found
    if box_size > biggest_box_size:
        works = True

        # Check if any lines intersect with the box
        for line in lines:
            if lines_cross_box(x1, y1, x2, y2, line):
                works = False

        # Now check if the midpoint outside spaces on each line is inside the box
        t1_outsides = [line for line in lines if (line[0], line[1]) == t1 or (line[2], line[3])== t1]
        t2_outsides = [line for line in lines if (line[0], line[1]) == t2 or (line[2], line[3])== t2]
        if  is_inside_box(x1, y1, x2, y2, t1_outsides[0]) or \
            is_inside_box(x1, y1, x2, y2, t1_outsides[1]) or \
            is_inside_box(x1, y1, x2, y2, t2_outsides[0]) or \
            is_inside_box(x1, y1, x2, y2, t2_outsides[1]):
            works = False
            
        # If it passes all those tests then it's a valid box
        if works:
            print(f"Found box size {box_size} - {t1}-{t2}")
            biggest_box_size = box_size
            biggest_box = (t1, t2)

print(f"Biggest box {biggest_box} size: {biggest_box_size}")