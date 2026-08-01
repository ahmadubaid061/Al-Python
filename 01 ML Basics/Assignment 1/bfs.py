def water_jug_bfs():
    visited = []
    queue = [((0, 0), [])]   # simple list as queue

    while len(queue) > 0:
        (x, y), path = queue.pop(0)   # dequeue (FIFO)

        if (x, y) in visited:
            continue

        visited.append((x, y))
        path = path + [(x, y)]

        # Goal condition
        if x == 2:
            return path

        # Possible moves
        next_states = [
            (4, y),  # Fill 4L
            (x, 3),  # Fill 3L
            (0, y),  # Empty 4L
            (x, 0),  # Empty 3L
            (x - min(x, 3 - y), y + min(x, 3 - y)),  # 4 → 3
            (x + min(y, 4 - x), y - min(y, 4 - x))   # 3 → 4
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))  # enqueue

    return None


print("BFS Path:")
print(water_jug_bfs())