class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(len(nums)+1):
    #             if nums[i]+nums[j]==target:
    #                 return i,j
        storage = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in storage:
                return i, storage[diff]
            storage[nums[i]] = i
    
