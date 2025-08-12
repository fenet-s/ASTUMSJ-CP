class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sorted_skills=sorted(skill)
        left=0
        pairs=[]
        right=len(skill)-1
        add_pairs=[]
        while left<right:
           
            mult=sorted_skills[right]*sorted_skills[left]
            add=sorted_skills[right]+sorted_skills[left]
            pairs.append(mult)
            add_pairs.append(add)
            right-=1
            left+=1
        set1=set(add_pairs)
        if len(set1)==1:
            return sum(pairs)
        else:
            return -1
        
        