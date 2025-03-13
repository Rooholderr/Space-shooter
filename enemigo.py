import pygame

class Enemigo:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.ancho = 110
        self.alto = 110
        self.velocidad = 3
        self.color = "green"
        self.vida = 3
        self.imagen = pygame.image.load(r"C:\Users\ronal\Desktop\Python\Fotos\Malo.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        
    def dibujar(self,ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        #pygame.draw.rect(ventana,self.color,self.rect )
        ventana.blit(self.imagen, (self.x, self.y))
    
    
    def movimiento(self):
        self.y += self.velocidad