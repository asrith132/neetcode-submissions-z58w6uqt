class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return 1
        nums.sort()
        count = 1
        max_count = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            print(str(nums[i]) + " " + str(prev) + "/n")
            if (nums[i] - 1 == prev):
                print("enter")
                count += 1
            elif (nums[i] == prev):
                count += 0
            else:
                count = 1
            if (max_count < count):
                max_count = count
            prev = nums[i]
        return max_count


            

        