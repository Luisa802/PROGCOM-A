import pygame
import random
import math

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Arkanoid de Nubes")

clock = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 24)

BLANCO = (255,255,255)
ROJO = (255,80,80)
AZUL = (0,150,255)
VERDE = (0,200,0)
MORADO = (200,0,200)
AMARILLO = (255,220,0)

fondo = "desierto"

vidas = 5
puntos = 0
nivel = 1

barra = pygame.Rect(350,550,120,15)
vel_barra = 7

pelota = pygame.Rect(390,300,20,20)

vel_x = 4
vel_y = -4

color_pelota = ROJO

nubes = []

def crear_nubes():
    global nubes
    nubes = []

    for fila in range(4):
        for col in range(9):

            nube = pygame.Rect(70 + col*75, 60 + fila*40, 60, 30)
            nubes.append(nube)

crear_nubes()

dulces = []

class Dulce:

    def __init__(self,x,y):

        self.rect = pygame.Rect(x,y,20,20)

        self.tipo = random.choice([
        "color",
        "barra_grande",
        "barra_peque",
        "ciudad",
        "mar",
        "campo"
        ])

    def mover(self):
        self.rect.y += 3

    def dibujar(self):

        if self.tipo == "color":
            color = AMARILLO

        elif self.tipo == "barra_grande":
            color = VERDE

        elif self.tipo == "barra_peque":
            color = ROJO

        elif self.tipo == "ciudad":
            color = MORADO

        elif self.tipo == "mar":
            color = AZUL

        else:
            color = (0,255,150)

        pygame.draw.circle(pantalla,color,self.rect.center,10)

def dibujar_desierto():

    pantalla.fill((240,210,140))
    pygame.draw.rect(pantalla,(200,180,100),(0,450,800,150))

def dibujar_mar():

    pantalla.fill((80,160,255))
    pygame.draw.rect(pantalla,(40,120,220),(0,450,800,150))

def dibujar_campo():

    pantalla.fill((150,220,120))

    for i in range(30):
        x=random.randint(0,800)
        y=random.randint(450,600)

        pygame.draw.circle(pantalla,(255,100,200),(x,y),4)

def dibujar_ciudad():

    pantalla.fill((120,120,140))

    for i in range(10):
        x=i*80
        altura=random.randint(200,350)

        pygame.draw.rect(pantalla,(60,60,80),(x,600-altura,60,altura))

def dibujar_nube(rect):

    x,y,w,h = rect

    pygame.draw.circle(pantalla,BLANCO,(x+15,y+15),15)
    pygame.draw.circle(pantalla,BLANCO,(x+30,y+10),18)
    pygame.draw.circle(pantalla,BLANCO,(x+45,y+15),15)

def dibujar_pelota():

    cx,cy = pelota.center

    pygame.draw.circle(pantalla,color_pelota,(cx,cy),10)

    for i in range(12):

        ang = i*30
        rad = math.radians(ang)

        x1 = cx + math.cos(rad)*10
        y1 = cy + math.sin(rad)*10

        x2 = cx + math.cos(rad)*16
        y2 = cy + math.sin(rad)*16

        pygame.draw.line(pantalla,color_pelota,(x1,y1),(x2,y2),2)

ejecutando = True

while ejecutando:

    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando=False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and barra.left>0:
        barra.x -= vel_barra

    if teclas[pygame.K_RIGHT] and barra.right<ANCHO:
        barra.x += vel_barra

    pelota.x += vel_x
    pelota.y += vel_y

    if pelota.left<=0 or pelota.right>=ANCHO:
        vel_x *= -1

    if pelota.top<=0:
        vel_y *= -1

    if pelota.colliderect(barra):
        vel_y *= -1

    if pelota.bottom>ALTO:

        vidas -= 1

        pelota.x = random.randint(100,700)
        pelota.y = random.randint(200,350)

        vel_x = random.choice([-4,4])
        vel_y = -4

    for nube in nubes[:]:

        if pelota.colliderect(nube):

            nubes.remove(nube)

            vel_y *= -1

            puntos += 10

            if random.random() < 0.6:
                dulces.append(Dulce(nube.x,nube.y))

    if len(nubes) == 0:

        nivel += 1

        vel_x *= 1.2
        vel_y *= 1.2

        crear_nubes()

    for d in dulces[:]:

        d.mover()

        if d.rect.colliderect(barra):

            if d.tipo == "color":
                color_pelota = random.choice([ROJO,AZUL,VERDE,AMARILLO])

            if d.tipo == "barra_grande":
                barra.width += 40

            if d.tipo == "barra_peque":
                barra.width = max(60,barra.width-30)

            if d.tipo == "ciudad":
                fondo = "ciudad"

            if d.tipo == "mar":
                fondo = "mar"

            if d.tipo == "campo":
                fondo = "campo"

            dulces.remove(d)

    if fondo=="desierto":
        dibujar_desierto()

    if fondo=="mar":
        dibujar_mar()

    if fondo=="campo":
        dibujar_campo()

    if fondo=="ciudad":
        dibujar_ciudad()

    for nube in nubes:
        dibujar_nube(nube)

    for d in dulces:
        d.dibujar()

    pygame.draw.rect(pantalla,(50,50,50),barra)

    dibujar_pelota()

    texto1 = fuente.render("Puntos: "+str(puntos),True,(0,0,0))
    texto2 = fuente.render("Vidas: "+str(vidas),True,(0,0,0))
    texto3 = fuente.render("Nivel: "+str(nivel),True,(0,0,0))

    pantalla.blit(texto1,(10,10))
    pantalla.blit(texto2,(700,10))
    pantalla.blit(texto3,(360,10))

    if vidas <= 0:

        fin = fuente.render("GAME OVER",True,(0,0,0))

        pantalla.blit(fin,(340,300))

        pygame.display.update()

        pygame.time.delay(3000)

        ejecutando=False

    pygame.display.update()

pygame.quit()