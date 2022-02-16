import pygame

pygame.init()  # reset (must have)

# screen size
screen_width = 480  # x length
screen_height = 640  # y length
pygame.display.set_mode((screen_width, screen_height))

# screen title setting

pygame.display.set_caption("Mumu Game")  # game name

# event loop
running = True  # check is game is running
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생 하였나? (pygame을 위해서 무조건 적어야함)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생 하였나?(오른쪽 위 빨간 X표 )
            running = False

pygame.quit()
