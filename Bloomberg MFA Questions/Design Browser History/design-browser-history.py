abc = ['a']

abc.insert(1, 'pepe')


# O(N) time | O(N) space
class BrowserHistory:

    def __init__(self, homepage: str):
        self.websites = [homepage]
        self.curr_pos = 0

    # O(N) time | O(1) space
    def visit(self, url: str) -> None:
        self.curr_pos += 1
        self.websites = self.websites[:self.curr_pos]
        self.websites.append(url)


    # O(1) time | O(1) space
    def back(self, steps: int) -> str:
        steps_back = 0

        if self.curr_pos - steps >= 0:
            steps_back = self.curr_pos - steps
            self.curr_pos = self.curr_pos - steps
        else:
            self.curr_pos = 0

        return self.websites[steps_back]

    # O(1) time | O(1) space
    def forward(self, steps: int) -> str:
        steps_forward = len(self.websites) - 1

        if self.curr_pos + steps < len(self.websites):
            steps_forward = self.curr_pos + steps
            self.curr_pos = self.curr_pos + steps
        else:
            self.curr_pos = len(self.websites) - 1

        return self.websites[steps_forward]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

if __name__ == '__main__':
    browser = BrowserHistory('leetcode.com')
    browser.visit('google.com')
    browser.visit('facebook.com')
    browser.visit('youtube.com')

    print(browser.back(1))
    print(browser.back(1))

    print(browser.forward(1))

    browser.visit('linkedin.com')

    print(browser.forward(2))

    print(browser.back(2))
    print(browser.back(7))









