class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return t
        if len(s)<len(t):
            return ""
        freq_t={}
        for ch in t:
            freq_t[ch]=freq_t.get(ch,0)+1
        left=0
        freq_s={}
        min_length=float('inf')
        res=""
        formed=0
        required=len(freq_t)

        for right in range(len(s)):
            freq_s[s[right]]=freq_s.get(s[right],0)+1
            if s[right] in freq_t and freq_s[s[right]]==freq_t[s[right]]:
                formed+=1
            while formed==required:
                if (right-left+1)<min_length:
                    min_length=right-left+1
                    res=s[left:right+1]
                freq_s[s[left]]-=1
                if s[left] in freq_t and freq_s[s[left]]<freq_t[s[left]]:
                    formed-=1
                left+=1
        return res

