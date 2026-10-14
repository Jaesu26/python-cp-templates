def find_strongly_connected_components(graph):
    n = len(graph)
    sccs, S, P = [], [], []
    indices = [-1] * n
    scc_ids = [-1] * n
    stack = list(range(n))
    while stack:
        u = stack.pop()
        if u < 0:
            u = ~u
            if u != P[-1]:
                continue
            scc = []
            while True:
                node = S.pop()
                scc.append(node)
                scc_ids[node] = len(sccs)
                if node == u:
                    break
            sccs.append(scc)
            P.pop()
        elif indices[u] == -1:
            indices[u] = len(S)
            S.append(u)
            P.append(u)
            stack.append(~u)
            stack.extend(graph[u])
        elif scc_ids[u] == -1:
            while indices[P[-1]] > indices[u]:
                P.pop()
    return sccs, scc_ids


def build_condensation_graph(graph, sccs, scc_ids):
    dag = [set() for _ in sccs]
    for u, neighbors in enumerate(graph):
        i = scc_ids[u]
        dag[i].update(j for v in neighbors if (j := scc_ids[v]) != i)
    return [list(adj) for adj in dag]
