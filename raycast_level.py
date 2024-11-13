class RaycastLevel:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.level = [
            [1,1,1,1,1,1,1,1],
            [1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1],
            [1,0,0,0,0,1,0,1],
            [1,0,0,0,0,0,0,1],
            [1,0,0,0,1,1,1,1],
            [1,1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1]
        ]
        self.steps_rectangle_width = 64
        self.steps_rectangle_height = 64
        pass