class LazySegmentTree:
    _root = 1

    def __init__(self, size_or_array, op, e, apply, compose, e_lazy):
        self._op = op
        self._e = e
        self._apply = apply
        self._compose = compose
        self._e_lazy = e_lazy
        is_int = isinstance(size_or_array, int)
        n = size_or_array if is_int else len(size_or_array)
        self._start, self._end = 0, n - 1
        size = 1 << ((n - 1).bit_length() + 1)
        self._tree = [e] * size
        self._lazy = [e_lazy] * size
        if not is_int:
            self._build(self._root, 0, n - 1, size_or_array)

    def _build(self, node, start, end, array):
        if start == end:
            self._tree[node] = array[start]
            return
        mid = (start + end) // 2
        self._build(2 * node, start, mid, array)
        self._build(2 * node + 1, mid + 1, end, array)
        self._tree[node] = self._op(self._tree[2 * node], self._tree[2 * node + 1])

    def update(self, left, right, param):
        self._update(left, right, param, self._root, self._start, self._end)

    def _update(self, left, right, param, node, start, end):
        self._push(node, start, end)
        if left > end or right < start:
            return
        if left <= start and end <= right:
            self._lazy[node] = self._compose(self._lazy[node], param)
            self._push(node, start, end)
            return
        mid = (start + end) // 2
        self._update(left, right, param, 2 * node, start, mid)
        self._update(left, right, param, 2 * node + 1, mid + 1, end)
        self._tree[node] = self._op(self._tree[2 * node], self._tree[2 * node + 1])

    def _push(self, node, start, end):
        if self._lazy[node] == self._e_lazy:
            return
        self._tree[node] = self._apply(self._tree[node], self._lazy[node], end - start + 1)
        if start != end:
            self._lazy[2 * node] = self._compose(self._lazy[2 * node], self._lazy[node])
            self._lazy[2 * node + 1] = self._compose(self._lazy[2 * node + 1], self._lazy[node])
        self._lazy[node] = self._e_lazy

    def query(self, left, right):
        return self._query(left, right, self._root, self._start, self._end)

    def _query(self, left, right, node, start, end):
        self._push(node, start, end)
        if left > end or right < start:
            return self._e
        if left <= start and end <= right:
            return self._tree[node]
        mid = (start + end) // 2
        f_l = self._query(left, right, 2 * node, start, mid)
        f_r = self._query(left, right, 2 * node + 1, mid + 1, end)
        return self._op(f_l, f_r)
