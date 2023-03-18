class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.top = 0
        

    def visit(self, url: str) -> None:
       
        self.stack = self.stack[:self.top + 1] + [url]
        self.top += 1
        

    def back(self, steps: int) -> str:
        self.top = max(0 , self.top - steps)
        return self.stack[self.top]

    def forward(self, steps: int) -> str:
        self.top = min((len(self.stack) - 1)  , self.top + steps)
        return self.stack[self.top]




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
