# This is O(n) time and space
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         total = 0
#         for i in range(len(digits)):
#             total += digits[i] *  (10 ** (len(digits) - i - 1))
        
#         return self.numberToDigits(total + 1)

#     def numberToDigits(self, n: int) -> List[int]:
#         if n == 0:
#             return [0]
        
#         digits = []
#         while n > 0:
#             digits.append(n % 10)
#             n //= 10

#         return digits[::-1]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits