# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

def maximumWealth(self, accounts):
    sumList = []
    for i in range(len(accounts)):
        sumd = sum(accounts[i])
        sumList.append(sumd)
    return max(sumList)

