def run_search(start_node, end_node, grid, pygame):
    def heuristic(n1, n2):
        return abs(n1.i - n2.i) + abs(n1.j - n2.j)

    # drawing colors
    LIGHT_BLUE = (173, 216, 230) 
    RED = (255, 0, 0) 
    GREEN = (0, 255, 0) 
    PINK = (255, 8, 127) 

    open_set = [start_node]
    closed_set = []

    while len(open_set) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # find the node with the lowest f score
        lowest_index = 0
        for i in range(len(open_set)):
            if open_set[i].f < open_set[lowest_index].f:
                lowest_index = i
        
        current = open_set[lowest_index]

        # did we reach the target?
        if current == end_node:
            
            # retrace steps to draw the final path in green
            temp = current
            while temp.previous:
                temp = temp.previous
                if temp != start_node:
                    temp.show(GREEN, 0)
            
            start_node.show(RED, 0)
            end_node.show(PINK, 0)
            return
        
        # move current node from open to closed
        open_set.pop(lowest_index)
        closed_set.append(current)
        
        # color it blue 
        if current != start_node:
            current.show(LIGHT_BLUE, 0)
        
        # check all the surrounding spots
        for neighbor in current.neighbors:
            # skip walls and places already checked
            if neighbor in closed_set or neighbor.obs:
                continue
            
            # g cost is distance from start. neighbor costs whatever its value is 
            temp_g = current.g + neighbor.value
            
            better_path = False
            if neighbor in open_set:
                # if we found a shorter way to get to this neighbor, update it
                if temp_g < neighbor.g:
                    neighbor.g = temp_g
                    better_path = True
            else:
                # first time seeing this neighbor
                neighbor.g = temp_g
                better_path = True
                open_set.append(neighbor)
                
            # if this is the best path to the neighbor so far, update scores and pointer
            if better_path:
                neighbor.h = heuristic(neighbor, end_node)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous = current 
        
        pygame.time.delay(5) 
    