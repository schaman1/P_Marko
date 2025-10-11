import pygame

class Alert : 
    def __init__(self,screen,text,duration):
        self.screen = screen
        self.Size = (self.screen.get_width(),self.screen.get_height())
        
        self.text = text
        self.font = pygame.font.SysFont(None, 48)
        self.alert_text = self.font.render(self.text,True,(255,0,0))
        self.text_rect = self.alert_text.get_rect(center=(self.Size[0]//2, self.Size[1]//4))

        self.calcul_rect()

        self.text_rect.center = self.rect.center

        self.start_alert(duration)


    def calcul_rect(self):

        rect = self.text_rect.get_rect()
        self.rect = pygame.Rect(0,0,rect.width + 20,rect.height + 20)
        rect.midtop = (self.screen.get_width() // 2, 20)

    def draw(self):
        """Draw the alert message on top of the screen."""

        pygame.draw.rect(self.screen,(0,0,0),(0,0,self.Size[0],self.Size[1]//2),border_radius = 20)

        self.screen.blit(self.alert_text, self.text_rect)

    def start_alert(self,duration=2):
        """Display the alert for a certain duration."""
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < duration*1000:
            self.draw()