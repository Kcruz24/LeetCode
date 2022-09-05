'''
You have a browser of one tab where you start on the homepage and you can visit another url,
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history
and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the
history and steps > x, you will forward only x steps. Return the current url after forwarding in
history at most steps.


'''
# O(N) Time | O(N) Space


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_pos = 0

    # O(N) Time
    def visit(self, url: str) -> None:
        self.curr_pos += 1
        self.history = self.history[:self.curr_pos]
        self.history.append(url)

    # O(1) Time
    def back(self, steps: int) -> str:
        if self.curr_pos - steps < 0:
            self.curr_pos = 0
        else:
            self.curr_pos -= steps

        return self.history[self.curr_pos]

    # O(1) Time
    def forward(self, steps: int) -> str:
        if steps + self.curr_pos >= len(self.history):
            self.curr_pos = len(self.history) - 1
        else:
            self.curr_pos += steps

        return self.history[self.curr_pos]


# Two Stack
# O(N) Time | O(N) Space
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []

    # O(1) Time
    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    # O(N) Time
    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history > 1):
            self.future.append(self.history.pop())
            steps -= 1

        return self.history[-1]

    # O(N) Time
    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.future):
            self.history.append(self.future.pop())
            steps -= 1

        return self.history[-1]


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
