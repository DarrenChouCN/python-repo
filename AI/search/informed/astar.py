import heapq

from AI.search.constants import *


# A* (A Star) Search Algorithm
# A* search algorithm is an informed search algorithm that combines the benefits of Dijkstra's algorithm and Greedy Best-First Search. It uses a heuristic function to estimate the cost from the current node to the goal, and it also considers the cost from the start node to the current node. This allows A* to find the optimal path to the goal while efficiently exploring the search space.

def astar_search(graph, start, goal, coordinates, heuristic):
    open_list = [(0 + heuristic(coordinates[start], coordinates[goal]), 0, start, [start])]
    closed_set = set()

    while open_list:
        _, cost, node, path = heapq.heappop(open_list)

        if node in closed_set:
            continue
        closed_set.add(node)

        if node == goal:
            return path

        for neighbor, weight in graph[node]:
            if neighbor not in closed_set:
                new_cost = cost + weight
                heapq.heappush(open_list, (
                new_cost + heuristic(coordinates[neighbor], coordinates[goal]), new_cost, neighbor, path + [neighbor]))

    return None


if __name__ == '__main__':
    start = 'Arad'
    goal = 'Bucharest'
    manhattan_path = astar_search(ROMANIA, start, goal, ROMANIA_COORDINATES, manhattan_heuristic)
    euclidean_path = astar_search(ROMANIA, start, goal, ROMANIA_COORDINATES, euclidean_heuristic)
    chebyshev_path = astar_search(ROMANIA, start, goal, ROMANIA_COORDINATES, chebyshev_heuristic)
    hamming_path = astar_search(ROMANIA, start, goal, ROMANIA_COORDINATES, hamming_heuristic)
    logarithmic_path = astar_search(ROMANIA, start, goal, ROMANIA_COORDINATES, logarithmic_heuristic)

    print("Manhattan Path:", manhattan_path)
    print("Euclidean Path:", euclidean_path)
    print("Chebyshev Path:", chebyshev_path)
    print("Hamming Path:", hamming_path)
    print("Logarithmic Path:", logarithmic_path)
