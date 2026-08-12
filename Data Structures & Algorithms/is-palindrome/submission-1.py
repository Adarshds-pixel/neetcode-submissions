class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch for ch in s if ch.isalnum()).lower()
        if s==s[::-1]:
            return True
        return False
        