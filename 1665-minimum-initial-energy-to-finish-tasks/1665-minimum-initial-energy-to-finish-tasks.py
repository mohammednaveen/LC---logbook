class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # sort by the diff (min-actual) because if we do tasks in that order we will get the most remaining energy
        tasks.sort(key=lambda x: x[1]-x[0], reverse=True)
        current_energy = 0
        total_needed = 0
        for actual, minimum in tasks:
            if current_energy < minimum:
                # we just need exactly the minimum to meet the requirement
                extra = minimum - current_energy
                current_energy += extra
                total_needed += extra
            # Spend the energy
            current_energy -= actual
        return total_needed