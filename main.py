import tkinter as tk
import random
import time

# Step 1: Define the warehouse and robot parameters
WAREHOUSE_WIDTH = 10
WAREHOUSE_HEIGHT = 10
CELL_SIZE = 50  # Size of each cell in pixels
DESTINATION = (7, 9)  # Updated destination according to your prompt

class Robot:
    def __init__(self, canvas, robot_id, start_position):
        self.canvas = canvas
        self.id = robot_id
        self.position = start_position
        self.target_position = DESTINATION
        self.rect = None  # This will store the robot's graphical representation
        self.moving = False
        self.move_time = 0  # Track movement time

    def draw(self):
        """ Draw or update the robot on the canvas. """
        if self.rect:
            self.canvas.delete(self.rect)
        x, y = self.position
        self.rect = self.canvas.create_rectangle(
            x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill="blue", outline="black"
        )

    def move_step(self):
        """ Move one step towards the target position. """
        if not self.moving:
            self.move_time += 1  # Increment the move time every tick
            if self.move_time < 10:  # Simulate moving for 1 second (0.1 m/s for 0.1 sec)
                x, y = self.position
                target_x, target_y = self.target_position

                if x < target_x:
                    x += 1
                elif x > target_x:
                    x -= 1

                if y < target_y:
                    y += 1
                elif y > target_y:
                    y -= 1

                self.position = (x, y)
                self.draw()  # Redraw the robot at its new position

            if self.move_time >= 10:  # After moving for 1 second
                self.moving = True
                self.move_time = 0  # Reset move time

        else:
            time.sleep(2)  # Pause for 2 seconds
            self.moving = False  # Allow the robot to move again

    def has_reached_destination(self):
        return self.position == self.target_position

# Step 2: Set up the tkinter window and grid
def initialize_warehouse(num_robots):
    window = tk.Tk()
    window.title("Warehouse Robot Simulation")

    # Canvas for drawing the warehouse grid
    canvas = tk.Canvas(window, width=WAREHOUSE_WIDTH * CELL_SIZE, height=WAREHOUSE_HEIGHT * CELL_SIZE)
    canvas.pack()

    # Draw grid lines for better visualization
    for i in range(WAREHOUSE_WIDTH):
        for j in range(WAREHOUSE_HEIGHT):
            canvas.create_rectangle(
                i * CELL_SIZE, j * CELL_SIZE, (i + 1) * CELL_SIZE, (j + 1) * CELL_SIZE, outline="gray"
            )

    # Step 3: Initialize robots at random positions
    robots = []
    for i in range(num_robots):
        while True:
            x = random.randint(0, WAREHOUSE_WIDTH - 1)
            y = random.randint(0, WAREHOUSE_HEIGHT - 1)
            if (x, y) != DESTINATION and all(robot.position != (x, y) for robot in robots):
                robot = Robot(canvas, i + 1, (x, y))
                robot.draw()
                robots.append(robot)
                break

    # Step 4: Run the simulation
    def run_simulation():
        while not all(robot.has_reached_destination() for robot in robots):
            for robot in robots:
                if not robot.has_reached_destination():
                    robot.move_step()
                    window.update()  # Refresh the window to show movement

        # Display completion message when all robots have reached the destination
        canvas.create_text(
            WAREHOUSE_WIDTH * CELL_SIZE // 2, WAREHOUSE_HEIGHT * CELL_SIZE // 2,
            text="All robots have reached the destination!",
            font=("Arial", 16), fill="green"
        )

    # Run the simulation in a separate thread to keep the UI responsive
    window.after(1000, run_simulation)  # Delay to let the UI load first
    window.mainloop()

# Start the simulation
num_robots = int(input("Enter the number of robots: "))
initialize_warehouse(num_robots)
