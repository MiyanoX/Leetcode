class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_1 = ["I", "X", "C", "M"]
        roman_2 = ["V", "L", "D"]
        
        sum = 0
        while s:
            last = s[-1]
            length = len(s)
            print(last)
            if length == 1:
                sum += romanDict[s]
                s = ""
            else:
                last_2 = s[-2]
                if (romanDict[last] > romanDict[last_2]) and (last_2 in roman_1):
                    sum = sum + romanDict[last] - romanDict[last_2]
                    print(s[-2:])
                    s = s[:-2]
                elif last in roman_1:
                    num = 1
                    while length > num and s[length-1-num] == last:
                        num += 1
                    s = s[:-num]
                    sum += romanDict[last] * num
                else:
                    sum += romanDict[last]
                    s = s[:-1]
            print(sum)
        return sum
                    
print(Solution.romanToInt(0, "DCXXI"))
