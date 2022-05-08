"""
LeetCode :: May 2022 Challenge :: Flatten Nested List Iterator
jramaswami
"""


class NestedIterator:
    def __init__(self, nested_list):
        self.stack = [(nested_list, 0)]
        self.empty = False
        self.top = None

    def _gettop(self):
        while True:
            if not self.stack:
                self.top = None
                self.empty = True
                return

            curr_list, curr_index = self.stack.pop()
            if curr_index < len(curr_list):
                # Each item is a NestedInteger.
                item = curr_list[curr_index]
                if item.isInteger():
                    self.top = item.getInteger()
                    self.stack.append((curr_list, curr_index + 1))
                    return
                else:
                    # This item is a list.
                    self.stack.append((curr_list, curr_index + 1))
                    next_list = item.getList()
                    self.stack.append((next_list, 0))

    def next(self):
        return self.top

    def hasNext(self):
        self._gettop()
        return not self.empty