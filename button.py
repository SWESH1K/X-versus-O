import pygame

class Button:
    def __init__(self, x, y, image, scale = 1) -> None:
        width = image.get_width()
        height = image.get_height()
        
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # mouse position
        pos = pygame.mouse.get_pos()

        # check mouse hover and click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y) )
        #pygame.display.update()

        return action