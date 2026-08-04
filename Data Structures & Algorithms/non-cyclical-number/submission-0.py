class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        current = n
        while current != 1:
            digits = self.digitsFromNum(current)
            sumSquared = sum(digit * digit for digit in digits)

            if sumSquared in seen:
                return False

            seen.add(sumSquared)
            current = sumSquared
        return True
        
        
    def digitsFromNum(self, n: int) -> list[int]:
        return [int(char) for char in str(n)]