import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        final = len(position)
        pair = sorted(zip(position, speed))
        sorted_position = []
        sorted_speed = []
        for a, b in pair:
            sorted_position.append(a)
            sorted_speed.append(b)
        prev_time = 0
        while sorted_position:
            top = sorted_position.pop()
            speed = sorted_speed.pop()
            time = (target - top)/speed
            if prev_time >= time:
                final -= 1
                time = prev_time
            prev_time = time
        return final
        