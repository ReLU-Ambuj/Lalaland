# Drill 1: Daily Temperatures
def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = [] # stores indices
    
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index
        stack.append(i)
        
    return ans

if __name__ == '__main__':
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))
    # Expected: [1,1,4,2,1,1,0,0]
