class Robot:
    def __init__(self, robot_id, start_position, destination):
        self.id = robot_id
        self.position = start_position
        self.destination = destination

    def move_towards_destination(self):
        x, y = self.position
        dest_x, dest_y = self.destination

        # Move one step in the x or y direction towards the destination
        if x < dest_x:
            x += 1
        elif x > dest_x:
            x -= 1

        if y < dest_y:
            y += 1
        elif y > dest_y:
            y -= 1

        # Update the robot's position
        self.position = (x, y)

    def has_reached_destination(self):
        return self.position == self.destination

    def __str__(self):
        return f"Robot {self.id} at position {self.position}"
