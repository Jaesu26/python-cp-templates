class _Node:
    __slots__ = ("left_child", "right_child", "size")

    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.size = 0


class DynamicOrderStatisticTree:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._root = _Node()

    @property
    def size(self):
        return self._root.size

    def count(self, x):
        node = self._root
        left, right = self._min_value, self._max_value
        while node is not None and left <= right:
            if left == right:
                return node.size
            mid = (left + right) // 2
            if x <= mid:
                node = node.left_child
                right = mid
            else:
                node = node.right_child
                left = mid + 1
        return 0

    def update(self, x, diff):
        node = self._root
        left, right = self._min_value, self._max_value
        node.size += diff
        while left < right:
            mid = (left + right) // 2
            if x <= mid:
                if node.left_child is None:
                    node.left_child = _Node()
                node = node.left_child
                right = mid
            else:
                if node.right_child is None:
                    node.right_child = _Node()
                node = node.right_child
                left = mid + 1
            node.size += diff

    def find_kth(self, k):
        node = self._root
        left, right = self._min_value, self._max_value
        while left < right:
            mid = (left + right) // 2
            left_child_size = node.left_child.size if node.left_child is not None else 0 
            if k <= left_child_size:
                node = node.left_child
                right = mid
            else:
                k -= left_child_size
                node = node.right_child
                left = mid + 1
        return left

    def bisect_right(self, x):
        left, right = self._min_value, self._max_value
        node = self._root
        if x < left:
            return 0
        if x >= right:
            return node.size
        f_x = 0
        while node is not None and left <= right:
            if left == right:
                f_x += node.size
                break
            mid = (left + right) // 2
            if x <= mid:
                node = node.left_child
                right = mid
            else:
                if node.left_child is not None:
                    f_x += node.left_child.size
                node = node.right_child
                left = mid + 1
        return f_x
