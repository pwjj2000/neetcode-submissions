class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [None] * len(position)
        for i in range(len(position)):
            cars[i] = (position[i], (target-position[i])/speed[i])
        cars.sort(key=lambda x: x[1])
        cars.sort(key=lambda x: x[0], reverse=True)
        fleets = 1
        fp, ft = cars[0]
        for i in range(len(cars)):
            p, t = cars[i]
            if t > ft:
                fleets += 1
                fp, ft = cars[i]
        return fleets
