class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        # Sort from most expensive to least expensive
        cost.sort(reverse=True)
        
        # Total sum minus every 3rd element starting from index 2
        return sum(cost) - sum(cost[2::3])