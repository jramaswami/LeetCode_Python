"""
LeetCode :: July 2021 Challenge :: Word Ladder II
jramaswami
"""


from collections import defaultdict


def adjacent(wd1, wd2):
    """
    Return True if wd1 and wd2 differ by only a single letter.
    """
    delta = 0
    for a, b in zip(wd1, wd2):
        if a != b:
            delta += 1
    return delta == 1


def build_graph(word_list):
    """
    Build a graph of words that differ by 1 letter.
    """
    adj = defaultdict(list)
    for i, wd1 in enumerate(word_list):
        for wd2 in word_list[i+1:]:
            if adjacent(wd1, wd2):
                adj[wd1].append(wd2)
                adj[wd2].append(wd1)
    return adj


def dfs(begin_word, end_word, adj):

    soln = []
    visited = defaultdict(int)

    def dfs_visit(u, path):
        if u == end_word:
            path.append(u)
            if not soln or len(path) < len(soln[0]):
                soln.clear()
                soln.append(list(path))
            elif len(path) == len(soln[0]):
                soln.append(list(path))
            path.pop()
            return

        visited[u] = 1
        path.append(u)

        for v in adj[u]:
            if not visited[v]:
                dfs_visit(v, path)

        path.pop()
        visited[u] = 0

    dfs_visit(begin_word, [])
    return soln


class Solution():
    def findLadders(self, begin_word, end_word, word_list):
        if begin_word not in word_list:
            word_list.append(begin_word)
        adj = build_graph(word_list)
        return dfs(begin_word, end_word, adj)


def test_1():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]
    expected = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)


def test_2():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log"]
    expected = []
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)


def test_3():
    """TLE"""
    begin_word = "qa"
    end_word = "sq"
    word_list = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    expected = []
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)
