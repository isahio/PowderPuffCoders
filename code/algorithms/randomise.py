import random


class Random:
    def __init__(self, grid):
        self.grid = grid

    def execute(self):
        """ Folds an entire protein by generating random directions """
        
        # Right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        location = (0, 0)

        # Keep connecting amino acids until the whole protein is folded
        for amino_id, amino in self.grid.amino_acids.items():
            # Check that the location of the amino acid is not already in use
            while True:
                direction = random.choice(directions)
                next_pos = location[0] + direction[0], location[1] + direction[1]
                
                # Check if the location falls outside the grid size (AKA length of the protein)
                if self.grid.is_valid(next_pos):
                    # Update the location of the amino acid
                    amino.update_loc(next_pos)
                    
                    # Add position to used locations
                    self.grid.locations.add(next_pos)
                    break
                
            location = next_pos

            # Check what the move was and add it to the history of moves
            if amino_id != self.grid.max_grid_size - 1:
                self.grid.add_move(direction, amino_id)
