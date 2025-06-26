from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        for element,cnt in count.items():
            if cnt > len(nums)/2:
                return element
                

        