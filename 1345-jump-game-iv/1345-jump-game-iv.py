class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Step 1: Map each value to all its indices
        value_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_to_indices[val].append(i)
            
        # Step 2: Initialize BFS
        queue = deque([(0, 0)]) # (current_index, current_steps)
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            # Target reached
            if idx == n - 1:
                return steps
            
            # Explore neighbors
            neighbors = []
            
            # Neighbor option 1: i + 1
            if idx + 1 < n:
                neighbors.append(idx + 1)
            # Neighbor option 2: i - 1
            if idx - 1 >= 0:
                neighbors.append(idx - 1)
            # Neighbor option 3: Same value indices
            if arr[idx] in value_to_indices:
                neighbors.extend(value_to_indices[arr[idx]])
                # Crucial optimization: clear the list so we don't traverse it again
                del value_to_indices[arr[idx]]
                
            # Process valid neighbors
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
                    
        return -1