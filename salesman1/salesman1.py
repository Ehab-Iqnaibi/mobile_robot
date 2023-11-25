# Traveling Salesman Problem (TSP)
balls_coords = {
    0: (2, 3),
    1: (1, 5),
    2: (2, 4),
    3: (7, 5),
    4: (9, 6),
    5: (8, 3),
    6: (6, 2),
    7: (4, 2),
    8: (9, 5),
    9: (1, 4),
    10: (6, 3)
}
import matplotlib.pyplot as plt

# Define the number of Tennis balls
num_balls = len(balls_coords)

# Plot the Tennis balls on a 2D plane
x_coords = [balls_coords[i][0] for i in range(num_balls)]
y_coords = [balls_coords[i][1] for i in range(num_balls)]
plt.scatter(x_coords, y_coords)

for i in range(num_balls):
    plt.annotate(str(i), (balls_coords[i][0], balls_coords[i][1]))
plt.show()

import pulp
import itertools
import math

def distance(ball1, ball2):
    x1, y1 = ball1
    x2, y2 = ball2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Define the TSP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the binary decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in balls_coords for j in balls_coords if i != j], cat='Binary')

# Define the objective function
prob += pulp.lpSum([distance(balls_coords[i], balls_coords[j]) * x[(i, j)] for i in balls_coords for j in balls_coords if i != j])

# Define the constraints
# Each ball must be visited exactly once
for i in balls_coords:
    prob += pulp.lpSum([x[(i, j)] for j in balls_coords if i != j]) == 1
    prob += pulp.lpSum([x[(j, i)] for j in balls_coords if i != j]) == 1

# Subtour elimination constraints
for k in balls_coords:
    for S in range(2, len(balls_coords)):
        for subset in itertools.combinations([i for i in balls_coords if i != k], S):
            prob += pulp.lpSum([x[(i, j)] for i in subset for j in subset if i != j]) <= len(subset) - 1

# Solve the problem using the CBC solver
prob.solve(pulp.PULP_CBC_CMD())

# Print the status of the solution
# print("Status:", pulp.LpStatus[prob.status])

# Print the optimal objective value
#print("Total distance traveled:", pulp.value(prob.objective))

# Extracting the Solution
# Extract the solution
solution = []
start_ball = 0
next_ball = start_ball
while True:
    for j in range(num_balls):
        if j != next_ball and x[(next_ball, j)].value() == 1:
            solution.append((next_ball, j))
            next_ball = j
            break
    if next_ball == start_ball:
        break

# Print the solution
print("Route:")
for i in range(len(solution)):
    print(str(solution[i][0]) + " -> " + str(solution[i][1]))

# Plot the solution on a 2D plane
for i in range(len(solution)):
    plt.plot([balls_coords[solution[i][0]][0], balls_coords[solution[i][1]][0]], [balls_coords[solution[i][0]][1], balls_coords[solution[i][1]][1]], 'k-')
for i in range(num_balls):
    plt.plot(balls_coords[i][0], balls_coords[i][1], 'ro')

    plt.annotate(str(i), (balls_coords[i][0], balls_coords[i][1]))
plt.axis('equal')
plt.show()