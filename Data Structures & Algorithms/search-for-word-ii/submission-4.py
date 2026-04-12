class Solution:
    class Trie:
        def __init__(self):
            self.root = self.Node()

        class Node:
            def __init__(self):
                self.children = {}
                self.word = None

        def addWord(self, word):
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = self.Node()
                node = node.children[ch]
            
            node.word = word
                
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.Trie()
        for word in words:
            trie.addWord(word)

        rows = len(board)
        cols = len(board[0])
        found = []

        def dfs(r, c, node):
            if ((r < 0 or r >= rows) or 
               (c < 0 or c >= cols)):
               return False

            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return
            
            next_node = node.children[ch]

            if next_node.word:
                found.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r + dr, c + dc, next_node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)
        
        return found


        