from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        countnum1=Counter(nums1)
        countnum2=Counter(nums2)
        final=[]
        for num in countnum1:
            if num in countnum2:
                final.extend([num]* min(countnum1[num],countnum2[num]))
        return final

