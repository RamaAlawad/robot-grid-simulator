import streamlit as st
from robot import RobotSimulator

# Configure the Streamlit page layout and title
st.set_page_config(page_title="Robot Grid Simulator", layout="wide")
st.title("Robot Grid Simulator ")

st.markdown("---")

# UI elements for user to set grid size
st.sidebar.header("Grid and Obstacle Settings")
grid_width = st.sidebar.slider("Grid Width", min_value=5, max_value=20, value=5, step=1)
grid_height = st.sidebar.slider("Grid Height", min_value=5, max_value=20, value=5, step=1)

# Set the grid size dynamically based on user input
current_grid_size = (grid_width, grid_height)

# Fixed obstacles, ensure they are within the initial grid size
OBSTACLES = [(2, 1), (3, 2)]

# Initialize robot and reset it if grid size changes
if 'robot' not in st.session_state or st.session_state.grid_size != current_grid_size:
    st.session_state.robot = RobotSimulator(grid_size=current_grid_size, obstacles=OBSTACLES)
    st.session_state.grid_size = current_grid_size
    st.toast(f"Grid size changed to {current_grid_size}. Robot has been reset.", icon="🔄")


# Function to draw the grid and its contents
def draw_grid():
    grid = [['⚪️' for _ in range(st.session_state.grid_size[0])] for _ in range(st.session_state.grid_size[1])]
    
    # Place obstacles on the grid
    for ox, oy in st.session_state.robot.obstacles:
        # Check if the obstacle is within the current grid size before placing it
        if 0 <= ox < st.session_state.grid_size[0] and 0 <= oy < st.session_state.grid_size[1]:
            grid[st.session_state.grid_size[1] - 1 - oy][ox] = '🚧'

    # Use different emojis based on the robot's direction
    direction_emojis = {
        'NORTH': '⬆️',
        'EAST': '➡️',
        'SOUTH': '⬇️',
        'WEST': '⬅️'
    }
    robot_emoji = direction_emojis.get(st.session_state.robot.facing, '🤖')

    # Place the robot on the grid only if it has battery
    if st.session_state.robot.battery > 0:
        # Check if the robot's position is within the current grid size before placing it
        if 0 <= st.session_state.robot.x < st.session_state.grid_size[0] and 0 <= st.session_state.robot.y < st.session_state.grid_size[1]:
            grid[st.session_state.grid_size[1] - 1 - st.session_state.robot.y][st.session_state.robot.x] = robot_emoji
    
    # Display the grid in markdown
    st.markdown("### Grid View")
    for row in grid:
        st.markdown(' '.join(row), unsafe_allow_html=True)

# Handles the command execution and updates the UI
def handle_command(command):
    try:
        # Check if battery is completely depleted before processing command
        if command != "recharge" and st.session_state.robot.battery <= 0:
            st.toast("Battery is completely depleted! Robot is inoperative. Please recharge.", icon="🚨")
            return

        if command == "forward":
            message = st.session_state.robot.forward()
        elif command == "diagonal":
            message = st.session_state.robot.diagonal()
        elif command == "left":
            message = st.session_state.robot.left()
        elif command == "right":
            message = st.session_state.robot.right()
        elif command == "recharge":
            message = st.session_state.robot.recharge()
        elif command == "report":
            message = st.session_state.robot.report()
        else:
            message = f"Invalid command: '{command}'. Allowed commands are: forward, diagonal, left, right, report, recharge."
        
        st.toast(message, icon="✅")
    except Exception as e:
        st.toast(f"An error occurred: {e}", icon="🚨")

# UI Layout with two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Controls")
    # A dropdown menu for easy command selection
    command = st.selectbox(
        "Select a command:",
        ('forward', 'diagonal', 'left', 'right', 'report', 'recharge')
    )
    if st.button("Execute Command"):
        handle_command(command)

    # Display robot status
    st.markdown("---")
    # Change battery icon based on charge level
    battery_icon = "🔋" if st.session_state.robot.battery > 20 else "🪫"
    st.markdown(f"**Battery Level: {st.session_state.robot.battery}% {battery_icon}**")
    st.markdown(f"**{st.session_state.robot.report()}**")
    if st.session_state.robot.battery <= 0:
        st.warning("Battery is empty! Please recharge.")

with col2:
    draw_grid()
