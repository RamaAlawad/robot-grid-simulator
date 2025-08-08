class RobotSimulator:
    """
    A class to simulate a robot moving on a grid with added features.
    """
    def __init__(self, grid_size=(10, 10), initial_battery=100, obstacles=None):
        self.x = 0
        self.y = 0
        self.facing = 'NORTH'
        self.grid_size = grid_size
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.battery = initial_battery
        self.obstacles = obstacles if obstacles is not None else []
        self.move_costs = {'forward': 5, 'diagonal': 7, 'turn': 1}

    def _is_valid_move(self, new_x, new_y):
        """Checks if a new position is within grid boundaries and not an obstacle."""
        is_in_bounds = 0 <= new_x < self.grid_size[0] and 0 <= new_y < self.grid_size[1]
        is_obstacle = (new_x, new_y) in self.obstacles
        return is_in_bounds and not is_obstacle

    def _consume_battery(self, command_type):
        """Decreases battery level based on the command."""
        self.battery -= self.move_costs.get(command_type, 0)
        return self.battery > 0

    def forward(self):
        """Moves the robot one step forward and consumes battery."""
        if not self._consume_battery('forward'):
            return "Battery too low! Cannot move."

        old_x, old_y = self.x, self.y
        if self.facing == 'NORTH':
            self.y += 1
        elif self.facing == 'EAST':
            self.x += 1
        elif self.facing == 'SOUTH':
            self.y -= 1
        elif self.facing == 'WEST':
            self.x -= 1

        if not self._is_valid_move(self.x, self.y):
            self.x, self.y = old_x, old_y
            return "Invalid move: Out of bounds or obstacle."
        return f"Moved to ({self.x}, {self.y}). Battery: {self.battery}%"

    def diagonal(self):
        """Moves the robot diagonally (forward-right) and consumes battery."""
        if not self._consume_battery('diagonal'):
            return "Battery too low! Cannot move."

        old_x, old_y = self.x, self.y
        # Determine diagonal direction based on current facing direction
        if self.facing == 'NORTH':
            self.x += 1
            self.y += 1
        elif self.facing == 'EAST':
            self.x += 1
            self.y -= 1
        elif self.facing == 'SOUTH':
            self.x -= 1
            self.y -= 1
        elif self.facing == 'WEST':
            self.x -= 1
            self.y += 1
        
        if not self._is_valid_move(self.x, self.y):
            self.x, self.y = old_x, old_y
            return "Invalid move: Out of bounds or obstacle."
        return f"Moved diagonally to ({self.x}, {self.y}). Battery: {self.battery}%"

    def left(self):
        """Turns the robot left and consumes battery."""
        if not self._consume_battery('turn'):
            return "Battery too low! Cannot turn."
        current_index = self.directions.index(self.facing)
        new_index = (current_index - 1) % 4
        self.facing = self.directions[new_index]
        return f"Turned left. Now facing {self.facing}. Battery: {self.battery}%"

    def right(self):
        """Turns the robot right and consumes battery."""
        if not self._consume_battery('turn'):
            return "Battery too low! Cannot turn."
        current_index = self.directions.index(self.facing)
        new_index = (current_index + 1) % 4
        self.facing = self.directions[new_index]
        return f"Turned right. Now facing {self.facing}. Battery: {self.battery}%"
        
    def report(self):
        """Reports the robot's current position, direction, and battery."""
        return f"Position: ({self.x}, {self.y}), Facing: {self.facing}, Battery: {self.battery}%"