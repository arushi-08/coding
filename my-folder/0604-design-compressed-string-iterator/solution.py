class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed_string = compressedString
        self.full_string = ''
        i = 0
        
        while i < len(self.compressed_string):
            char = ''
            while self.compressed_string[i].isalpha():
                char += self.compressed_string[i]
                i += 1
            
            digit = ''
            while i < len(self.compressed_string) and self.compressed_string[i].isdigit():
                digit += self.compressed_string[i]
                i += 1
            
            self.full_string += char * int(digit)

        self.idx = 0

    def next(self) -> str:
        if self.idx < len(self.full_string):
            self.idx += 1
            return self.full_string[self.idx - 1]
        return ' '

    def hasNext(self) -> bool:
        return self.idx < len(self.full_string)



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
