def find_strongly_connected_components(graph):
    n = len(graph)
    indices = [0] * n
    on_stack = [False] * n
    stack = []
    sccs = []
    timer = 0

    def dfs(u):
        nonlocal timer
        timer += 1
        low = indices[u] = timer
        on_stack[u] = True
        stack.append(u)
        for v in graph[u]:
            if indices[v] == 0:
                low = min(low, dfs(v))
            elif on_stack[v]:
                low = min(low, indices[v])
        if low == indices[u]:
            scc = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                scc.append(node)
                if node == u:
                    break
            sccs.append(scc)
        return low

    for u in range(n):
        if indices[u] == 0:
            dfs(u)
    return sccs
