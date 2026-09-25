class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        
        l1 = 0 
        r1 = l - 1
        while l1 <= r1:
            mid = (l1 + r1) // 2

            if target > nums[mid]:
                l1 = mid + 1
            elif nums[mid] > target:
                r1 = mid - 1
            else:
                return mid

        l2 = l
        r2 = len(nums) - 1
        while l2 <= r2:
            mid = (l2 + r2) // 2

            if target > nums[mid]:
                l2 = mid + 1
            elif nums[mid] > target:
                r2 = mid - 1
            else:
                return mid

        return -1
        
        