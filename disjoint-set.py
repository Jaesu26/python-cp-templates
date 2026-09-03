class DisjointSet:
    def __init__(self, n):
        self._parents = list(range(n))
        self._sizes = [1] * n

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self._sizes[u_root] > self._sizes[v_root]:
            u_root, v_root = v_root, u_root
        self._parents[u_root] = v_root
        self._sizes[v_root] += self._sizes[u_root]
        return True

    def find(self, u):
        p_u = self._parents[u]
        if p_u != u:
            self._parents[u] = self.find(p_u)
        return self._parents[u]

    def get_size_of(self, u):
        return self._sizes[self.find(u)]
