import pygame
from pygame.math import Vector2
import math
from raycast_rays import Raycast

class DrawSchema():
    def __init__(self, level, player, screen, width, height, pos_x, pos_y):
        self.level = level
        self.screen = screen
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.player = player
        self.font = pygame.font.Font(None, 16)        
        self.raycast = Raycast(level, player, screen, width, height, pos_x, pos_y)
        pass

    def convert_x(self, player_pos_x):
        return self.width / (self.level.width * self.level.steps_rectangle_width  ) * player_pos_x + self.pos_x
    
    def convert_y(self, player_pos_y):
        return self.height / (self.level.height * self.level.steps_rectangle_height  ) * player_pos_y + self.pos_y

    def draw_rays(self, ray):
        

        #direction_multi = 1 if (self.player.angle >= math.pi) else -1
        #direction_grid_addition  = 1 if (self.player.angle >= math.pi) else 0

        color_rays =  (0, 0, 255)


        pygame.draw.line(self.screen, 
                        color_rays,
                        (self.convert_x(ray.get("start")[0]), self.convert_y(ray.get("start")[1])),
                        (self.convert_x(ray.get("end")[0]), self.convert_y(ray.get("end")[1])))

        #return {
        #    "start": (self.player.pos_x, self.player.pos_y),
        #    "end": ray_endpoint,
        #    "distance": ray_distance,
        #    "target_coordinates": ray_endpoint_level
        #}

    

    def draw_3d(self, pos_x, ray, alpha, view_angle, ray_view):

        max_color = 255
        min_color = 30

        color_wall = (max_color, max_color, max_color)
        
        max_wall_height = 300
        min_wall_height = 40
        max_distance = 400

        new_angel =  abs(alpha - view_angle)
        projection_sistance = ray.get("distance") * math.cos(new_angel)
        draw_height = max_wall_height - (max_wall_height / max_distance * projection_sistance)
        draw_height = (10/projection_sistance * 2500)

        """player_coord = self.player.get_coordinats()

        if ray.get("wall_direction") == 0:
            grid_distance = abs(ray.get("target_coordinates")[0] - player_coord.get("grid_pos_x"))
        else:
            grid_distance = abs(ray.get("target_coordinates")[1] - player_coord.get("grid_pos_y"))
        print(grid_distance)"""

        color_factor =  ray.get("distance") // 64 

        current_color = 255-(color_factor * 50)
        if current_color < 40:
            current_color = 40   

        pygame.draw.line(self.screen,
                         (current_color, current_color, current_color),
                         (self.width  + pos_x*1, (self.height / 2) - (draw_height / 2)),
                         (self.width  + pos_x*1, (self.height / 2) + (draw_height / 2)),
                         1
                         )
        
       
        
  


    def draw(self):
        color_area_border = (255, 255, 255)
        color_wall_border = (150, 100, 0)
        color_wall_fill = (255, 255, 0)
        color_grid = (50,50,50)
        color_player =  (0, 255, 255)

        #area
        pygame.draw.rect(self.screen, color_area_border , pygame.Rect(self.pos_x, self.pos_y , self.width, self.height),  2)

        #grid
        for x in range(1, self.level.width):
             draw_x = self.width / self.level.width * x
             pygame.draw.line(self.screen, 
                              color_grid,
                              Vector2(self.pos_x + draw_x, self.pos_y),
                              Vector2(self.pos_x + draw_x, self.pos_y + self.height ) )
             
        for y in range(1, self.level.height):
             draw_y = self.height / self.level.height * y
             pygame.draw.line(self.screen, 
                              color_grid,
                              Vector2(self.pos_x, draw_y + self.pos_y),
                              Vector2(self.pos_x + self.width, draw_y + self.pos_y))      

        #level_walls
        for y in range(0, self.level.width):   
            for x in range(0, self.level.width): 
                if self.level.level[y][x] == 1:
                    rect_width = self.width / self.level.width
                    rect_height = self.height / self.level.height
                    draw_x = rect_width * x
                    draw_y = rect_height * y
                    pygame.draw.rect(self.screen, 
                                     color_wall_border, 
                                     pygame.Rect(self.pos_x + draw_x + 1, 
                                                 self.pos_y + draw_y + 1, 
                                                 rect_width - 2, 
                                                 rect_height - 2))
        
        # player
        pygame.draw.circle(self.screen,
                           color_player,
                           (self.convert_x(self.player.pos_x) + self.pos_x,
                           self.convert_y(self.player.pos_y) + self.pos_y),
                            2)  
        
        pygame.draw.line(self.screen, 
                        color_player,
                        (self.convert_x(self.player.pos_x), self.convert_y(self.player.pos_y)),
                        (self.convert_x(self.player.pos_x + self.player.dx*30), self.convert_y(self.player.pos_y + self.player.dy*30)) )



        viewfield_angel = 1.0
        viewfield_steps = viewfield_angel / 700
        view_angle_left = self.player.angle - (viewfield_angel/2)
        if view_angle_left < 0:
            view_angle_left = (2*math.pi) + view_angle_left
        print()
        for x in range(700):
            if view_angle_left >= 2*math.pi:
                view_angle_left = 0.001
                  

            ray = self.raycast.getRay(view_angle_left )
            ray_view = self.raycast.getRay(self.player.angle )
            self.draw_rays(ray)
            view_angle_left += viewfield_steps
            self.draw_3d(x, ray, view_angle_left, self.player.angle, ray_view)

