from collections import deque

class BrowserNode:
    def __init__(self, url, next: Optional['BrowserNode'] = None, prev: Optional['BrowserNode'] = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = BrowserNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        self.curr.next = BrowserNode(url, None, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev is None:
                break
            self.curr = self.curr.prev
        return self.curr.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next is None:
                break
            self.curr = self.curr.next
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)