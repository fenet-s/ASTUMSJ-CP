class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        final_list=[]
        joined_digit=int(''.join(str(i) for i in digits))
        joined_digit+=1
        final=str(joined_digit)
        for i in final:
            i.split(',')
            final_list.append(int(i))

        return final_list


        