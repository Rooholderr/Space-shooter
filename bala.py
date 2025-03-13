import pygame

class Bala:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 12
        self.color = "white"
        self.imagen = pygame.image.load(r"C:\Users\ronal\Desktop\Python\Fotos\malbala.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        
    def dibujar(self,ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        #pygame.draw.rect(ventana,self.color,self.rect )
        ventana.blit(self.imagen, (self.x, self.y))
    
    
    def movimiento(self):
        self.y -= self.velocidad