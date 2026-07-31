class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

            if counts[n] > 1:
                return True

        return False


