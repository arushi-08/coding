class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        # rowlen = len(words)
        # for i in range(rowlen):
        #     collen = len(words[i])
        #     for j in range(collen):
        #         if j < rowlen and i < collen and words[i][j] != words[j][i]:
        #             return False
        #         if (j >= rowlen and i < collen and j < collen) or (j < rowlen and i >= collen and i < rowlen):
        #             print(words[i][j], i, j, collen)
        #             return False
        
        for i in range(len(words)):
            colword = []
            for j in range(len(words)):
                if i < len(words[j]):
                    colword.append(words[j][i])
            # print(colword)
            if words[i] != "".join(colword):    
                return False

        return True
