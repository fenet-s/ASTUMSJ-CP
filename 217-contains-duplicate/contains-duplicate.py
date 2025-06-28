from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count= Counter(nums)
        for element, cnt in count.items():
            if cnt >= 2:
                return True
        return False
        