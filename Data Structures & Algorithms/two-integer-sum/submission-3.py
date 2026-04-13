class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        anagram = defaultdict(list)
        for i in range(0, len(nums)):
            if target - nums[i] in anagram:
                return[anagram[target-nums[i]], i]
            anagram[nums[i]] = i
        print(anagram.items())
        return [0,0]