class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
                
        res = sorted(dict, key=lambda x: (-dict[x], x))
        
        return res[:k]