'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        
        ans = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(0, len(s)-1):

            a = dic[s[i]]
            b = dic[s[i+1]]

            if b > a: 
                ans -= a
            else:
                ans += a

        ans += dic[s[-1]]
        
        return ans
