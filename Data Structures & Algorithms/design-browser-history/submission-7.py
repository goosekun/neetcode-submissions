
class BrowserHistory:
    def __init__(self, homepage: str = "neetcode.com"):
        self.history = [homepage]
        self.current_page_index = 0

    def visit(self, url: str) -> None:
        self.delete_forward_history()
        self.history.append(url)
        self.current_page_index += 1

    def back(self, steps: int) -> str:
        self.current_page_index = max(0, self.current_page_index - steps)
        return self.history[self.current_page_index] if self.history else ""  
            

    def forward(self, steps: int) -> str:
        self.current_page_index = min(len(self.history) - 1, self.current_page_index + steps)
        return self.history[self.current_page_index]  

    def delete_forward_history(self) -> None:
        length = len(self.history)
        if self.current_page_index < length:
            curr = self.current_page_index
            del self.history[curr+1:]
            
        return 


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)