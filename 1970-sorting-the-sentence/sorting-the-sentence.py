class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(' ')
        ans=['a']*len(words)
        for word in words:
            index=int(word[-1])
            ans[index-1]=word[:-1]
        return ' '.join(ans)
        # pairs=[]
        # for word in s.split():
        #     text=' '
        #     num=' '
        # for char in word:
        #     if char.isdigit():
        #         num += char
        #     else:
        #         text += char
        # return num
    



        