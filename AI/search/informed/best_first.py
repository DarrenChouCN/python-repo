import heapq

from AI.search.constants import *


# Best First Search Algorithm
# The Best First Search algorithm is a heuristic search algorithm that requires a heuristic function to evaluate the priority of nodes. It uses a priority queue (open_list) to manage unvisited nodes and a set (closed_set) to track visited nodes. Each time a node is added to the queue, the nodes are sorted based on the heuristic function's value, ensuring that nodes with lower heuristic values are expanded first. When the goal node is found, the algorithm returns the path leading to the goal.

def best_first_search(graph, start, goal, coordinates, heuristic):
    open_list = [(heuristic(coordinates[start], coordinates[goal]), start, [start])]
    closed_set = set()

    while open_list:
        _, node, path = heapq.heappop(open_list)

        if node in closed_set:
            continue
        closed_set.add(node)

        if node == goal:
            return path

        for neighbor, _ in graph[node]:
            if neighbor not in closed_set:
                heapq.heappush(open_list,
                               (heuristic(coordinates[neighbor], coordinates[goal]), neighbor, path + [neighbor]))

    return None


if __name__ == '__main__':
    start = 'Arad'
    goal = 'Bucharest'
    manhattan_path = best_first_search(ROMANIA, start, goal, ROMANIA_COORDINATES, manhattan_heuristic)
    euclidean_path = best_first_search(ROMANIA, start, goal, ROMANIA_COORDINATES, euclidean_heuristic)
    chebyshev_path = best_first_search(ROMANIA, start, goal, ROMANIA_COORDINATES, chebyshev_heuristic)
    hamming_path = best_first_search(ROMANIA, start, goal, ROMANIA_COORDINATES, hamming_heuristic)
    logarithmic_path = best_first_search(ROMANIA, start, goal, ROMANIA_COORDINATES, logarithmic_heuristic)

    print("Manhattan Path:", manhattan_path)
    print("Euclidean Path:", euclidean_path)
    print("Chebyshev Path:", chebyshev_path)
    print("Hamming Path:", hamming_path)
    print("Logarithmic Path:", logarithmic_path)
