def kruskals_algorithm(graph):

    # Step 1: Collect all unique edges
    edges = []
    seen = set()

    for node in graph:
        for weight, neighbor in graph[node]:
            edge = tuple(sorted((node, neighbor)))
            if edge not in seen:
                seen.add(edge)
                edges.append((weight, edge[0], edge[1]))

    # Step 2: Sort edges by weight
    edges.sort()

    # Step 3: Union-Find (no library)
    parent = {node: node for node in graph}
    rank   = {node: 0    for node in graph}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False  # same group → cycle
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True

    # Step 4: Pick edges greedily
    mst_edges = []
    total_weight = 0

    print("All edges sorted by weight:")
    for w, u, v in edges:
        print(f"  {u}-{v} : {w}")

    print(f"\n{'Step':<5} {'Edge':<10} {'Weight':<10} {'Cycle?':<10} {'Total Weight'}")
    print("-" * 50)

    step = 0
    for weight, u, v in edges:
        step += 1
        if union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            print(f"{step:<5} {u}-{v:<8} {weight:<10} {'No':<10} {total_weight}")
        else:
            print(f"{step:<5} {u}-{v:<8} {weight:<10} {'Yes - Skip':<10} -")

        if len(mst_edges) == len(graph) - 1:
            break

    print("-" * 50)
    print(f"\nMST Edges:")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v}  (weight: {w})")
    print(f"\nTotal MST Weight: {total_weight}")

    return mst_edges, total_weight

graph = {
    1: [(10, 2), (30, 4), (45, 5)],
    2: [(10, 1), (50, 3), (40, 5), (25, 6)],
    3: [(50, 2), (35, 5), (15, 6)],
    4: [(30, 1), (20, 6)],
    5: [(45, 1),(40, 2), (35, 3), (55, 6)],
    6: [(25, 2), (15, 3), (20, 4), (55, 5)],
}

kruskals_algorithm(graph)