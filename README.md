<div style="background-color:#f0f0f0; padding:10px; border-radius:8px;">
🚀 <b>مرحبا بك في مشروعي</b>
</div>
# Robot Grid Simulator

## Project Title and Purpose
This project is a robot simulator written in Python using object-oriented programming principles. It simulates the robot's movement on a grid starting from size (5,5) and its area is expandable according to the user's desire. Additional features were incorporated to control the battery and to reduce the error rate, the user was able to select the movement through a drop-down list. It was implemented with a simple interactive interface implemented using Streamlet.

## How to Run the Code
1. Clone this repository.
2. Navigate to the project directory in your terminal.
3. Create and activate a virtual environment:
   `python -m venv env`
   `source env/bin/activate` (or `.\env\Scripts\activate` on Windows)
4. Install the required libraries:
   `pip install -r requirements.txt`
5. Run the Streamlit application:
   `streamlit run robot_simulator/streamlit_app.py`
6. The application will open in your web browser, where you can control the robot.

## Features
The RobotSimulator class handles the core logic, while streamlit_app.py provides the user interface.

- **RobotSimulator Class**

1. __init__(self, grid_size, initial_battery, obstacles): Initializes the robot at (0, 0) facing NORTH with a customizable grid size, battery level, and a list of obstacles.

2. forward(): Moves the robot one step forward in its current direction, consuming battery.

3. diagonal(): Moves the robot one step diagonally (forward-right), consuming battery.

4. left(), right(): Turns the robot 90 degrees left or right, consuming a small amount of battery.

5. recharge(): Resets the robot's battery to 100%.

6. report(): Returns a string with the robot's current position, direction, and battery level.

7. _is_valid_move(self, new_x, new_y): A helper method to check if a move is within grid boundaries and not on an obstacle.
 
8. _consume_battery(self, command_type): A helper method to handle battery consumption for each command.

**User Interface (streamlit_app.py):**

1. st.sidebar.slider(): Allows the user to dynamically expand or shrink the grid size.

2. st.selectbox(): Provides a dropdown menu for selecting commands.

3. draw_grid(): Renders the grid with the robot and obstacles, adjusting for the grid's dynamic size.**

4. Visual indicators for battery level and robot direction.

