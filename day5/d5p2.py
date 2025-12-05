from itertools import combinations

# open and read the input file into a list of strings
input = open("day5/input.txt", "r").read().split("\n")

# Read in the ranges from the input file
fresh_ranges, new_ranges = [], set()
for line in input:
    if "-" in line:
        # If there's a - then it's a range
        [range_start, range_end] = [int(a) for a in line.split("-")]
        new_ranges.add((int(range_start), int(range_end)))        

# Iterate comparing all the ranges and combining any that overlap
# delete_ranges contains the set of ranges that were superceded
# new_ranges containts the set of new combined or unique ranges
# fresh_ranges is the working list for this set of comparisons
while set(fresh_ranges) != new_ranges:
    fresh_ranges = list(new_ranges)
    new_ranges = set()
    delete_ranges = set()

    for (r1_start, r1_end), (r2_start, r2_end) in combinations(fresh_ranges, 2):
        if((r1_start, r1_end) not in delete_ranges and (r2_start, r2_end) not in delete_ranges):
            start_inside = r2_start <= r1_start <= r2_end
            end_inside = r2_start <= r1_end <= r2_end

            if start_inside and end_inside:
                # Ranges overlap inside     r2s--r1s--r1e--r2e
                delete_ranges.add((r1_start, r1_end))
                new_ranges.add((r2_start, r2_end))

            elif r2_start >= r1_start and r2_end <= r1_end:
                # Ranges overlap outside     r1s--r2s--r2e--r1e
                delete_ranges.add((r2_start, r2_end))
                new_ranges.add((r1_start, r1_end))

            elif start_inside and not end_inside:
                # Ranges overlap right r2s--r1s--r2e--r1e
                delete_ranges.add((r1_start, r1_end))
                delete_ranges.add((r2_start, r2_end))
                new_ranges.add((r2_start, r1_end))

            elif not start_inside and end_inside:
                # Ranges overlap left r1s--r2s--r1e--r2e
                delete_ranges.add((r1_start, r1_end))
                delete_ranges.add((r2_start, r2_end))
                new_ranges.add((r1_start, r2_end))

            else:
                # Ranges do not overlap - Add both to new_ranges
                new_ranges.add((r1_start, r1_end))
                new_ranges.add((r2_start, r2_end))

    # Make sure deleted ranges are not included in the new_ranges
    new_ranges = new_ranges - delete_ranges

# Print ther result
print(f"Fresh items: {sum([end-start+1 for (start,end) in new_ranges])}")