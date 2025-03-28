from collections import deque

STUDENT_ID = 'a1960564'
DEGREE = 'PG'


class MapGraph:
    def __init__(self, map_text):
        self.parse_map(map_text)

    def parse_map(self, map_text):
        lines = map_text.strip().split("\n")

        # parse the first line for rows and columns
        self.rows, self.cols = map(int, lines[0].split())

        # parse the second and third lines for start and end coordinates
        # subtract 1 to convert to 0-indexed
        self.start = tuple(map(lambda x: int(x) - 1, lines[1].split()))
        self.end = tuple(map(lambda x: int(x) - 1, lines[2].split()))

        # parse the grid
        self.grid = [line.split() for line in lines[3:]]

        # parse the grid to adjacency list
        self.adjacency_list = self.build_adjacency_list()

    def build_adjacency_list(self):
        adjacency_list = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "X":
                    continue

                neighbors = []
                for r, c in directions:
                    neighbor_row, neighbor_col = row + r, col + c
                    if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols and self.grid[neighbor_row][
                        neighbor_col] != "X":
                        neighbors.append((neighbor_row, neighbor_col))

                adjacency_list[(row, col)] = neighbors

        return adjacency_list



# pseudocode
# problem equals a map, need to parse to MapGraph
# function GRAPH-SEARCH (problem, fringe) returns a solution, or failure
#     closed <- an empty set
#     fringe <- INSERT(MAKE-NODE(INITIAL-STATE[problem]), fringe)
#     loop do
#         if fringe is empty then return failure
#         node <- REMOVE-FRONT(fringe)
#         if GOAL-TEST(problem, STATE[node]) then return node
#         if STATE[node] is not in closed then
#             add STATE[node] to closed
#             fringe <- INSERTALL(EXPAND(node, problem), fringe)
#     end

# Breadth First Search (BFS)
def bfs(problem, fringe=None):
    # Parse the problem into a graph
    graph = MapGraph(problem)
    closed = set()
    if fringe is None:
        fringe = deque([graph.start])

    while fringe:
        node = fringe.popleft()
        # print(node)

        if node == graph.end:
            return node

        if node not in closed:
            closed.add(node)
            for neighbor in graph.adjacency_list.get(node, []):
                fringe.append(neighbor)

    return None


problem = """10 10
1 1
10 10
1 1 1 1 1 1 4 7 8 X
1 1 1 1 1 1 1 5 8 8
1 1 1 1 1 1 1 4 6 7
1 1 1 1 1 X 1 1 3 6
1 1 1 1 1 X 1 1 1 1
1 1 1 1 1 1 1 1 1 1
6 1 1 1 1 X 1 1 1 1
7 7 1 X X X 1 1 1 1
8 8 1 1 1 1 1 1 1 1
X 8 7 1 1 1 1 1 1 1"""

if __name__ == '__main__':
    # Test BFS
    result = bfs(problem)
    if result:
        print("Path found:", result)
    else:
        print("No path found")

# A* Search (A*)
