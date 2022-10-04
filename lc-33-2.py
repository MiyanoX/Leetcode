class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        sum = 0
        
        for i in range(len(s)-1):
            if romanDict[s[i]] < romanDict[s[i+1]]:
                sum -= romanDict[s[i]]
            else:
                sum += romanDict[s[i]]
        return sum + romanDict[s[-1]]
    
print(Solution.romanToInt(0, "DCXXI"))