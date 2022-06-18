"""
Leet Code :: June 2022 Challenge :: Prefix and Suffix Search
jramaswami
"""


class WordFilter:

    def __init__(self, words):
        self.words = [(t + "*" + t, i) for i, t in enumerate(words)]

    def f(self, prefix, suffix):
        key = suffix + "*" + prefix
        for wd, i in reversed(self.words):
            if wd.find(key) >= 0:
                return i
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


def test_1():
    methods = ["WordFilter", "f"]
    arguments = [[["apple"]], ["a", "e"]]
    wf = WordFilter(*arguments[0])
    expected = [None, 0]
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(wf, meth)(*args) == exp


def test_2():
    methods = ["WordFilter", "f", "f", "f"]
    arguments = [[["apple", "orange", "oe", "orangeorangeorange"]], ["a", "e"],["orange", "orange"], ["app", "zle"]]
    wf = WordFilter(*arguments[0])
    expected = [None, 0, 3, -1]
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(wf, meth)(*args) == exp



def test_3():
    """WA"""
    methods = ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
    arguments = [[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
    wf = WordFilter(*arguments[0])
    expected = [None,9,4,5,0,8,1,2,5,3,1]
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        print(meth, args, exp)
        assert getattr(wf, meth)(*args) == exp
