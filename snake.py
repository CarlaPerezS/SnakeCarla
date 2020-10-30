#snake.py
#Carla Perez, Aranza Garcia 
#juego snaka mejorado

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors  = ["green","blue","orange","purple","pink","yellow"] #lista de colores para la sepiente y para la comida
colorSnake = random.choice(colors) #elije el color de la serpiente aleatoriamente
colorFood= random.choice(colors) #elije el color de la comida aleatoriamente
if colorFood == colorSnake: #no se repite el color 
    colorSnake = random.choice(colors)



def change(x, y):
    #Direccion de la serpiente
    aim.x = x
    aim.y = y

def inside(head):
    #Regresa True si la cabeza esta dentro de los límites
    return -200 < head.x < 190 and -200 < head.y < 190
def insideFood(food):
    #Regresa True si la comida esta dentro de lo límites
    return -200 < food.x < 190 and -200 < food.y < 190

def move():
    #Mueve a la serpiente un segmento
    head = snake[-1].copy()
    head.move(aim)
    n= randrange(0,6)


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        write("Game Over", align="center", font=("Arial", 20, "bold")) #Escribe Game Over si la serpiente choca o se come a ella misma
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9,colorSnake)
    if body.x and body.y in snake == food.x and food.y:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    

    square(food.x, food.y, 9,colorFood)
    
    update()
    ontimer(move, 100)



def moveFood():
    #movimiento aleatorio de la comida
    food.x =+ randrange(-10,11,10)
    food.y =+ randrange(-10,11,10)
    if not insideFood(food):
        food.x = randrange(-15,15)*10
        food.y= randrange(-15,15)*10
    

    ontimer(moveFood, 500)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()
