class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.split()
        if len(k) != 0:
            return len(k[-1])
        else:
            return 0
