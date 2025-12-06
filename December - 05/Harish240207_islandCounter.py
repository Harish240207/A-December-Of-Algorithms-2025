# December 05 - Island Counter
# Input:
#   Line 1: R C (rows and columns)
#   Next R lines: C integers (0 or 1) each
#
# Output:
#   Single integer: number of islands (groups of connected 1's using 4-directional adjacency)

from collections import deque

def count_islands(grid, R, C):
    visited = [[False] * C for _ in range(R)]

    def bfs(start_r, start_c):
        # BFS starting from (start_r, start_c)
        queue = deque()
        queue.append((start_r, start_c))
        visited[start_r][start_c] = True

        # 4-directional moves: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

    islands = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1 and not visited[r][c]:
                islands += 1
                bfs(r, c)

    return islands


def main():
    # Read R and C
    R, C = map(int, input().split())

    # Read the grid
    grid = []
    for _ in range(R):
        row = list(map(int, input().split()))
        # ensure row has exactly C elements
        row = row[:C]
        grid.append(row)

    result = count_islands(grid, R, C)
    print(result)


if __name__ == "__main__":
    main()
