def topological_sort(graph):
    n = len(graph)
    indegrees = [0] * n
    for v in (v for neighbors in graph for v in neighbors):
        indegrees[v] += 1
    stack = [u for u in range(n) if indegrees[u] == 0]
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                stack.append(v)
    return order
