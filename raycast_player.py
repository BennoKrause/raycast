import math

class RaycastPlayer():
    def __init__(self, start_x, start_y, level):
        self.level = level
        self.pos_x = start_x
        self.pos_y = start_y
        self.steps_per_move = 6
        self.angle = 4.9
        self.dx = math.cos(self.angle) * self.steps_per_move
        self.dy = math.sin(self.angle) * self.steps_per_move
       
        pass

    def move_top(self):
        self.pos_x +=  self.dx 
        self.pos_y +=  self.dy 

    def move_down(self):
        self.pos_x -=  self.dx 
        self.pos_y -=  self.dy  

    def turn_left(self):
        self.angle -= 0.05
        if self.angle < 0:
            self.angle += 2 * math.pi
        self.dx = math.cos(self.angle) * self.steps_per_move
        self.dy = math.sin(self.angle) * self.steps_per_move       

    def turn_right(self):
        self.angle += 0.05
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi
        self.dx = math.cos(self.angle) * self.steps_per_move
        self.dy = math.sin(self.angle) * self.steps_per_move                 
    
    def get_coordinats(self):
        return {
            "step_pos_x": int(self.pos_x),
            "step_pos_y": int(self.pos_y),
            "grid_pos_x": int(self.pos_x) // self.level.steps_rectangle_width,
            "grid_pos_y": int(self.pos_y) // self.level.steps_rectangle_height,
        }