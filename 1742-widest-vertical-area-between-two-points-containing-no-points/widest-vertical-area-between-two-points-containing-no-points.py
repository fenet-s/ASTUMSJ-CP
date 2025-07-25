class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        result=[]
        final=[]
        dif=0
        for i in range(len(points)):
            result.append(points[i][0])
        result.sort()
        left=0
        right=1
        while(right<len(points)):
            dif=result[right]-result[left]
            final.append(dif)
            left+=1
            right+=1
        return max(final)

