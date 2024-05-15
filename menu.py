import pygame
pygame.font.init()
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.font = pygame.font.Font(None, 20)
        self.rect.w = self.width
        self.rect.h = self.height
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))