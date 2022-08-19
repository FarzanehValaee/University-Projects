# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import *
from graphs import *
import queue as Q


def bfs(graph, start, goal):
    graph1 = {}
    for j in graph.nodes:
        neighbour1 = graph.get_connected_nodes(j)
        graph1[j] = neighbour1

    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return [start]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph1[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)


# Once you have completed the breadth-first search,
# this part should be very simple to complete.


def dfs(graph, start, goal):
    graph1 = {}
    for j in graph.nodes:
        neighbour1 = graph.get_connected_nodes(j)
        graph1[j] = neighbour1
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return [start]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph1[node]
            # go through all neighbour nodes, construct a new path and
            # insert it into first of the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.insert(0, new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)


# Now we're going to try optimal search.  The previous searches haven't
# used edge distances in the calculation.

# This function takes in a graph and a list of node names, and returns
# the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    length = 0
    for i in range(0, len(node_names) - 1):
        length = length + Graph.get_edge(graph, node_names[i], node_names[i + 1]).length
    return length


def uniform_cost_search(graph, start, goal):
    graph1 = {}
    felan = {}
    for j in graph.nodes:
        neighbour1 = graph.get_connected_nodes(j)
        for i in neighbour1:
            felan[i] = graph.get_edge(j, i).length
        graph1[j] = felan
        felan = {}

    if start not in graph1:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if goal not in graph1:
        raise TypeError(str(goal) + ' not found in graph !')
        return

    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if goal in node[1]:
            return node[1]

        cost = node[0]

        for neighbor in graph1[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + int(graph1[current][neighbor]), temp))
    raise NotImplementedError


def a_star(graph, start, goal):
    graph1 = {}
    new_graph = {}
    for j in graph.nodes:
        neighbour1 = graph.get_connected_nodes(j)
        for i in neighbour1:
            new_graph[i] = graph.get_edge(j, i).length
        graph1[j] = new_graph
        new_graph = {}

    frontier = Q.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph1[current]:
            new_cost = cost_so_far[current] + int(graph1[current][next]) + graph.get_heuristic(next, goal)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost + graph.get_heuristic(next, goal)
                priority = new_cost + graph.get_heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    i = goal
    a = []
    a.append(i)
    while j:
        j = came_from[i]
        a.insert(0, j)
        i = j
    a.remove(None)

    return a


# It's useful to determine if a graph has a consistent and admissible
# heuristic.  You've seen graphs with heuristics that are
# admissible, but not consistent.  Have you seen any graphs that are
# consistent, but not admissible?




def is_admissible(graph, goal):
    for i in graph.nodes:
        f = path_length(graph,uniform_cost_search(graph,i,goal))
        if f < graph.get_heuristic(i, goal):
            return False
    return True



def is_consistent(graph, goal):

    for i in graph.nodes:
        for neighbour in graph.get_connected_nodes(i):
            f = graph.get_edge(i,neighbour).length
            g =abs(graph.get_heuristic(i,goal) - graph.get_heuristic(neighbour,goal))
            if (f < g):
                return False
    return True


