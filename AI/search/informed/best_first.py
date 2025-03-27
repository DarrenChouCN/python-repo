import heapq

from AI.search.constants import *

# Best First Search Algorithm
# The Best First Search algorithm is a heuristic search algorithm that requires a heuristic function to evaluate the priority of nodes. It uses a priority queue (open_list) to manage unvisited nodes and a set (closed_set) to track visited nodes. Each time a node is added to the queue, the nodes are sorted based on the heuristic function's value, ensuring that nodes with lower heuristic values are expanded first. When the goal node is found, the algorithm returns the path leading to the goal.

def best_first_search(graph, start, goal, heuristic):
    open_list = [(heuristic(start, goal)),start,[start]]

    closed_set = set()

    while open_list:
        _, node, path = heapq.heappop(open_list)

        if node in closed_set:
            continue
        closed_set.add(node)

        if node == goal:
            return path

        for neighbor,_ in graph[node]:
            if neighbor not in closed_set:
                heapq.heappush(open_list,(heuristic(neighbor,goal),neighbor,path+[neighbor]))

    return None


def main():
    start = 'Arad'
    goal = 'Sibiu'

    if start not in ROMANIA_COORDINATES or goal not in ROMANIA_COORDINATES:
        print("The coordinate information is missing！")
        return

    start_coord = ROMANIA_COORDINATES[start]
    goal_coord = ROMANIA_COORDINATES[goal]

    print("start：", start, "coordinate：", start_coord)
    print("end：", goal, "coordinate：", goal_coord)
    print()

    heuristics = [
        ('Manhattan', manhattan_heuristic),
        ('Euclidean', euclidean_heuristic),
        ('Chebyshev', chebyshev_heuristic),
        ('Hamming', hamming_heuristic),
        ('Logarithmic', logarithmic_heuristic)
    ]

    for name, func in heuristics:
        try:
            h_value = func(start_coord, goal_coord)
            print(f"{name} heuristic: {h_value}")
        except Exception as e:
            print(f"{name} heuristic error: {e}")


if __name__ == '__main__':
    main()
