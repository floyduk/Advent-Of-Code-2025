from pulp import LpProblem, LpVariable, LpInteger, LpMinimize, lpSum, LpStatus, value, PULP_CBC_CMD

def solve_integer_system_ilp(A_list, b_list, lower_bound=0):
    m = len(A_list)
    n = len(A_list[0])
    
    # ILP variables x0..xn-1
    x_vars = [LpVariable(f"x{i}", lowBound=lower_bound, cat=LpInteger) for i in range(n)]
    
    prob = LpProblem("IntegerSystem", LpMinimize)
    
    # Equality constraints
    for row, bi in zip(A_list, b_list):
        prob += lpSum(ci*xi for ci, xi in zip(row, x_vars)) == bi
    
    # Objective: minimize sum of all variables
    prob += lpSum(x_vars)
    
    status = prob.solve(PULP_CBC_CMD(msg=0))
    
    if LpStatus[status] != 'Optimal':
        return None
    
    solution = [int(value(xi)) for xi in x_vars]
    return solution

#############################################################################

# open and read the input file into a list of strings
input = open("day10/input.txt", "r").read().split("\n")

# Parse the input
machines = []
for line in input:
    parts = line.split()
    target_LEDs = parts.pop(0)[1:-1]
    joltages = [int(a) for a in parts.pop(-1)[1:-1].split(",")]
    buttons = [tuple([int(a) for a in b[1:-1].split(",")]) for b in parts]
    machines.append((joltages, buttons))

total_button_presses = 0
for m in machines:
    Y, A = m[0], []
    for i in range(len(Y)):
        values = []
        for button in m[1]:
            values.append(1 if i in button else 0)
        A.append(values)
    
    total_button_presses += sum(solve_integer_system_ilp(A, Y))

print(total_button_presses)