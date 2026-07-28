class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 ## we need to check for last word to be present
        
        nei = defaultdict(list)
        ## In order to construct adjacency list, we need to create a
        ## pattern from the word with one letter changing
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        
        ## we have the adjacency list ready, we need to explore them
        visited = set(beginWord)
        q = deque([beginWord])
        res = 1
        ## it is asked to find the closest path
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                ## now we have a word, figure out all the patterns
                ## it can transform into
                ## each pattern leads to neigbhours this word can transform

                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visited:
                            visited.add(neiword)
                            q.append(neiword)
            res+=1
        return 0