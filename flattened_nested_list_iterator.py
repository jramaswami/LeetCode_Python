"""
LeetCode :: April 2021 Challenge :: Flatten Nested List Iterator
jramaswami
"""
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

def nested_iterator_to_list(nested_iterator, acc):
    if isinstance(nested_iterator, list):
        for item in nested_iterator:
            nested_iterator_to_list(item, acc)
    elif nested_iterator.isInteger():
        acc.append(nested_iterator.getInteger())
    else:
        nested_iterator_to_list(nested_iterator.getList(), acc)
        
        
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.items = []
        nested_iterator_to_list(nestedList, self.items)
        self.index = 0
            
    def next(self) -> int:
        ret_val = self.items[self.index]
        self.index += 1
        return ret_val
        
    def hasNext(self) -> bool:
        return self.index < len(self.items)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
