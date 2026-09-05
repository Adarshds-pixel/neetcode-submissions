from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)
        for word in strs:
            sorted_word="".join(sorted(word))
            if "".join(sorted(word))==sorted_word:
                freq[sorted_word].append(word)
        return list(freq.values())
            