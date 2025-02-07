# given string array and int array
# i.e., previously types sentence and times[i] is number of times sentence was typed
# for each character except '#' return top 3 hot prev typed sentences with same prefix
class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word): # O(S)
        trie = self.trie
        for ch in word:
            if ch not in trie:
                trie[ch] = {}
            trie = trie[ch]
        trie['#'] = '#'
    
    def starts_with(self, word): # O(S)
        trie = self.trie
        for ch in word:
            if ch not in trie:
                return {}
            trie = trie[ch]

        return trie
    
    def get_sentences(self, trie, prefix): # O(S+N)
        sentences = []

        def dfs(trie, sentences, word):
            if '#' in trie:
                sentences.append(word)
            
            for k in trie:
                if k != '#':
                    dfs(trie[k], sentences, word+k)

        for k in trie:
            if k == '#':
                sentences.append(prefix)
                continue
            dfs(trie[k], sentences, prefix+k)
        return sentences

class AutocompleteSystem:
    # O(N*S + NlogN)
    
    def __init__(self, sentences: List[str], times: List[int]):
        # store the sentences in a trie
        # when i find a '#' in trie that's a sentence
        # see its hot degree
        # sort elements by hot degree
        # return the top 3 based on ascii sorting
        self.trie = Trie()
        self.sentence_to_degree = {}
        for sentence, hot_degree in zip(sentences, times): # O(N*S)
            self.trie.insert(sentence)
            self.sentence_to_degree[sentence] = hot_degree

        self.input_search = ''

    def input(self, c: str) -> List[str]: # O(N+S+NlogN)
        
        if c == '#' : 
            self.trie.insert(self.input_search)
            self.sentence_to_degree[self.input_search] = self.sentence_to_degree.get(self.input_search, 0) + 1

            self.input_search = ''
            return []

        self.input_search += c
        trie_dict = self.trie.starts_with(self.input_search)
        sentences_start_w_search_word = self.trie.get_sentences(
            trie_dict, self.input_search
            )
        
        rank_sentences = []
        for sentence in sentences_start_w_search_word:
            rank_sentences.append([self.sentence_to_degree[sentence], sentence])

        rank_sentences.sort(key = lambda x: [-x[0], x[1]])

        return [sentence for _, sentence in rank_sentences][:3]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
