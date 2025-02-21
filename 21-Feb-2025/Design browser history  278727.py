# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = WebPage(homepage)
        self.current = self.homepage
        self.last = WebPage()
        self.homepage.next = self.last
        self.last.prev = self.homepage

    def visit(self, url: str) -> None:
        self.clearHistory()
        new_page = WebPage(url)
        self.current.next = new_page
        new_page.prev = self.current
        self.current = new_page
        new_page.next = self.last
        self.last.prev = new_page

    def clearHistory(self):
        self.current.next = self.last
        self.last.prev = self.current
    
    def returnHistory(self):
        ans = []
        curr = self.last
        while curr:
            ans.append(curr.url)
            curr = curr.prev
        
        ans_for = []
        fir = self.homepage
        while fir:
            ans_for.append(fir.url)
            fir = fir.next

        print(ans_for)        
        print(ans[::-1])
        print()
        print()

    def navigate(self, steps, dir_, stop) -> str:
        current = 0
        self.returnHistory()
        
        while self.current != stop and current < steps:
            current += 1
            if dir_ == 1:
                self.currrent = self.current.next
            else:
                self.current = self.current.prev

        return self.current

    def back(self, steps: int) -> str:
        current = 0

        while self.current != self.homepage and current < steps:
            current += 1
            self.current = self.current.prev

        return self.current.url

    def forward(self, steps: int) -> str:
        current = 0

        while self.current != self.last.prev and current < steps:
            current += 1
            self.current = self.current.next

        return self.current.url


        
class WebPage:
    def __init__(self, url = "---"):
        self.url = url
        self.prev = None
        self.next = None


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)