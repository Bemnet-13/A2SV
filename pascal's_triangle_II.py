class Solution:
    def getRow(self, rowIndex: int):
        row = [[1], [1,1]]
        i = 1
        while i < rowIndex:
            last_row = row[-1][:]
            last_row.append(1)
            for i in range(1, len(last_row)- 1):
                last_row[i] = row[-1][i - 1] + row[-1][i]
            row.append(last_row)
            i += 1
        return row[rowIndex]