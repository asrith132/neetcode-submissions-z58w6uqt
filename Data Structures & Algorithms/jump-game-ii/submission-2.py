class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        p = 0

        while p < len(nums) - 1:
            print(p)
            current_jump = nums[p]
            best_option = 0
            min_jumps += 1
            best_location = 0
            for i in range(p + 1, p + current_jump + 1):
                if i >= len(nums) - 1:
                    return min_jumps
                jump_val = i - p + nums[i]
                if jump_val > best_option:
                    best_option = jump_val
                    best_location = i
            p = best_location
        return min_jumps
        
        