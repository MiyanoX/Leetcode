class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s: str) -> str:           # help function to backspace the string
            res = ''                            
            for char in s:
                if char == '#':                 # judge if current char is #
                    if res:
                        res = res[:-1]          # if res is not None, delete the last char in string
                else:
                    res += char                 # otherwise add char into string
            return res
        
        return backspace(s) == backspace(t)     # return the comparison of two strings