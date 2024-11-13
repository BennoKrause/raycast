import pygame
from pygame.math import Vector2
import math

class DrawStats():
    def __init__(self, level, player, screen, width, height, pos_x, pos_y):
        self.level = level
        self.screen = screen
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.player = player
        self.font = pygame.font.Font(None, 16)
        pass

    def draw(self):
        color_area_border = (255, 255, 255)
        color_wall_border = (150, 100, 0)
        color_wall_fill = (255, 255, 0)
        color_grid = (50,50,50)
        color_player =  (0, 255, 255)    


        text_angel = self.font.render(f"Angle: {self.player.angle:.2f}", True, (255, 255, 255))
        text_direction = self.font.render(f"Direction: {self.player.dx:.2f}, {self.player.dy:.2f}", True, (255, 255, 255))
        player_pos = self.player.get_coordinats()
        text_player_steps = self.font.render(f"Player Steps: {player_pos.get("step_pos_x")}, {player_pos.get("step_pos_y")}", True, (255, 255, 255))
        text_player_grid = self.font.render(f"Player Grid: {player_pos.get("grid_pos_x")}, {player_pos.get("grid_pos_y")}", True, (255, 255, 255))
        self.screen.blit(text_angel, (self.pos_x  + self.width + 10, 10))    
        self.screen.blit(text_direction, (self.pos_x  + self.width + 10, 30))      
        self.screen.blit(text_player_steps, (self.pos_x  + self.width + 10, 50))      
        self.screen.blit(text_player_grid, (self.pos_x  + self.width + 10, 70))      
