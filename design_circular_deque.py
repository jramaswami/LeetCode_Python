"""
LeetCode
641. Design Circular Deque
September 2024 Challenge
jramaswami
"""


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = [None] * k
        self.left = self.right = 0        
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.left = (self.left - 1 + self.k) % self.k
        self.deque[(self.left + self.k) % self.k] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.deque[(self.right + self.k) % self.k] = value
        self.right = (self.right + 1 + self.k) % self.k
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[(self.left + self.k) % self.k] = None
        self.left = (self.left + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[(self.right - 1 + self.k) % self.k] = None
        self.right = (self.right - 1 + self.k) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.left + self.k) % self.k]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.right - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
