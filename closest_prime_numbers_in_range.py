"""
LeetCode
2523. Closest Prime Numbers in Range
March 2025 Challenge
jramaswami
"""


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        limit = right+1
        is_prime = [True for _ in range(limit)]
        is_prime[0] = is_prime[1] = False
        for x in range(4, limit, 2):
            is_prime[x] = False
        primes = [2, ]
        for p in range(3, limit, 2):
            if is_prime[p]:
                primes.append(p)
                for x in range(p + p, limit, p):
                    is_prime[x] = False
        
        curr_delta = pow(10,6)
        curr_values = [-1, -1]
        for i, q in enumerate(primes[1:], start=1):
            p = primes[i-1]
            if left <= p <= right and left <= q <= right:
                if q - p < curr_delta:
                    curr_delta, curr_values = q-p, [p, q]
        return curr_values
