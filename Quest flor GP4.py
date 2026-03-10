import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("black")  # Fondo negro para que los colores resalten
t = turtle.Turtle()
t.speed(0) # Velocidad máxima

# Paleta de colores que combinan (Tonos joya)
colors = ["#FF007F", "#FF55BB", "#BA55D3", "#9400D3", "#8A2BE2"]

def dibujar_flor():
    for i in range(100):
        # Cambia de color cada pocos trazos
        t.color(colors[i % len(colors)])
        
        # Dibujamos un pétalo circular
        t.circle(190 - i, 90)
        t.left(90)
        t.circle(190 - i, 90)
        t.left(18) # Rotación para el siguiente pétalo
        
    # Dibujar el centro de la flor
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Ejecutar el dibujo
dibujar_flor()

# Ocultar la tortuga y mantener la ventana abierta
t.hideturtle()
screen.mainloop()