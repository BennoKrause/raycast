import pygame
from raycast_level import RaycastLevel
from raycast_schema import DrawSchema
from raycast_statistics import DrawStats
from raycast_player import RaycastPlayer


class Raycast():
    def __init__(self):
        self.width = 1024
        self.height = 768
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode([self.width*2, self.height])
        pygame.display.set_caption("Raycast")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 20)


        self.level =  RaycastLevel()   
        
        self.player = RaycastPlayer(230,
                                    230,
                                    self.level)
        self.schema = DrawSchema(self.level, self.player , self.screen, self.width, self.height, 0, 0)
        self.stats = DrawStats(self.level, self.player , self.screen, self.width, self.height, 0, 0)
        return
    



    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running  = False
                #if event.type == pygame.KEYDOWN:


            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move_top()
            if keys[pygame.K_s]:
                self.player.move_down()
            if keys[pygame.K_a]:
                self.player.turn_left()
            if keys[pygame.K_d]:
                self.player.turn_right()              

            self.screen.fill((0, 0, 0))

            self.schema.draw()
            self.stats.draw()
            # FPS berechnen
            fps = self.clock.get_fps()
            fps_text = self.font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
            # FPS-Anzeige auf Bildschirm anzeigen
            self.screen.blit(fps_text, (10, 10))            
        
            pygame.display.flip()   
            self.clock.tick(60)     
        pygame.quit()    

