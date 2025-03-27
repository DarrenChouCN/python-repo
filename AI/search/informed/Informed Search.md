# Informed Search

#### Uniform Cost Search (UCS)
UCS is an uninformed search algorithm. Starting from a given point, UCS explores paths by selecting the one with the lowest accumulated cost using a priority queue. The endpoint of the chosen path is then marked as visited. This process repeats, continuously selecting the least costly unvisited node until the goal is reached or all possible paths have been explored.

---

#### 1. Why uninformed search (such as UCS) is not efficient in certain cases

Uninformed search methods, like Uniform Cost Search (UCS), rely solely on the path cost and do not utilize any information about the goal. As a result, in vast search spaces, these methods often need to explore a large number of irrelevant or redundant nodes. Although they guarantee an optimal solution, the time and memory consumption can be extremely high, leading to significant inefficiency in large-scale problems.

#### 2. How to use evaluation functions to sort nodes and expand the most promising ones first

Evaluation functions assign a numerical value to each node (for example, h(n) in Greedy Search or f(n)=g(n)+h(n) in A* Search) to guide the search process. By sorting the candidate nodes based on how likely they are to lead to the goal, the algorithm prioritizes expanding those nodes that appear to be most promising. This targeted expansion greatly reduces unnecessary search efforts.

#### 3.Distinguishing between heuristic search and traditional search

Traditional search methods (such as BFS or UCS) do not incorporate any goal-related information and perform a blind traversal, often expanding many irrelevant nodes. In contrast, heuristic search uses goal-related estimates (such as distance heuristics) to guide the search, making it more focused and efficient. In practice, this approach can significantly improve search efficiency and, in algorithms like A*, even guarantee optimal solutions.

----

### Heuristic Functions
A heuristic function can be understood as an evaluation function used to estimate the distance from the current node to the goal node. Common heuristic functions include Manhattan distance, Euclidean distance, Chebyshev distance, Hamming distance, and Logarithmic distance. The choice of heuristic function depends on the specific problem and requirements.

- Manhattan Distance: The Manhattan distance between two points is the sum of their horizontal and vertical distances. It is commonly used in urban navigation.

- Euclidean Distance: The Euclidean distance between two points is the straight-line distance between them. It is typically used for spatial distance calculations.

- Chebyshev Distance: The Chebyshev distance between two points is the maximum of their horizontal and vertical distances. It is often used for calculating distances on a chessboard.

- Hamming Distance: The Hamming distance between two equal-length strings is the minimum number of substitutions required to change one string into the other. It is commonly used in genetic algorithms.

- Logarithmic Distance: The logarithmic distance measures the logarithmic difference between two points and is generally used for assessing data similarity.

--- 
#### Best First Search

The Best First Search algorithm is a heuristic search algorithm that requires a heuristic function to evaluate the priority of nodes. It uses a priority queue (open_list) to manage unvisited nodes and a set (closed_set) to track visited nodes. Each time a node is added to the queue, the nodes are sorted based on the heuristic function's value, ensuring that nodes with lower heuristic values are expanded first. When the goal node is found, the algorithm returns the path leading to the goal.