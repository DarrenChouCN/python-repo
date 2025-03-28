# constants.py
import math

ROMANIA = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

ROMANIA_COORDINATES = {
    'Arad': (46.1833, 21.3167),
    'Zerind': (46.6167, 21.5167),
    'Oradea': (47.0667, 21.9333),
    'Timisoara': (45.7597, 21.2300),
    'Lugoj': (45.6886, 21.9031),
    'Mehadia': (44.9041, 22.3645),
    'Drobeta': (44.6369, 22.6597),
    'Sibiu': (45.7972, 24.1519),
    'Rimnicu Vilcea': (45.1000, 24.3667),
    'Craiova': (44.3167, 23.8000),
    'Fagaras': (45.8416, 24.9731),
    'Pitesti': (44.8565, 24.8692),
    'Bucharest': (44.4328, 26.1043),
    'Giurgiu': (43.9000, 25.9667),
    'Urziceni': (44.7167, 26.6333),
    'Hirsova': (44.6833, 27.9500),
    'Eforie': (44.0667, 28.6333),
    'Vaslui': (46.6333, 27.7333),
    'Iasi': (47.1622, 27.5889),
    'Neamt': (46.9759, 26.3819)
}


def manhattan_heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def euclidean_heuristic(node, goal):
    return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5


def chebyshev_heuristic(node, goal):
    return max(abs(node[0] - goal[0]), abs(node[1] - goal[1]))


def hamming_heuristic(node, goal):
    return sum(el1 != el2 for el1, el2 in zip(node, goal))


def logarithmic_heuristic(node, goal):
    return abs(math.log(node[0]) - math.log(goal[0])) + abs(math.log(node[1]) - math.log(goal[1]))
