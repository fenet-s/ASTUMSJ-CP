class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        str_list=[]
        string=''
        n=len(strs[0])
        m=len(strs)
        for i in range(n):
            group=''
            for j in range(m):
                group+=strs[j][i]
            str_list.append(group)
        for i in str_list:
            if i!=''.join(sorted(i)):
                count+=1
        return count
        

        