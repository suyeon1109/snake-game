"""
change(x,y) -> 스네이크의 방향을 책임지는
inside(head) -> 스네이크의 머리가 벽에 부딪혔을때 죽도록 또는 안에서만 return true 할 수 있도록
move() -> 스네이크가 움직이도록
    음식먹기
    랜덤한 곳에서 음식 띄우기
"""

from freegames import square, vector
from random import randrange
from turtle import *

food = vector(0,0)
snake = [vector(10,0)]
aim = vector(0,-10)


def change(x,y):
    #change snake direction
    aim.x = x
    aim.y = y
    # print(x, y)

def inside(head):
    #return true if head is inside the boundaries
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    #move snake forward one segemnt
    head = snake[-1].copy()
    head.move(aim)

    #when snake eat itself or touches boundary
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    if head == food:
        print("Score:", len(snake))
        food.x = randrange(-15,15) * 10
        food.y = randrange(-15,15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 120) #숫자 줄이면 속도 빨라짐



setup(420, 420, 370, 0) #height, width, 모니터에 이 창 띄울 x y 좌표
hideturtle() #거북이 모양 안쓸꺼니까
tracer(False)
listen() #socket class
onkey(lambda: change(10,0), 'Right')
onkey(lambda: change(-10,0), 'Left')
onkey(lambda: change(0,10), 'Up')
onkey(lambda: change(0,-10), 'Down')
move()
done()