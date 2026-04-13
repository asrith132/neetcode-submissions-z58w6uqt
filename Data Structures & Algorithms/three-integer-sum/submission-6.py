class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-4, -1, -1, 0, 1, 2]
        """
        nums = sorted(nums)
        final_list = []
        for i in range(0, len(nums) - 2):
            current_num = nums[i]
            if i > 0 and nums[i - 1] == current_num:
                continue
            l = i + 1
            r = len(nums) - 1
            target = 0 - current_num
            while (l < r):
                left_num = nums[l]
                right_num = nums[r]
                current_sum = left_num + right_num
                if (current_sum < target):
                    l += 1
                elif (current_sum > target):
                    r -= 1
                else:
                    final_list.append([current_num, left_num, right_num])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return list(final_list)


                        
            
        