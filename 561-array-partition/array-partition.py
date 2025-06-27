class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sub_list=[]
        left=0
        while left < len(nums):
            sub_list.append(nums[left])
            left+=2
        return sum(sub_list)
        