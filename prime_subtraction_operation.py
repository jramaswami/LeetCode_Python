"""
LeetCode
2601. Prime Subtraction Operation
November 2024 Challenge
jramaswami
"""


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Sieve primes
        is_prime = [True for _ in range(1000)]
        is_prime[0] = is_prime[1] = False
        for x in range(4, 1000, 2):
            is_prime[x] = False
        for p in range(3, 1000, 2):
            if is_prime[p]:
                for x in range(p+p, 1000, p):
                    is_prime[x] = False

        primes = [p for p in range(1000) if is_prime[p]]
        
        # Keep track of the current max value
        curr_max = 0
        # For each number
        for n in nums:
            x = n
            # Find the lowest number we can produce
            # by subtracing a prime from n that is 
            # more than our current max
            for p in primes:
                if n - p <= curr_max:
                    break
                x = n - p
            # If we cannot produce a number greater than
            # the curr max, then return False
            if x <= curr_max:
                return False
            # Update current max
            curr_max = x
        # Return true
        return True
