from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=Counter(arr1)
        result=[]
        r2=[]
        for num in arr2:
            result.extend([num]*count[num])
        for num in arr1:
            if num not in result:
                r2.append(num)
        r3=sorted(r2)
        final=result+r3
        return final

        