class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        list =  [[1], [1,1]]
        
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        
        for i in range(0, numRows-2):
            last_row = list[-1]
            curr_row = [1]
            for j in range(0, len(last_row)-1):
                curr_row.append(last_row[j] + last_row[j+1])
            curr_row.append(1)
            list.append(curr_row)
            
        return list