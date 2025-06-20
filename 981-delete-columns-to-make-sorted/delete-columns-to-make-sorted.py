class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        n=len(strs[0])
        m=len(strs)
        for i in range(n):
            for j in range(1,m):
                if strs[j][i]<strs[j-1][i]:
                    count+=1
                    break
        return count
        

                