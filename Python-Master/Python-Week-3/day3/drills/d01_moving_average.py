# Drill 1: Moving Average from Data Stream
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        
    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.window_sum -= self.queue.popleft()
            
        self.queue.append(val)
        self.window_sum += val
        return self.window_sum / len(self.queue)

if __name__ == '__main__':
    m = MovingAverage(3)
    print(m.next(1)) # 1.0
    print(m.next(10)) # 5.5
    print(m.next(3)) # 4.666...
    print(m.next(5)) # 6.0
