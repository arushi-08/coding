class Solution:
    def betterCompression(self, compressed: str) -> str:
        
        # char appear only once
        # chars are alphabetical

        # compressed = 'a3c9b2c1'
        # a3b2c10
        
        # split after digits and before chars
        # sort list
        # add items

        strings = []
        curr_string = ''
        for i in range(len(compressed)):
            curr_string += compressed[i]
            if i + 1 < len(compressed) and compressed[i].isdigit() and compressed[i+1].isalpha():
                strings.append(curr_string)
                curr_string = ''

        if curr_string:
            strings.append(curr_string)
        
        strings = sorted(strings)
        
        compressed_better = ''
        i = 0
        print(strings)
        while i < len(strings):
            curr_number = 0
            while i + 1 < len(strings) and strings[i][0] == strings[i+1][0]:
                curr_number += int(strings[i][1:])
                i += 1
            if curr_number:
                curr_number += int(strings[i][1:])
                compressed_better += strings[i][0] + str(curr_number)
                # print(compressed_better, strings[i])
            else:
                # print(strings[i])
                compressed_better += strings[i]
            i += 1
        
        return compressed_better




