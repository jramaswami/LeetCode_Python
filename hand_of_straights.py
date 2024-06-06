"""
LeetCode
846. Hand of Straights
jramaswami
"""


import collections


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # The there must be some k such that k * groupSize == len(hand)
        if len(hand) % groupSize:
            return False
        
        freqs = collections.Counter(hand)
        queue = collections.deque(sorted(freqs.keys()))

        while queue:
            hand = []
            for x in queue:
                if freqs[x]:
                    hand.append(x)
                    freqs[x] -= 1
                if len(hand) == groupSize:
                    break
            
            if len(hand) != groupSize:
                return False
            if any(b - a != 1 for a, b in zip(hand[:-1], hand[1:])):
                return False
            
            # Discard any cards that now have a frequency of zero
            while queue and freqs[queue[0]] == 0:
                queue.popleft()
        
        return True
