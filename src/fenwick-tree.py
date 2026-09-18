class FenwickTree:
    def __init__(self, size_or_array):
        is_int = isinstance(size_or_array, int)
        self._size = size_or_array if is_int else len(size_or_array)
        self._tree = [0] * (self._size + 1)
        if not is_int:
            self._build(size_or_array)

    def _build(self, array):
        for i, a in enumerate(array, start=1):
            self._tree[i] += a
            j = i + (i & -i)
            if j <= self._size:
                self._tree[j] += self._tree[i]

    def add(self, index, delta):
        i = index + 1
        while i <= self._size:
            self._tree[i] += delta
            i += i & -i

    def query(self, left, right):
        return self._prefix_sum(right) - self._prefix_sum(left - 1)

    def _prefix_sum(self, index):
        i = index + 1
        f_i = 0
        while i > 0:
            f_i += self._tree[i]
            i -= i & -i
        return f_i
