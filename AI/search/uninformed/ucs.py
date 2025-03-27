import heapq

from AI.search.constants import ROMANIA

# Uniform Cost Search (UCS) algorithm implementation
# Starting from a given point, UCS explores paths by selecting the one with the lowest accumulated cost using a priority queue. The endpoint of the chosen path is then marked as visited. This process repeats, continuously selecting the least costly unvisited node until the goal is reached or all possible paths have been explored.

def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost+weight, neighbor, path+[neighbor]))

    return None, float('inf')

if __name__ == '__main__':
    path, cost = ucs(ROMANIA, 'Arad', 'Bucharest')
    print('Path:', path)
    print('Cost:', cost)