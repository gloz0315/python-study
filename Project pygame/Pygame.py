import pygame

pygame.init() # 파이게임 초기화

# 윈도우 창 설정하기
WINDOW_WIDTH = 800 # 가로 크기
WINDOW_HIGHT = 600 # 세로 크기

surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HIGHT)) # 화면 설정

pygame.display.set_caption("지렁이 게임") # 게임 이름
background = pygame.image.load("C:/Users/User/PycharmProjects/study/project pygame/image/image1.png.jpg")
surface.blit(background, (0,0)) # 배경 씌우기 (0,0)은 background가 표시되는 위치
done = False

def run():
    global done
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

        surface.blit(background, (0, 0))  # 배경 그리기 (0,0)은 background가 표시되는 위치
        pygame.display.update() #화면 그리기 업데이트

run() # 게임 실행
pygame.quit() # 나가기

