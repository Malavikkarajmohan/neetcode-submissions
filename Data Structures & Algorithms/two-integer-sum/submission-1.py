class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #value:index

        for i,n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return 

assert Solution().twoSum([3,4,5,6], 7) == [0,1]
        