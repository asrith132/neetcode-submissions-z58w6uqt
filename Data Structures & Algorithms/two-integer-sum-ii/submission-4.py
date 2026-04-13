class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            left_num = numbers[l]
            right_num = numbers[r]
            current_sum = left_num + right_num
            if (current_sum < target):
                l += 1
            elif (current_sum > target):
                r -= 1
            else:
                return [l + 1, r + 1]