class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.chain = ListNode(homepage)
        self.currchain = self.chain

    def visit(self, url: str) -> None:
        self.currchain.next = None
        self.currchain.next = ListNode(url)
        self.currchain.next.prev = self.currchain
        self.currchain = self.currchain.next

    def back(self, steps: int) -> str:
        while self.currchain.prev and steps:
            self.currchain = self.currchain.prev
            steps -= 1
        return self.currchain.val

    def forward(self, steps: int) -> str:
        while self.currchain.next and steps:
            self.currchain = self.currchain.next
            steps -= 1
        return self.currchain.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
