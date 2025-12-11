from itertools import permutations

# open and read the input file into a list of strings
input = open("day10/input.txt", "r").read().split("\n")

# Take a list of integers and convert it into a binary number as a string
def convert_list_to_binary(button, target_len):
    digits = []
    for i in range(target_len):
        digits.append("1" if i in button else "0")
    return "".join(digits)

# Parse the input. Ignore joltages for part 1
# Convert target_LEDs and the buttons lists into decimal numbers so we can do 
# bitwise operations on them when pressing buttons
machines = []
for line in input:
    parts = line.split()
    target_LEDs = parts.pop(0)[1:-1]
    joltages = parts.pop(-1)
    buttons = [tuple([int(a) for a in b[1:-1].split(",")]) for b in parts]
    buttons = [int(convert_list_to_binary(b, len(target_LEDs)), 2) for b in buttons]
    target_LEDs = int(target_LEDs.replace('.', '0').replace('#', '1'), 2)
    machines.append((target_LEDs, buttons))

def find_shortest_button_sequence(m):
    for buttons_pressed in range(len(m[1])):
        for button_order in permutations(m[1], buttons_pressed):
            current_LEDs = 0
            for button in button_order:
                current_LEDs = current_LEDs ^ button
            if current_LEDs == m[0]:
                # print(f"SOLUTION FOUND: {buttons_pressed}, button_order: {button_order}")
                return buttons_pressed
    
print(sum([find_shortest_button_sequence(m) for m in machines]))