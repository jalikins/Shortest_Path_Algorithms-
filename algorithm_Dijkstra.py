def run_search(start_node, end_node, grid, pygame):
    # drawing colors
    LIGHT_BLUE = (173, 216, 230) 
    RED = (255, 0, 0) 
    GREEN = (0, 255, 0) 
    PINK = (255, 8, 127) 

    open_set = [start_node]
    closed_set = []

    while len(open_set) > 0:
        # keep the window responsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #
        # find the node we've discovered that is closest to the start
        lowest_index = 0
        for i in range(len(open_set)):
            if open_set[i].g < open_set[lowest_index].g:
                lowest_index = i
        
        current = open_set[lowest_index]

        # did hit the target?
        if current == end_node:
            print("Path found!")
            
            # backtrack to draw the final path
            temp = current
            while temp.previous:
                temp = temp.previous
                if temp != start_node:
                    temp.show(GREEN, 0)
            
            start_node.show(RED, 0)
            end_node.show(PINK, 0)
            return
        
        # move from open to closed list
        open_set.pop(lowest_index)
        closed_set.append(current)
        
        # color it blue to show checked it
        if current != start_node:
            current.show(LIGHT_BLUE, 0)
        
        # look at all neighboring spots
        for neighbor in current.neighbors:
            # skip walls and spots already processed
            if neighbor in closed_set or neighbor.obs:
                continue
            
            # calculate exact distance from start to this neighbor
            temp_g = current.g + neighbor.value
            
            if neighbor in open_set:
                # if already knew about this neighbor, but just found a faster route to it
                if temp_g < neighbor.g:
                    neighbor.g = temp_g
                    neighbor.previous = current
            else:
                # first time discovering this neighbor
                neighbor.g = temp_g
                neighbor.previous = current
                open_set.append(neighbor)
                
        pygame.time.delay(5) 

