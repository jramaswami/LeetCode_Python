"""
LeetCode
2115. Find All Possible Recipes from Given Supplies
March 2025 Challenge
jramaswami
"""


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies0 = set(supplies)
        made = []
        for _ in recipes:
            for r, i in zip(recipes, ingredients):
                if r not in supplies0:
                    if all(x in supplies0 for x in i):
                        changed = True
                        supplies0.add(r)
                        made.append(r)
        return made