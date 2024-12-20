class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        lp_set = {}
        for i in range(len(licensePlate)):
            if licensePlate[i].isalpha():
                lp_set[licensePlate[i].lower()] = lp_set.get(licensePlate[i].lower(), 0)+1 

        cand_words = []
        for word in words:
            w_map = Counter(word)
            skip_word = False
            for key in lp_set:
                if lp_set[key] > w_map.get(key, 0):
                    skip_word = True
                
            if not skip_word:
                cand_words.append(word)

        cand_words.sort(key=len)

        return cand_words[0]

        
