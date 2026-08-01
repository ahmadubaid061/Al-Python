def prims_algorithm(graph, start):
    visited = []
    mst_edges = []
    total_weight = 0

    visited.append(start)

    print(f"Starting Prim's Algorithm from node: {start}\n")
    print(f"{'Step':<5} {'Edge':<12} {'Weight':<8} {'Total Weight'}")
    print("-" * 45)

    # We need to visit all nodes (total nodes - 1 edges in MST)
    while len(visited) < len(graph):
        min_weight = None
        min_edge = None

        # Look at all visited nodes
        for node in visited:
            # Check all their neighbors
            for weight, neighbor in graph[node]:
                # Only consider unvisited neighbors
                if neighbor not in visited:
                    if min_weight is None or weight < min_weight:
                        min_weight = weight
                        min_edge = (node, neighbor, weight)

        # Add the cheapest edge found
        if min_edge:
            u, v, w = min_edge
            visited.append(v)
            mst_edges.append(min_edge)
            total_weight += w
            print(f"{len(mst_edges):<5} {u}-{v:<10} {w:<8} {total_weight}")

    print("-" * 45)
    print(f"\nMST Edges:")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v}  (weight: {w})")
    print(f"\nTotal MST Weight: {total_weight}")

    return mst_edges, total_weight


# ── Graph from the image ──────────────────────────
graph = {
    'A': [(14, 'B'), (8, 'G'), (21, 'F')],
    'B': [(14, 'A'), (26, 'H'), (13, 'F'), (14, 'D'), (15, 'C')],
    'C': [(15, 'B'), (12, 'D')],
    'D': [(12, 'C'), (14, 'B'), (10, 'E'), (12, 'F')],
    'E': [(10, 'D'), (10, 'F'), (14, 'G')],
    'F': [(21, 'A'), (13, 'B'), (12, 'D'), (10, 'E')],
    'G': [(7, 'H'),(8, 'A'), (14, 'E'), (33, 'C')],
    'H': [ (26, 'B'), (7, 'G')],
}

prims_algorithm(graph, start='A')