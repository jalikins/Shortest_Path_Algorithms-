import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
import os

# Grid Node Class 
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
purple = (255, 8, 127)

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
        grid[i][j].show(white, 1)

# Draw boundaries
for i in range(0, row):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols-1][i].show(grey, 0)
    grid[cols-1][i].obs = True
    grid[i][row-1].show(grey, 0)
    grid[i][row-1].obs = True
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True

# PyGame Drawing Phase 
def mousePress(pos):
    t, w_m = pos
    g1 = int(t // (800 / cols))
    g2 = int(w_m // (800 / row))
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if not acess.obs:
            acess.obs = True
            acess.show(grey, 0) # Draw wall

end.show(purple, 0)
start.show(purple, 0)

print("Click and drag to draw walls. Press SPACE to start the algorithm.")

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            mousePress(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                drawing = False

# Once drawing is done, calculate neighbors for all open spaces
for i in range(cols):
    for j in range(row):
        grid[i][j].addNeighbors(grid)

# lock in here
def run_search_algorithm(start_node, end_node, grid_array):
    print("Algorithm started. Implement your logic here!")

run_search_algorithm(start, end, grid)

# Keep Window Open 
print("Finished. Close the PyGame window to exit.")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()