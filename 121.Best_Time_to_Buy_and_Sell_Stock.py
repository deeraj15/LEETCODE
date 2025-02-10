class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnval=prices[0]
        anss=0
        for i in range(1,len(prices)):
            anss=max(anss,(prices[i]-minnval))
            minnval=min(minnval,prices[i])
        return anss