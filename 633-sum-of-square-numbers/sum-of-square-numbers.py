class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(c**0.5) 
        flag=False
        while l<=r:
            square=l*l + r*r
            if square==c:
                return not flag
            elif square < c:
                l+=1
            else:
                r-=1
        return flag

        