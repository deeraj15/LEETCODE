class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=""
        for i in stones:
            for j in jewels:
                if i==j:
                    ans+=i
        return len(ans)
