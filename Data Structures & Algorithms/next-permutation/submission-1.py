class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = -1
        pivot = -1
        for i in range(len(nums) - 1, -1, -1):
            if prev > nums[i]:
                pivot = i
                break
            else:
                prev = nums[i]

        if pivot == -1:
            nums.sort()
            return nums

        val = nums[pivot]
        swap = -1
        smallest = float('inf')
        for i in range(i + 1, len(nums)):
            if nums[i] > val and nums[i] < smallest:
                smallest = nums[i]
                swap = i
        
        temp = nums[pivot]
        nums[pivot] = nums[swap]
        nums[swap] = temp

        nums[pivot + 1: len(nums)] = sorted(nums[pivot + 1: len(nums)])
        return nums

            
        