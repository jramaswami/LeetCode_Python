"""
LeetCode
2353. Design a Food Rating System
December 2023 Challenge
jramaswami
"""


import collections
import heapq


HItem = collections.namedtuple('HItem', ['negrating', 'food'])


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_ratings = dict()
        self.food_cuisines = dict()
        self.ratings_by_cuisine = collections.defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_ratings[f] = r
            self.food_cuisines[f] = c
            heapq.heappush(self.ratings_by_cuisine[c], HItem(-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cu = self.food_cuisines[food]
        self.food_ratings[food] = newRating
        heapq.heappush(self.ratings_by_cuisine[cu], HItem(-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        rbc = self.ratings_by_cuisine[cuisine]
        while rbc:
            fd = rbc[0].food
            if self.food_ratings[fd] == -rbc[0].negrating:
                break
            heapq.heappop(rbc)
        return rbc[0].food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)