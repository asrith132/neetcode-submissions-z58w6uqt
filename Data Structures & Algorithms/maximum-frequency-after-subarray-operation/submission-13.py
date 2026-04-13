class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count_of_k = nums.count(k)

        result = 0

        for i in range(1, 51):
            cnt = 0
            if nums == k:
                continue
            else:
                for num in nums:
                    if num == k:
                        cnt -= 1
                    elif num == i:
                        cnt += 1
                    cnt = max(cnt, 0)
                    result = max(result, cnt + count_of_k)
        return result
            

            

        
