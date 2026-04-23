Problem Statement: 
The task is to design an optimal path for a robot, navigating through five designated locations (tennis balls), while considering the return journey to the starting point while minimizing the 
total distance traveled. The problem is commonly known as the Travelling Salesman Problem (TSP), further complicated by the presence of a known obstacle that must be circumvented. 
Method: 
The problem is mathematically formulated as a symmetric TSP with an obstacle, modeled as an undirected weighted graph. Each tennis ball represents a vertex, and edges denote the paths 
between them, with associated weights representing distances. The TSP is solved using a mixed-integer linear programming (MILP) model and the CBC solver. 
To address the obstacle, the algorithm checks for intersections between the optimal path and the obstacle. If intersections are found, a new point is strategically added to the path, allowing 
the robot to avoid the obstacle. The TSP is then solved again with the updated coordinates. 

<img width="640" height="480" alt="output1_without_obstacle" src="https://github.com/user-attachments/assets/b0f6ff79-a8c9-479f-a291-70f41d8a0932" />

<img width="640" height="480" alt="output1_with_obstacle" src="https://github.com/user-attachments/assets/30c54c6f-11ee-4d91-9fd1-2257ac76cb1c" />
