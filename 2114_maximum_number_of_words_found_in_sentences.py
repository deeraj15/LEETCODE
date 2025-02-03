class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in range(len(sentences)):
            s=sentences[i]
            temp=1
            for j in range(len(s)):
                ab=s[j]
                if ab==" ":
                    temp+=1
                ans=max(ans,temp)
        return ans
                