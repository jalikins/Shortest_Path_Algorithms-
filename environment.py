import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
import os

from algorithm_Dijkstra import run_search

# Grid Node Class (GRAPH INFO)
class spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1

    def show(self, color, st):
        if not self.closed:
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()

    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        if i < cols-1 and not grid[self.i + 1][j].obs:
            self.neighbors.append(grid[self.i + 1][j])
        if i > 0 and not grid[self.i - 1][j].obs:
            self.neighbors.append(grid[self.i - 1][j])
        if j < row-1 and not grid[self.i][j + 1].obs:
            self.neighbors.append(grid[self.i][j + 1])
        if j > 0 and not grid[self.i][j - 1].obs:
            self.neighbors.append(grid[self.i][j - 1])

cols = 50
row = 50
w = 800 / cols
h = 800 / row

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
white = (255, 255, 255)
pink = (255, 8, 127)
orange = (255, 165, 0)

# Grid Initialization
grid = [[spot(i, j) for j in range(row)] for i in range(cols)]

start = grid[12][5]
end = grid[3][6]

# Tkinter Start/End Selector 
def onsubmit():
    global start, end
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()

window = Tk()
window.title("Setup")
Label(window, text='Start(x,y) [e.g. 12,5]: ').grid(row=0, pady=3)
startBox = Entry(window)
startBox.insert(0, "12,5")
startBox.grid(row=0, column=1, pady=3)

Label(window, text='End(x,y) [e.g. 3,6]: ').grid(row=1, pady=3)
endBox = Entry(window)
endBox.insert(0, "3,6")
endBox.grid(row=1, column=1, pady=3)

Button(window, text='Submit', command=onsubmit).grid(columnspan=2, row=3, pady=10)
window.mainloop()

# PyGame Setup 
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pathfinding Algorithm Sandbox")

# Draw initial empty grid
for i in range(cols):
    for j in range(row):
        pygame.draw.rect(screen, white, (i * w, j * h, w, h), 1)

# Draw boundaries
for i in range(0, row):
    grid[0][i].obs = True
    pygame.draw.rect(screen, grey, (0 * w, i * h, w, h), 0)
    
    grid[cols-1][i].obs = True
    pygame.draw.rect(screen, grey, ((cols-1) * w, i * h, w, h), 0)
    
    grid[i][row-1].obs = True
    pygame.draw.rect(screen, grey, (i * w, (row-1) * h, w, h), 0)
    
    grid[i][0].obs = True
    pygame.draw.rect(screen, grey, (i * w, 0 * h, w, h), 0)


def save_map(filename="saved_map.txt"):
    with open(filename, "w") as f:
        # Loop through rows (y) then columns (x) so the text file matches the screen visually
        for j in range(row):
            line = ""
            for i in range(cols):
                if grid[i][j].obs:
                    line += "1"
                else:
                    line += "0"
            f.write(line + "\n")
    print(f"Map saved to {filename}")

def load_map(filename="saved_map.txt"):
    if not os.path.exists(filename):
        print("No saved map found!")
        return
        
    with open(filename, "r") as f:
        lines = f.readlines()
        for j, line in enumerate(lines):
            line = line.strip()
            # Stop if the text file doesn't match 
            if j >= row: break 
            
            for i, char in enumerate(line):
                if i >= cols: break
                
                # Apply walls
                acess = grid[i][j]
                if char == "1" and acess != start and acess != end:
                    acess.obs = True
                    acess.show(grey, 0)
    print(f"Map loaded from {filename}")

    
# PyGame Drawing Phase 
def mousePress(pos, button_type):
    t, w_m = pos
    g1 = int(t // (800 / cols))
    g2 = int(w_m // (800 / row))
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if button_type == "left" and not acess.obs:
            acess.obs = True
            acess.show(grey, 0) # Draw wall
        elif button_type == "right" and not acess.obs:
            acess.value = 2 # Set weight to 2
            acess.show(orange, 0) # Draw orange weight

end.show(pink, 0)
start.show(pink, 0)


print("Commands: Left Click to draw walls. Right Click to draw weights.")
print("'S' to Save. 'L' to Load. SPACE to start.")

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Left click draws walls
        if pygame.mouse.get_pressed()[0]:
            mousePress(pygame.mouse.get_pos(), "left")
            
        # Right click draws weights
        if pygame.mouse.get_pressed()[2]:
            mousePress(pygame.mouse.get_pos(), "right")
            
        # Keyboard commands
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                drawing = False  
            elif event.key == pygame.K_s:
                save_map()       
            elif event.key == pygame.K_l:
                load_map()

# Once drawing is done, calculate neighbors for all open spaces
for i in range(cols):
    for j in range(row):
        grid[i][j].addNeighbors(grid)


run_search(start, end, grid, pygame) #changes depending on which file is imported

# Keep Window Open 
print("Finished. Close the PyGame window to exit.")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()