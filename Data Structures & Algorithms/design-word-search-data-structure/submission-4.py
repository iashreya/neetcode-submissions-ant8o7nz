class WordDictionary:

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.Node()
            node = node.children[ch]
        node.EOW = True
        return 

    def search(self, word: str) -> bool:

        def dfs(word, node):
            if word == "":
                return node.EOW

            ch = word[0]
            if ch == ".":
                for child in node.children.values():
                    found = dfs(word[1:], child)
                    if found:
                        return True
                return False

            if ch in node.children:
                return dfs(word[1:], node.children[ch])
            
            return False
        return dfs(word, self.root)

    class Node:
        def __init__(self):
            self.children = {}
            self.EOW = False