class SegmentTree:
    def __init__(self, len_or_array, op, e):
        self._op = op
        self._e = e
        is_int = isinstance(len_or_array, int)
        n = len_or_array if is_int else len(len_or_array)
        self._size = 1 << (n - 1).bit_length()
        self._tree = [self._e] * (self._size << 1)
        if not is_int:
            self._build(len_or_array)

    def _build(self, array):
        for i, a in enumerate(array):
            self._tree[i + self._size] = a
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = self._op(self._tree[i << 1], self._tree[i << 1 | 1])

    def update(self, index, value):
        i = index + self._size
        self._tree[i] = value
        while i > 1:
            i >>= 1
            self._tree[i] = self._op(self._tree[i << 1], self._tree[i << 1 | 1])

    def query(self, left, right):
        l = left + self._size
        r = right + self._size
        f_l = self._e
        f_r = self._e
        while l <= r:
            if l & 1:
                f_l = self._op(f_l, self._tree[l])
                l += 1
            if ~r & 1:
                f_r = self._op(self._tree[r], f_r)
                r -= 1
            l >>= 1
            r >>= 1
        return self._op(f_l, f_r)
