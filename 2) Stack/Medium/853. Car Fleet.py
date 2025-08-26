'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        for i in range(length):
            position[i] = target - position[i]
            pos_time = []
        for i in range(length):
            pos_time.append([position[i], position[i] / speed[i]]) 
        pos_time.sort(key = lambda x: x[0])

        last = None
        for el in pos_time:
            if not last:
                last = el[1]
                counter = 1
            elif el[1] > last:
                counter += 1
                last = el[1]
        return counter