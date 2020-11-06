# Source https://youtu.be/KiCBXu4P-2Y?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P
# William Fiset's Graph Theory playlist

# Search through a Maze or Dungeon Problem
# Returns shortest path from start (coordinates given) to end in a 
# maze
# Returns -1 if path is not found

# Time Complexity: O(Rows * Columns) for BFS
# Considering the fact that no.of vertices = rows*cols
# And no.of edges = 4*rows*cols
# Space Complexity: O(Rows * Columns)

from collections import deque
class Maze:
    def __init__(self, maze, start):
        self.maze = maze
        self.R = len(maze)
        self.C = len(maze[0])
        self.sr = start[0]
        self.sc = start[1]
        self.er = None
        self.ec = None
        self.rq = deque()
        self.cq = deque()
        
        
        self.move_count = 0
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0
        
        self.reached_end = False
        x = [[False]*len(maze[0]) for i in range(len(maze))]
        self.visited = x[:]
        y = [[None]*len(maze[0]) for i in range(len(maze))]
        self.prev = y[:]
        
        self.dr = [-1, 1, 0, 0]
        self.dc = [0, 0, 1, -1]
        
    
    def solve(self):
        self.rq.append(self.sr)
        self.cq.append(self.sc)
        
        self.visited[self.sr][self.sc] = True
        while len(self.rq) > 0:
            r = self.rq.popleft()
            c = self.cq.popleft()
            
            if self.maze[r][c] == 'E':
                self.reached_end = True
                self.er = r
                self.ec = c
                #self.prev[r][c] = (self.er, self.ec)
                break
            
            self.explore_neighbors(r, c)
            self.nodes_left_in_layer -= 1
            
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                self.move_count += 1
                
        if self.reached_end:
            return self.reconstructed_path()[::-1]
            
        return -1
    
    
    def reconstructed_path(self):
        path = []
        er = self.er
        ec = self.ec
        while (self.prev[er][ec] != self.prev[self.sr][self.sc]):
            path.append((self.prev[er][ec][0], self.prev[er][ec][1]))
            er,ec = self.prev[er][ec][0], self.prev[er][ec][1]
            
        return path
            
    def explore_neighbors(self, r, c):
        for i in range(4):
            rr = r + self.dr[i]
            cc = c + self.dc[i]
            
            if rr < 0 or cc < 0:
                continue
            if rr >= self.R or cc >= self.C:
                continue
            if self.visited[rr][cc]:
                continue
            if self.maze[rr][cc] == '#':
                continue
            
            self.rq.append(rr)
            self.cq.append(cc)
            
            self.visited[rr][cc] = True
            self.prev[rr][cc] = (r, c)
            self.nodes_in_next_layer += 1

# Starts here            
matrix = [['S', '.', '.', '#', '.', '.', '.'],
          ['.', '#', '.', '.', '.', '#', '.'],
          ['.', '#', '.', '.', '.', '.', '.'],
          ['.', '.', '#', '#', '.', '.', '.'],
          ['#', '.', '#', 'E', '.', '#', '.']]        
m = Maze(matrix, (0, 0))
print(m.solve())