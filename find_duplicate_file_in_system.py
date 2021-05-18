"""
LeetCode :: May 2021 Challenge :: Find Duplicate File in System
jramaswami
"""
from typing import *
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dupes = defaultdict(list)
        for T in paths:
            folder, *files = T.split()
            for f in files:
                name, content = f.split('(')
                path = folder + '/' + name
                dupes[content].append(path)

        soln = []
        for paths in dupes.values():
            if len(dupes) > 1:
                soln.append(paths)
        return soln




def test_1():
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    expected = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    result = Solution().findDuplicate(paths)
    print(result)
    assert sorted(sorted(t) for t in expected) == sorted(sorted(t) for t in result)


def test_2():
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    expected = [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    result = Solution().findDuplicate(paths)
    print(result)
    assert sorted(sorted(t) for t in expected) == sorted(sorted(t) for t in result)


def test_3():
    """WA"""
    paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
    expected = []
    result = Solution().findDuplicate(paths)
    print(result)
    assert sorted(sorted(t) for t in expected) == sorted(sorted(t) for t in result)
