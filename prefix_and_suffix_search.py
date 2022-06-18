"""
Leet Code :: June 2022 Challenge :: Prefix and Suffix Search
jramaswami
"""


class WordFilter:

    def __init__(self, words):
        self.lookup = dict()
        for i, word in enumerate(words):
            prefixes = [word[:r] for r in range(1, len(word)+1)]
            suffixes = [word[l:] for l in range(len(word))]
            for prefix in prefixes:
                for suffix in suffixes:
                    key = "*".join([prefix, suffix])
                    self.lookup[key] = i

    def f(self, prefix, suffix):
        key = "*".join([prefix, suffix])
        return self.lookup.get(key, -1)


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
        result = getattr(wf, meth)(*args)
        print(f"{meth=} {args=} {exp=} {result=}")
        assert result == exp



def test_3():
    """WA"""
    methods = ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
    arguments = [[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
    wf = WordFilter(*arguments[0])
    expected = [None,9,4,5,0,8,1,2,5,3,1]
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        print(meth, args, exp)
        assert getattr(wf, meth)(*args) == exp
