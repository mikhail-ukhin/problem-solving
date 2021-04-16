# Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

#     Only one letter can be changed at a time.
#     Each transformed word must exist in the word list.

# Return 0 if there is no such transformation sequence.

from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        words = set(wordList)

        if not endWord in words: return 0

        beginSet = set()
        endSet = set()

        beginSet.add(beginWord)
        endSet.add(endWord)

        length = 1

        while len(beginSet) and len(endSet):
            



    def get_neighbors(self, word: str):
        neighbors = []
        chars = list(word)

        for i in range(len(chars)):
            temp = chars[i]
            current_char, end_char = 97, 123

            while current_char < end_char:
                chars[i] = chr(current_char)
                neighbor = "".join(chars)
                neighbors.append(neighbor)

                current_char += 1

            chars[i] = temp    

        return neighbors    


if __name__ == "__main__":
    s = Solution()
    r = s.ladderLength('hit', 'cog', ['hot','dot','dog','lot','log','cog'])

    print(r)


