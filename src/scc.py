def find_strongly_connected_components(graph):
    n = len(graph)
    indices = [0] * n
    on_stack = [False] * n
    stack = []
    timer = 0
    sccs = []
    scc_ids = [0] * n
    id_ = 0

    def dfs(u):
        nonlocal timer, id_
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
                scc_ids[node] = id_
                if node == u:
                    break
            sccs.append(scc)
            id_ += 1
        return low

    for u in range(n):
        if indices[u] == 0:
            dfs(u)
    return sccs, scc_ids


def build_condensation_graph(graph, sccs, scc_ids):
    dag = [set() for _ in sccs]
    for u, neighbors in enumerate(graph):
        i = scc_ids[u]
        dag[i].update(j for v in neighbors if (j := scc_ids[v]) != i)
    dag = [list(adj) for adj in dag]
    return dag
