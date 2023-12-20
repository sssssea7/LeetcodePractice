from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f2c = {f:c for f, c in zip(foods, cuisines)}
        self.f2r = {f:-r for f, r in zip(foods, ratings)}
        self.c2f = defaultdict(SortedList)
        for f, c, r in zip(foods, cuisines, ratings):
            self.c2f[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.f2c[food]
        self.c2f[c].remove((self.f2r[food], food))
        self.c2f[c].add((-newRating, food))
        self.f2r[food] = -newRating

    def highestRated(self, cuisine: str) -> str:
        return self.c2f[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)