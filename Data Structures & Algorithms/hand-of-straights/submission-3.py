class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        hashmap = defaultdict(int)

        for num in hand:
            hashmap[num] += 1

        for num in hand:
            if hashmap[num] == 0:
                continue

            for i in range(groupSize):
                if hashmap[num + i] == 0:
                    return False
                hashmap[num + i] -= 1

        return True