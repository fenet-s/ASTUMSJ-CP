class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank=[]
        sorted_score=sorted(score,reverse=True)
        first='Gold Medal'
        second='Silver Medal'
        third='Bronze Medal'
        for i in range(len(score)):
            if score[i]==max(score):
                rank.append(first)
            elif score[i]==sorted_score[1]:
                rank.append(second)
            elif score[i]==sorted_score[2]:
                rank.append(third)
            else:
                rank.append(str(sorted_score.index(score[i])+1))
        return rank
        
        

        