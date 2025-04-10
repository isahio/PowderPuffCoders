import random


class Greedy:
    def __init__(self, grid):
        self.best_grid = grid
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def execute(self):
        location = (0, 0)
        self.best_grid.amino_acids[0].update_loc(location)
        self.best_grid.locations.add(location)

        for amino_id, amino in list(self.best_grid.amino_acids.items())[1:]:
            # Initialize variables
            min_score = float('inf')
            best_direction = None

            # Generating a randomized list of directions
            random_directions = self.directions[:]
            random.shuffle(random_directions)

            for direction in random_directions:
                next_pos = (location[0] + direction[0], location[1] + direction[1])
                
                if self.best_grid.is_valid(next_pos):
                    # Temporarily place the amino acid in the grid and calculate the score
                    amino.update_loc(next_pos)
                    self.best_grid.locations.add(next_pos)
                    score = self.best_grid.compute_score()

                    if score < min_score:
                        min_score = score
                        best_direction = direction

                    # Remove the amino acid from the temporary location
                    amino.update_loc(None)
                    self.best_grid.locations.remove(next_pos)

            # If no direction was found that improves the score, take a random direction
            if best_direction is None:
                print("????")
                best_direction = random.choice(random_directions)

            next_pos = (location[0] + best_direction[0], location[1] + best_direction[1])
            amino.update_loc(next_pos)
            self.best_grid.locations.add(next_pos)
            location = next_pos

            self.best_grid.add_move(best_direction, amino_id)

                
    def get_best_configuration(self):
        return self.best_grid