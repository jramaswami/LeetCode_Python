"""
LeetCode
506. Relative Ranks
May 2024 Challenge
jramaswami
"""


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        def medal(t):
            if t < len(medals):
                return medals[t]
            return str(t+1)

        sorted_scores = list(sorted(((t, i) for i, t in enumerate(score)), reverse=True))
        soln = ['' for _ in score]
        for rank, (_, i) in enumerate(sorted_scores):
            soln[i] = medal(rank)
        return soln