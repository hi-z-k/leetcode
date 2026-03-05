class Node:
    def __init__(self,link, prev=None, next=None):
        self.link = link
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(link=homepage)

    def visit(self, url: str) -> None:
        history = self.history
        newWebsite = Node(link=url)
        newWebsite.prev = history
        history.next = newWebsite
        self.history = newWebsite

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.history.prev:
                break
            self.history = self.history.prev
        return self.history.link
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.history.next:
                break
            self.history = self.history.next
        return self.history.link


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)