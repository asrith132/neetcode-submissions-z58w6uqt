class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = False
        for triplet in triplets:
            if triplet == target:
                return True
        
        arr = [False] * len(target)
        for i in range(0, len(triplets)):
            valid = True
            for j in range(0, 3):
                print(i, j)
                if triplets[i][j] > target[j]:
                    valid = False

            if valid:
                for j in range(0, len(triplets[i])):
                    if triplets[i][j] == target[j]:
                        arr[j] = True
        
        for val in arr:
            if val == False:
                return False

        return True
        
                        


        

