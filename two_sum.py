class Solution(object):
    def twoSum(self, nums, target):
        # Dictionary to store the indices of the numbers
        index = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in index:
                return [index[temp], i]
            index[num] = i
