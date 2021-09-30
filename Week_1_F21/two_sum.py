class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, curr_num in enumerate(nums):
            if curr_num in d:
                return [d[curr_num], idx]   # success! return result.
            else:
                d[target - curr_num] = idx  # cache: target - curr_num
                
        return []

    def slow_twoSum(self, nums: List[int], target: int) -> List[int]:
        r = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []