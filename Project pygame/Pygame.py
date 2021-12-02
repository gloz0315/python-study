import pygame
import sys
import random

from pygame.examples.resizing_new import FPS
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 한칸을 20으로 잡기
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH/GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT/GRID_SIZE

WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255,0,0)

# 파이게임에서의 좌표는 위쪽이 -1, 아래쪽이 +1
UP = (0,-1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#하나의 사각형을 만들기
def draw_object(surface, color, position):
    r = pygame.Rect((position[0],position[1]), (GRID_SIZE,GRID_SIZE))
    pygame.draw.rect(surface, color, r)

class Snake(object):
    def __init__(self):
        self.create()
        self.color = GREEN

    def create(self):
        self.length = 2
        self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))] # 중앙에 생성
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT]) # 뱀이 랜덤하게 방향을 정의

    #뱀의 진행방향과 반대 방향으로 꺾는것을 방지하기 위해서서
    def control(self, xy):
        # 만약 진행방향과 반대방향으로 꺾었다면 변화 주지 않음
        if(xy[0] * -1, xy[1] * -1) == self.direction:
            return
        #그 외에는 진행방향으로 변화
        else:
            self.direction = xy

    def move(self):
        current = self.positions[0]
        x, y = self.direction
        # 창을 넘어가도 잘 나오게끔 만듬
        new = (((current[0] + (x * GRID_SIZE)) % WINDOW_WIDTH , (current[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT))


        if new in self.positions[1:]:
            #머리가 몸통에 부딪히면 다시 시작
            self.create()
        else:
            self.positions.insert(0, new)
            #뱀이 움직이면서 현재의 위치의 길이가 길이보다 클때 없애버리기 ( 즉, 이동하기 )
            if len(self.positions) > self.length:
                self.positions.pop()

    #뱀을 그리기
    def draw(self,surface):
        for i in self.positions:
            draw_object(surface, self.color, i)

class Feed(object):
    def __init__(self):
        self.position = (0,0)
        self.color = RED
        self.create()

    def create(self):
        #먹이가 생성될 위치에 대해서 랜덤한 값으로 position에 넣기 (y,x)
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)

    #사과 그리기
    def draw(self,surface):
        draw_object(surface, self.color, self.position)



if __name__ == "__main__":
    snake = Snake()
    feed = Feed()

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("지렁이 게임")
    surface = pygame.Surface(window.get_size()) # 윈도우의 실제 크기를 넣어줌
    surface = surface.convert()
    surface.fill(WHITE)
    clock = pygame.time.Clock() #게임에 시간을 넣어서 할 것
    pygame.key.set_repeat(1,40) #키의 시간 간격을 제어
    window.blit(surface, (0, 0)) # 배경 씌우기 (0,0)은 surface가 표시되는 위치


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.control(UP)
                elif event.key == K_DOWN:
                    snake.control(DOWN)
                elif event.key == K_LEFT:
                    snake.control(LEFT)
                elif event.key == K_RIGHT:
                    snake.control(RIGHT)

        surface.fill(WHITE)
        snake.move()
        speed = (FPS + snake.length) /2  # -> 속도 조절
        snake.draw(surface)
        feed.draw(surface)
        window.blit(surface,(0,0)) # 화면에 덮어씌움
        pygame.display.update() # 화면 업데이트
        clock.tick(speed) # -> 이걸 하지 않으면 지렁이가 미친듯이 움직임




