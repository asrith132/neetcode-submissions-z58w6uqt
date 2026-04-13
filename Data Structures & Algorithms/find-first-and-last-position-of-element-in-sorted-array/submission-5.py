class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            middle = (r + l) // 2
            if nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1
            else:
                check_left = middle
                check_right = middle
                while check_left - 1 >= 0 and nums[check_left - 1] == target:
                    check_left -= 1
                while check_right + 1 < len(nums) and nums[check_right + 1] == target:
                    check_right += 1
                return [check_left, check_right]
        return [-1, -1]
        