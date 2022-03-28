n = len(board)
        m = len(board[0])
        #_board = [x[:] for x in board]

        def dfs_word(visited, i,j, letter=0):
            if (i >= n) or (j>= m) or (j < 0) or (i < 0) or (i,j) in visited:               
                return False
            
            if board[i][j] == word[letter]:
                if letter == (len(word) - 1):
                    return True
                visited.append((i,j))
                out = []
                out.append(dfs_word(visited, i,j+1, letter+1))
                out.append(dfs_word(visited, i-1,j, letter+1))
                out.append(dfs_word(visited, i+1,j, letter+1)) 
                out.append(dfs_word(visited, i,j-1, letter+1))
                visited.remove((i,j))
                return max(out)
            
            return False
        

        for c in word:
            found = False
            for row in board:
                if c in row:
                    found = True
                    break
            if not found:
                return False
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs_word([], i,j):
                        return True
        return False
            
