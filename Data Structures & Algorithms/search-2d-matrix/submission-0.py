class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
            
        # access r1's col1 and rn's coln'
        nr = len(matrix)
        nc = len(matrix[0])

        left = 0
        right = nr * nc -1

        # Given mid flat index, row = mid // 4, col = mid % 4
        while left <= right:
            mid = (left + right) // 2

            row  = mid // nc
            col =  mid % nc

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

        