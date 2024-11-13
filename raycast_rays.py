import math

class Raycast():
    def __init__(self, level, player, screen, width, height, pos_x, pos_y):
        self.level = level
        self.screen = screen
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.player = player
        pass

    def getRay(self, alpha) -> dict:

        if alpha == 0:
            alpha += 0.0000001
        player_pos = self.player.get_coordinats()
        startpoint = (player_pos.get("step_pos_x") , player_pos.get("step_pos_y")) 


        y_grid = 0
        x_grid = 0
        hi_ray_x = player_pos.get("step_pos_x") 
        hi_ray_y = player_pos.get("step_pos_y") 
        hi_endpoint = (self.player.pos_x, self.player.pos_y)

        if alpha >= math.pi:
            hi_yn = player_pos.get("step_pos_y") - (self.level.steps_rectangle_height * player_pos.get("grid_pos_y"))    
        else:
            hi_yn = (self.level.steps_rectangle_height * (player_pos.get("grid_pos_y")+1) - player_pos.get("step_pos_y") )
        hi_ys = self.level.steps_rectangle_height
        hi_xs = self.level.steps_rectangle_width / math.tan(alpha)        
        hi_xn =  hi_yn / math.tan(alpha)
        hi_y_addition = hi_yn
        hi_x_addition = hi_xn

        while y_grid in range(0, self.level.height) and (x_grid in range(0, self.level.width) ):
            if alpha >= math.pi:
                hi_ray_y -= hi_y_addition    
                hi_ray_x -= hi_x_addition
                y_grid = int((hi_ray_y - 1) // self.level.steps_rectangle_height) + 1
                x_grid = int((hi_ray_x - 1) // self.level.steps_rectangle_width)
                hi_level_y = y_grid - 1
                hi_level_x = x_grid                
            else:
                hi_ray_y += hi_y_addition    
                hi_ray_x += hi_x_addition   
                y_grid = int((hi_ray_y) // self.level.steps_rectangle_height)       
                x_grid = int((hi_ray_x) // self.level.steps_rectangle_width)    
                hi_level_y = y_grid
                hi_level_x = x_grid                

            hi_y_addition = hi_ys    
            hi_x_addition = hi_xs

            
            if (hi_level_y in range(0, self.level.height)) and (hi_level_x in range(0, self.level.width) ):
                if self.level.level[hi_level_y][hi_level_x] == 1:
                    break    
        hi_endpoint = (hi_ray_x, (y_grid) * self.level.steps_rectangle_height )               
        hi_distance = abs(math.dist(startpoint, hi_endpoint))

        y_grid = 0
        x_grid = 0
        vi_ray_x = player_pos.get("step_pos_x") 
        vi_ray_y = player_pos.get("step_pos_y") 
        vi_endpoint = (self.player.pos_x, self.player.pos_y)
        if (alpha>= 3/2*math.pi) or (alpha<= 1/2*math.pi):
            vi_xn = self.level.steps_rectangle_width * (player_pos.get("grid_pos_x") + 1) - player_pos.get("step_pos_x")     
        else:
            vi_xn = player_pos.get("step_pos_x") - (self.level.steps_rectangle_width * player_pos.get("grid_pos_x"))    
        vi_yn = vi_xn * math.tan(alpha)
        vi_xs = self.level.steps_rectangle_width 
        vi_ys = vi_xs * math.tan(alpha)
        vi_y_addition = vi_yn
        vi_x_addition = vi_xn        

        while y_grid in range(0, self.level.height) and (x_grid in range(0, self.level.width) ):
            if (alpha >= 3/2*math.pi) or (alpha <= 1/2*math.pi):
                vi_ray_y += vi_y_addition    
                vi_ray_x += vi_x_addition
                y_grid = int((vi_ray_y) // self.level.steps_rectangle_height)
                x_grid = int((vi_ray_x) // self.level.steps_rectangle_width)
                vi_level_y = y_grid
                vi_level_x = x_grid    
            else:
                vi_ray_y -= vi_y_addition    
                vi_ray_x -= vi_x_addition
                y_grid = int((vi_ray_y) // self.level.steps_rectangle_height) 
                x_grid = int((vi_ray_x) // self.level.steps_rectangle_width)
                vi_level_y = y_grid
                vi_level_x = x_grid -1   
                
            vi_y_addition = vi_ys    
            vi_x_addition = vi_xs    
            
            if (vi_level_y in range(0, self.level.height)) and (vi_level_x in range(0, self.level.width) ):
                if self.level.level[vi_level_y][vi_level_x] == 1:
                    break             
        
        vi_endpoint = (x_grid * self.level.steps_rectangle_width , vi_ray_y)    
        vi_distance = abs(math.dist(startpoint, vi_endpoint))

        if vi_distance <= hi_distance:            
            ray_endpoint = vi_endpoint
            ray_distance = vi_distance
            ray_endpoint_level = (vi_level_y,vi_level_x)
            wall_direction = 0
        else:
            ray_endpoint = hi_endpoint
            ray_distance = hi_distance
            ray_endpoint_level = (hi_level_y,hi_level_x)
            wall_direction = 1

        return {
            "start": (self.player.pos_x, self.player.pos_y),
            "end": ray_endpoint,
            "distance": ray_distance,
            "target_coordinates": ray_endpoint_level,
            "wall_direction": wall_direction
        }
