# Browser History using Doubly Linked List

class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node
        print(f"Visited: {self.curr.url}")

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        print(f"Back to: {self.curr.url}")
        return self.curr.url

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        print(f"Forward to: {self.curr.url}")
        return self.curr.url

if __name__ == '__main__':
    b = BrowserHistory("google.com")
    b.visit("leetcode.com")
    b.visit("github.com")
    b.back(1)
    b.back(1)
    b.forward(1)
