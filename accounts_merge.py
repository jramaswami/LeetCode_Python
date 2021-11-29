"""
LeetCode :: November 2021 Challenge :: 721. Accounts Merge
jramaswami
"""


import collections
import itertools


class UnionFind:

    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1 for _ in self.parent]

    def find_set(self, u):
        if self.parent[u] == u:
            return u
        p = self.find_set(self.parent[u])
        self.parent[u] = p
        return p

    def union_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]


class Solution:

    def accountsMerge(self, accounts):
        # Collection the indexes of each email.
        by_email = collections.defaultdict(set)
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                by_email[email].add(i)

        # Use union find to connect indexes.
        uf = UnionFind(len(accounts))
        for email, indexes in by_email.items():
            if len(indexes) > 1:
                for a, b in itertools.combinations(indexes, 2):
                    uf.union_set(a, b)

        # Use the union find to combine indexes.
        email_p = collections.defaultdict(list)
        for i, _ in enumerate(accounts):
            email_p[uf.find_set(i)].append(i)

        soln = []
        for i, E in email_p.items():
            name = accounts[i][0]
            curr = set()
            for j in E:
                curr.update(accounts[j][1:])
            T = [name]
            T.extend(sorted(curr))
            soln.append(T)

        return soln


def test_1():
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    expected = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    assert sorted(Solution().accountsMerge(accounts)) == sorted(expected)


def test_2():
    accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    expected = [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
    assert sorted(Solution().accountsMerge(accounts)) == sorted(expected)
