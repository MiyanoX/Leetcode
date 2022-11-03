class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        d = {}                              # count dictionary
        mid = 0                             # mid item
        for word in words:
            if word[::-1] in d:             # if have palindrome string
                if d[word[::-1]] == 1:      # decrease count
                    del d[word[::-1]]
                else:
                    d[word[::-1]] -= 1
                res += 4                    # result add 4
                if word[0] == word[1]:      # mid item decrease 1
                    mid -= 1
            elif word in d:                 # increase count
                d[word] += 1
            else:
                d[word] = 1
                if word[0] == word[1]:      # mid item increase 1
                    mid += 1
        return res + 2 if mid else res      # if have mid item, result add 2