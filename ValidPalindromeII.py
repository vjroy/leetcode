def Palindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        while L <= R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True


class Solution:

    def validPalindrome(self, s: str) -> bool:
        if Palindrome(s):
            return True
        for i in range(len(s)):
            pass
            
       