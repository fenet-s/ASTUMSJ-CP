from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        for element, times in count.items():
            if times==1:
                return element

        
        