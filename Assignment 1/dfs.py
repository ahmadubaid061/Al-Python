def water_jug_dfs():
    visited = []
    stack = [((0, 0), [])]   # simple list as stack

    while len(stack) > 0:
        (x, y), path = stack.pop()   # pop (LIFO)

        if (x, y) in visited:
            continue

        visited.append((x, y))
        path = path + [(x, y)]

        # Goal condition
        if x == 2:
            return path

        # Possible moves
        next_states = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (x - min(x, 3 - y), y + min(x, 3 - y)),
            (x + min(y, 4 - x), y - min(y, 4 - x))
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state, path))  # push

    return None


print("DFS Path:")
print(water_jug_dfs())