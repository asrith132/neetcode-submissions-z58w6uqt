class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix = [1] * len_nums
        postfix = [1] * len_nums
        total = 1
        total_two = 1
        for i in range(len_nums):
            total = nums[i] * total
            prefix[i] = total
            total_two = nums[len_nums - i - 1] * total_two
            postfix[len_nums - i - 1] = total_two
            print("Prefix: " + str(prefix[i]) + "Postfix: "  + str(postfix[i]))

        ret = [1] * len_nums
        for i in range(len_nums):
            print(i)
            if (i == 0):
                ret[i] = postfix[i+1]
            elif (i == len_nums - 1):
                ret[i] = prefix[i-1]
            else:
                ret[i] = prefix[i-1] * postfix[i+1]
        return ret
            

            
        
        
