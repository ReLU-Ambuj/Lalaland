# Drill 1: Richest Customer Wealth
# Just standard row-wise iteration.

def maximum_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        # sum() is optimized in C
        max_wealth = max(max_wealth, sum(customer))
    return max_wealth

if __name__ == "__main__":
    print(maximum_wealth([[1,2,3],[3,2,1]])) # Expected: 6
