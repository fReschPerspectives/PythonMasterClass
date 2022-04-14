"""
Given a string s, return true if the s can be palindrome 
after deleting at most one character from it.
"""
import numpy as np

class Solution:
    def validPalindrome(s: str) -> bool:

        if s == s[::-1]:
            return True
        else:
            for j in range(len(s)):
                t = ''.join([s[i] for i in range(len(s)) if i != j])
                if t == t[::-1]:
                    return True
                else:
                    continue

        return False


s = "aba"
s2 = "abca"
s3 = "abc"
print(Solution.validPalindrome(s=s))
print(Solution.validPalindrome(s=s2))
print(Solution.validPalindrome(s=s3))