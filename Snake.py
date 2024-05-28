import pygame

size = [450, 600]
FRAME_COLOR = (0, 255, 204)  # цвета в РГБ
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (204, 255, 255)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1



screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = BLUE_COLOR
            else:
                color = WHITE_COLOR
            pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             20 + row * SIZE_BLOCK + MARGIN * (row + 1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])

    pygame.display.flip()


