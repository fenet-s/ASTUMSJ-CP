class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=list(set(nums))
        n.sort(reverse=True)
        if len(n)>= 3:
            return n[2]
        else:
            return max(n)


        