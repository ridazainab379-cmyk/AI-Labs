
warehouse = {
    "Receiving": {"Aisle1": 40, "Aisle2": 70},
    "Aisle1": {"Aisle2": 30, "Packing Station": 90},
    "Aisle2": {"Packing Station": 35},
    "Packing Station": {}
}

heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0
}


def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        total += warehouse[current][next_node]

    return total


def get_h(path):
    return heuristic[path[-1]]


def get_f(path):
    return get_g(path) + get_h(path)


def a_star(start, goal):
    frontier = [[start]]
    explored = 0

    while len(frontier) > 0:
        frontier.sort(key=get_f)
        path = frontier.pop(0)
        node = path[-1]

        explored += 1

        if node == goal:
            print("Path found by A*:", path)
            print("Total cost of this path:", get_g(path))
            return path

        for neighbour in warehouse[node]:
            frontier.append(path + [neighbour])

    print("No path found.")
    return None


a_star("Receiving", "Packing Station")
