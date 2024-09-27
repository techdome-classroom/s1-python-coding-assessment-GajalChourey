class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_count = 0
        
        # Helper function for DFS
        def dfs(row: int, col: int):
            # Check boundaries
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[row][col] == 'W':
                return
            
            # Mark the cell as visited
            grid[row][col] = 'W'  # Change 'L' to 'W' to mark it as visited
            
            # Visit all four directions (up, down, left, right)
            dfs(row - 1, col)  # Up
            dfs(row + 1, col)  # Down
            dfs(row, col - 1)  # Left
            dfs(row, col + 1)  # Right
        
        # Traverse the grid
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'L':
                    # Found an unvisited land, start DFS
                    island_count += 1
                    dfs(i, j)
        
        return island_count

# Example Dispatches
solution = Solution()

dispatch1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
print(solution.getTotalIsles(dispatch1))  

dispatch2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]
print(solution.getTotalIsles(dispatch2))  
