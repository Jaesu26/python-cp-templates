class OrderStatisticTree:
    _root = 1

    def __init__(self, max_value_or_counts):
        is_int = isinstance(max_value_or_counts, int)
        n = max_value_or_counts + 1 if is_int else len(max_value_or_counts)
        self._size = 1 << n.bit_length()
        self._tree = [0] * (self._size << 1)
        if not is_int:
            self._build(max_value_or_counts)

    def _build(self, array):
        for i, a in enumerate(array):
            self._tree[i + self._size] = a
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = self._tree[i << 1] + self._tree[i << 1 | 1]

    @property
    def size(self):
        return self._tree[self._root]

    def count(self, x):
        return self._tree[x + self._size]

    def update(self, x, diff):
        i = x + self._size
        while i:
            self._tree[i] += diff
            i >>= 1

    def find_kth(self, k):
        i = 1
        while i < self._size:
            i <<= 1
            if self._tree[i] < k:
                k -= self._tree[i]
                i |= 1
        return i - self._size

    def bisect_right(self, x):
        i = x + self._size
        f_x = 0
        while i:
            if ~i & 1:
                f_x += self._tree[i]
                i -= 1
            i >>= 1
        return f_x
