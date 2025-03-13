import pygame
from Personaje import Cubo
from enemigo import Enemigo
from bala import Bala
import random

# Inicializar Pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Space Shooter Ronald")

# Configuración de la ventana
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
FPS = 60
FUENTE = pygame.font.SysFont("Comic Sans", 40)

# Variables del juego
jugando = True
reloj = pygame.time.Clock()
vida = 5
puntos = 0    
tiempo_pasado = 0
tiempo_entre_enemigos = 500
cubo = Cubo(ANCHO/2, ALTO-160) 
enemigos = []
balas = []
ultima_bala = 0 
tiempo_entre_bala = 300

enemigos.append(Enemigo(ANCHO/2, 100))

# Cargar imagen de fondo
FONDO = pygame.image.load(r"C:\Users\ronal\Desktop\Python\Fotos\Ronald.jpg").convert()

# Función para disparar
def crear_bala():
    global ultima_bala
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_bala:
        balas.append(Bala(cubo.rect.centerx, cubo.rect.centery))
        ultima_bala = pygame.time.get_ticks()

# Función para gestionar las teclas y limitar el movimiento del personaje
def gestionar_teclas(teclas):
    if teclas[pygame.K_a] and cubo.x > 0:  # Evita que se salga por la izquierda
        cubo.x -= cubo.velocidad 
    if teclas[pygame.K_d] and cubo.x < ANCHO - cubo.rect.width:  # Evita que se salga por la derecha
        cubo.x += cubo.velocidad
    if teclas[pygame.K_SPACE]:
        crear_bala()

# Bucle principal del juego
while jugando and vida > 0:
    tiempo_pasado += reloj.tick(FPS)

    # Generar nuevos enemigos cada cierto tiempo
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0, ANCHO), -100))
        tiempo_pasado = 0
        
    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed()
    texto_vida = FUENTE.render(f"Vida: {vida}", True, "White")
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "White")
    
    gestionar_teclas(teclas)
    
    # Detectar eventos de salida
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
    
    # Dibujar elementos en la pantalla
    VENTANA.blit(FONDO, (0, 0))
    cubo.dibujar(VENTANA)

    # Control de enemigos
    for enemigo in enemigos[:]:  # Usamos `[:]` para evitar errores al eliminar elementos dentro del loop
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()
        
        # Colisión con el personaje
        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
            vida -= 1
            print(f'Te matan palomaso, te quedan {vida} vidas')
            enemigos.remove(enemigo)

        # Si el enemigo sale de la pantalla, se elimina pero **no suma puntos**
        if enemigo.y > ALTO:
            enemigos.remove(enemigo)
        
        # Colisión con las balas
        for bala in balas[:]:  # Evitar modificar la lista dentro del loop
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigo.vida -= 1
                balas.remove(bala)  # Se elimina la bala tras impactar
                
                # Solo suma puntos si el enemigo muere por impacto
                if enemigo.vida <= 0:
                    puntos += 1
                    enemigos.remove(enemigo)
        
    # Mover y dibujar balas
    for bala in balas[:]:  # Usamos `[:]` para evitar errores de modificación
        bala.dibujar(VENTANA)
        bala.movimiento()
        
    # Mostrar vida y puntuación
    VENTANA.blit(texto_vida, (20, 20))
    VENTANA.blit(texto_puntos, (20, 60))
    
    pygame.display.update()

# Salir del juego
pygame.quit()

# Guardar puntuación en un archivo
nombre = input("Ingresa tu nombre: ") 
with open('puntuaciones.txt', 'a') as archivo:
    archivo.write(f"{nombre} - {puntos}\n")

quit()
