class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ret = [0] * length
        for i in range(length):
            total = 1
            for j in range(length):
                if (i != j):
                    print(nums[j])
                    total = total * nums[j]
            ret[i] = total
        return ret

            
        
        
