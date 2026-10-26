
campus = {
    "Hostel": {
        "Cafeteria": 150,
        "Admin Block": 300,
        "Sports Complex": 100
    },
    "Cafeteria": {"Academic Block": 200},
    "Admin Block": {"Academic Block": 120},
    "Sports Complex": {"Academic Block": 250},
    "Academic Block": {"Library": 100},
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Sports Complex": 280,
    "Academic Block": 90,
    "Library": 0
}


def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        total += campus[current][next_node]

    return total


def get_h(path):
    return heuristic[path[-1]]


def gbfs(start, goal):
    frontier = [[start]]
    visited = []

    while len(frontier) > 0:
        frontier.sort(key=get_h)
        path = frontier.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            print("Path found by GBFS:", path)
            print("Total cost of this path:", get_g(path))
            return path

        for neighbour in campus[node]:
            if neighbour not in visited:
                frontier.append(path + [neighbour])

    print("No path found.")
    return None


gbfs("Hostel", "Library")
