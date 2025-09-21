import collections
from typing import List
import sortedcontainers


Movie = collections.namedtuple('Movie', ['price', 'shop_id', 'movie_id'])


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.inventory = dict()
        self.available = collections.defaultdict(sortedcontainers.SortedList)
        self.rented = sortedcontainers.SortedList()

        for s, m, p in entries:
            movie = Movie(p, s, m)
            inventory_key = (movie.shop_id, movie.movie_id)
            self.inventory[inventory_key] = p
            self.available[m].add(movie)

    def search(self, movie_id: int) -> List[int]:
        return [m.shop_id for m in self.available[movie_id]]

    def rent(self, shop_id: int, movie_id: int) -> None:
        inventory_key = (shop_id, movie_id)
        price = self.inventory[inventory_key]
        movie = Movie(price, shop_id, movie_id)
        self.available[movie_id].remove(movie)
        self.rented.add(movie)

    def drop(self, shop_id: int, movie_id: int) -> None:
        inventory_key = (shop_id, movie_id)
        price = self.inventory[inventory_key]
        movie = Movie(price, shop_id, movie_id)
        self.available[movie_id].add(movie)
        self.rented.remove(movie)

    def report(self) -> List[List[int]]:
        return [[m.shop_id, m.movie_id] for m in self.rented[:5]]


null = None


def test_1():
    fs = ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
    ps = [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
    es = [null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]
    mrs = MovieRentingSystem(*ps[0])
    for f, p, e in zip(fs[1:], ps[1:], es[1:]):
        assert getattr(mrs, f)(*p) == e

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()