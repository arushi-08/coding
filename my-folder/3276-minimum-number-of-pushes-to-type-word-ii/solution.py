class Solution:
    def minimumPushes(self, word: str) -> int:
        
        wfreq = Counter(word)
        wfreq = sorted(wfreq.items(), key=lambda x:x[1], reverse=True)
        wmap = {}
        pushes = 0
        buttons = 1
        presses = 1
        for wd, freq in wfreq:
            if buttons == 9:
                presses += 1
                buttons = 1
            pushes += presses * freq
            buttons += 1
            # print('wd', wd, 'pushes', pushes, 'presses', presses, 'buttons', buttons)
        return pushes
                    

