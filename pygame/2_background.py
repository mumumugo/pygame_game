from turtle import Screen
import pygame

pygame.init()  # reset (must have)

# screen size
screen_width = 480  # x length
screen_height = 640  # y length
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Mumu Game")  # game name

# background
background = pygame.image.load(
    "C:/Users/pe343/Downloads/pythonworkspace/pygame/background.png")

# event loop
running = True  # check is game is running
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생 하였나? (pygame을 위해서 무조건 적어야함)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생 하였나?(오른쪽 위 빨간 X표 )
            running = False
    screen.blit(background, (0, 0))  # background를 그려줌
    pygame.display.update()  # draw game display

pygame.quit()
