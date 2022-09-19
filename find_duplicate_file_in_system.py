"""
LeetCode :: September 2022 Challenge :: Find Duplicate File in System
jramaswami
"""


from typing import *
import collections


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files_by_content = collections.defaultdict(list)
        for path in paths:
            folder, *files = path.split()
            for file in files:
                paren = file.find('(')
                filepath = f"{folder}/{file[:paren]}"
                content = file[paren+1:-1]
                files_by_content[content].append(filepath)
        return [f for f in files_by_content.values() if len(f) > 1]




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
