class TextEditor:

    def __init__(self):
        self.book = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        # self.book.append(text)
        self.book = self.book[:(self.cursor)] + text + self.book[self.cursor:]
        # print("added text", self.book)
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        ans = min(self.cursor, k)
        old_cursor = self.cursor
        self.cursor -= k 
        self.cursor = max(0, self.cursor)
        self.book = self.book[:(self.cursor)] + self.book[old_cursor:]
        # print("in delete text", self.cursor)
        # print("in delete text", self.book)
        return ans

    def cursorLeft(self, k: int) -> str:
        # self.cursor = min(self.cursor-k, self.cursor)
        if self.cursor > k:
            self.cursor -= k
        else:
            self.cursor = 0
        if self.cursor <=10:
            return self.book[:self.cursor]
        # print("cursor left", self.book)

        return self.book[self.cursor-10:self.cursor]

    def cursorRight(self, k: int) -> str:
        # print("check",self.cursor)
        self.cursor = min(self.cursor+k, len(self.book))
        # print("check", self.book, self.cursor)
        if self.cursor <=10:
            return self.book[:self.cursor]
        return self.book[self.cursor-10:self.cursor]
        # -22: -12
        # cursor = 12  'leetpractice'[-10:]       -12+12
        # cursor = 11  'leetpractice'[-10-1:11].  -12+11
        # cursor = 6   'leetpractice'[-10-6:6]    -12+6





# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
