#6.66%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transpose = l = [[row[i] for row in board] for i in range(len(board))]
        d = {}
        idx = 0
        for i in board:
            for j in i:
                d[idx] = j
                idx += 1
        for i in board:
            seen = []
            for j in i:
                if j != '.' and j in seen:
                    return False
                seen.append(j)
        for i in transpose:
            seen = []
            for j in i:
                if j != '.' and j in seen:
                    return False
                seen.append(j)
        position = sum([[i for i in range(j, j + 7, 3)] for j in [0, 27, 54]],
                       [])

        def check(pos):
            #raise error if false
            arr = [[i + j for j in range(3)] for i in range(pos, pos + 21, 9)]
            seen = []
            for i in arr:
                for k in i:
                    j = d[k]
                    if j != '.' and j in seen:
                        raise Exception()
                    seen.append(j)

        for i in position:
            try:
                check(i)
            except:
                return False
        return True