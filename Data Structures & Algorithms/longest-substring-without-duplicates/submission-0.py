class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strs=set()
        max_length=0
        left=0
        for right in range(len(s)):
            while s[right] in strs:
                strs.remove(s[left])
                left+=1
            strs.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length

            
        