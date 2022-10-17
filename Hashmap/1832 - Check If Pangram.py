class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lst = []
        for char in sentence:
            if char not in lst:
                lst.append(char)
        return len(lst) == 26