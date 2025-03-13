import pygame

class Cubo:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.ancho = 125
        self.alto = 125
        self.velocidad = 9.5
        self.color = "red"
        self.imagen = pygame.image.load(r"C:\Users\ronal\Desktop\Python\Fotos\bueno1.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        
    def dibujar(self,ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        # pygame.draw.rect(ventana,self.color,self.rect )
        ventana.blit(self.imagen, (self.x, self.y))
        