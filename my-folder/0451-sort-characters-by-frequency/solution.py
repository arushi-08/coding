class Solution:
    def frequencySort(self, s: str) -> str:
        
        sitems = list(Counter(s).items())

        sitems.sort(key = lambda x: x[1], reverse=True)

        news = [k*v for k,v in sitems]

        return ''.join(news)
