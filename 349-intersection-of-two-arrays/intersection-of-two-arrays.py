class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        for num in nums1:
            if num in nums2:
                inter.append(num)
        return list(set(inter))

        