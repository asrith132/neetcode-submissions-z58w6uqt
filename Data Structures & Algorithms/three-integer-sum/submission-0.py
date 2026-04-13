class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        go through each num and then for each num we 
        """
        hashmap = {}
        final_list = []
        for i, num in enumerate(nums):
            hashmap = {}
            target = 0 - num
            for j in range(i + 1, len(nums)):
                if target - nums[j] in hashmap:
                    if (i != j != hashmap[target - nums[j]]):
                        new_list = sorted([nums[i], target - nums[j], nums[j]])
                        if new_list not in final_list:
                            final_list.append(new_list)
                else:
                    hashmap[nums[j]] = j
        return final_list
                        
            
        