class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = Node(homepage)
        self.firstPage = newNode
        self.lastPage = newNode
        self.currPage = newNode

    def visit(self, url: str) -> None:
        newPage = Node(url)
        self.currPage.next = newPage
        newPage.next = None
        newPage.prev = self.currPage
        self.currPage = newPage
        self.lastPage = newPage

    def back(self, steps: int) -> str:
        while self.currPage.prev and steps > 0:
            self.currPage = self.currPage.prev
            steps -= 1
        
        return self.currPage.val

    def forward(self, steps: int) -> str:
        while self.currPage.next and steps > 0:
            self.currPage = self.currPage.next
            steps -= 1
        
        return self.currPage.val

        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)