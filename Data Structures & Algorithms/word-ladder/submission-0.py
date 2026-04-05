from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)

        return 0

