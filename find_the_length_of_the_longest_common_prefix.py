class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        def all_prefixes(x):
            while x:
                yield str(x)
                x = x // 10
        
        P = set()
        for n in arr1:
            for pfx in all_prefixes(n):
                P.add(pfx)
        
        soln = 0
        for n in arr2:
            for pfx in all_prefixes(n):
                if pfx in P:
                    soln = max(soln, len(pfx))
        return soln
