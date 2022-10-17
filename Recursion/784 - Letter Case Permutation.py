class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for i in range(len(s)):
            length = len(res)
            if s[i].isalpha():
                res *= 2
                for j in range(length):
                    res[j] += s[i]
                    res[length+ j] += s[i].swapcase()
            else:
                for j in range(length):
                    res[j] += s[i]
        return res