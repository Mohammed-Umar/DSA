class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_wealth = []
        
        for i in range(len(accounts)):
            sum_amt = sum(accounts[i])
            sum_wealth.append(sum_amt)
        return max(sum_wealth)