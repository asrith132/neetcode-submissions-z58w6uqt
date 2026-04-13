class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_one = 0
        pointer_two = len(numbers) - 1
        while (True):
            if (numbers[pointer_two] + numbers[pointer_one] > target):
                pointer_two = pointer_two - 1;
            elif (numbers[pointer_two] + numbers[pointer_one] < target):
                pointer_one = pointer_one + 1;
            else:
                return [pointer_one + 1, 1 + pointer_two]
        