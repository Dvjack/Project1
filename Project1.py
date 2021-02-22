# Here is project 1 for ENPM 661
import numpy as np
import queue as q

if __name__ == "__main__":
    # Test case 1
    # Matrix =        [[1, 2, 3, 4], 
    #                 [5, 6, 0, 8], 
    #                 [9, 10, 7, 12], 
    #                 [13, 14, 11, 15]]

    # Test case 2
    # Matrix =        [[1, 0, 3, 4], 
    #                 [5, 2, 7, 8], 
    #                 [9, 6, 10, 11], 
    #                 [13, 14, 15, 12]]

    # Test case 3
    # Matrix =        [[0, 2, 3, 4], 
    #                 [1, 5, 7, 8], 
    #                 [9, 6, 11, 12], 
    #                 [13, 10, 14, 15]]

    # Test case 4
    # Matrix =        [[5, 1, 2, 3], 
    #                 [0, 6, 7, 4], 
    #                 [9, 10, 11, 8], 
    #                 [13, 14, 15, 12]]

    # Test case 5
    # Matrix =        [[1, 6, 2, 3], 
    #                 [9, 5, 7, 4], 
    #                 [0, 10, 11, 8], 
    #                 [13, 14, 15, 12]]

    # Small test
    Matrix =        [[1, 0, 3], 
                    [4, 5, 6], 
                    [7, 2, 8]]

    # Smallest Test
    # Matrix =        [[1, 2], 
                    # [0, 3 ]]

    
    
    # making the matrix into a numpy array             

    Node_State_i = np.asarray(Matrix)

    # Turning the array into a list

    State = Node_State_i.flatten()
    size = Node_State_i.shape[0]
    print(f'State is: {State}')

    
    # Generating the goal state for any case
    goal_state = list(range(1,size**2))
    goal_state.append(0)
    
    # Initializing the Queue and visited list
    visited = [State]
    parent_q = q.Queue()
    parent_q.put_nowait(State)

    # Function that calcultates location of blank tile
    # In the 4x4 matrix and returns the output as an index

    # Function to find the blank tile

    def find_blank_tile(array):

        # grab index of where the value of the index of the state is 0
        blank_tile = np.where(array == 0)[0][0]
       
        # print(f'blank tile location is: {blank_tile}')
        
        return blank_tile
        

    # Function used to move the blank tile when given the coordinates of the blank tile, original state, amd direction to move
    def Action_Move(zero_col, zero_row, parent_state, direction):
        
        next_pos = (zero_col + direction[0], zero_row + direction[1])
        
        # If the move is legal then swap the blank space with the next position
        if next_pos[0] < size and next_pos[0] >= 0 and next_pos[1] < size and next_pos[1] >= 0:
            
            next_pos_index = (next_pos[1] * size) + next_pos[0]
            zero_loc = (zero_row * size) + zero_col
            # print(f'next_pos_index is: {next_pos_index}')
            # print(f'zero_loc: {zero_loc}')

            curr_state = parent_state.copy()
            print(f'current State is: {curr_state}')
            
            temp = curr_state[zero_loc]
            curr_state[zero_loc] = curr_state[next_pos_index]
            curr_state[next_pos_index] = temp
            # print(np.all(curr_state == visited[0]))
            # print(np.any(np.all(curr_state not in visited)))

            # If the current state isn't visited then append it to the visited list and add it to the queue            
            if np.any([np.any(curr_state != visited_i) for visited_i in visited]):

                visited.append(curr_state)
                parent_q.put_nowait(curr_state)

                # Let us know when we are at the goal state and return true
                if np.all(curr_state == goal_state):
                    print("Goal has been reached")
                    print(f'Puzzle is: {curr_state}')
                    return True
        return False 
        
    # Splitting the blank space index into rows and columns
    blank_tile = find_blank_tile(State)
    blank_tile_col =  blank_tile % size
    # print(f'blank col is: {blank_tile_col}')
    
    blank_tile_row = (blank_tile//size) 
    # print(f'blank row is: {blank_tile_row}')
    
    
i =0
while i<6:

    print(f'I is:{i}')
    parent_state = parent_q.get()
    Action_Move(blank_tile_col,blank_tile_row, parent_state, (0,-1))
    print(list(parent_q.queue))
    Action_Move(blank_tile_col,blank_tile_row, parent_state, (0,1))
    print(list(parent_q.queue))
    Action_Move(blank_tile_col,blank_tile_row, parent_state, (-1,0))
    print(list(parent_q.queue))
    Action_Move(blank_tile_col,blank_tile_row, parent_state, (1,0))
    

    print(f'Parent State is: {parent_state}')
    i += 1

    
# else:
    # print("The Queue is empty")
    
            