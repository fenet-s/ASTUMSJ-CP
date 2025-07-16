class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:  
        final=[]
        name_height=[[x,y] for x,y in zip(names,heights)]
        name_height.sort(key=lambda x:x[1],reverse=True)
        for i in range(len(names)):
            final.append(name_height[i][0])
        return final
       

        

        
        