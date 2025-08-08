class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
      sorted_list=sorted(people)
      left=0
      right=len(people)-1
      count=0
      while right>=left:
        if sorted_list[right]+sorted_list[left]<=limit:
            left+=1
        right-=1
        count+=1
      return count 