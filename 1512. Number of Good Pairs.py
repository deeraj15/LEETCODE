class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        ans=0
        for i in dici:
            n=dici[i]
            temp=n*(n-1)/2
            ans+=temp
        return int(ans)