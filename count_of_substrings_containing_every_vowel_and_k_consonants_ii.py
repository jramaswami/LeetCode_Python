"""
LeetCode
3306. Count of Substrings Containing Every Vowel and K Consonants II
March 2025 Challenge
jramaswami

Thank You NeetCode.IO
"""


import collections


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atleast(k):
            vowels = collections.defaultdict(int)
            consonants = 0
            result = 0
            left = 0
            for right, char in enumerate(word):
                if char in 'aeiou':
                    vowels[char] += 1
                else:
                    consonants += 1
            
                while len(vowels) == 5 and consonants >= k:
                    result += (len(word) - right)
                    if word[left] in 'aeiou':
                        vowels[word[left]] -= 1
                    else:
                        consonants -= 1
                    
                    if vowels[word[left]] == 0:
                        vowels.pop(word[left])
                    
                    left += 1
                
            return result

        return atleast(k) - atleast(k+1)   
