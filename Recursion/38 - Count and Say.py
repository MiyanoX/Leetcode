class Solution:
    def countAndSay(self, n: int) -> str:
	
		# base case
        if n == 1:
            return str(n)
        
		# recursive result
        prev = self.countAndSay(n-1)
		
		# count each number in string
        res = ''
        index, count = 0, 0
        while index < len(prev):
            current = prev[index]
            while index < len(prev) and prev[index] == current:
                count += 1
                index += 1
            res += str(count) + str(current)
            count = 0
			
        return res