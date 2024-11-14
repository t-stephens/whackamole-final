import pygame
import random



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        screen.fill("light green")
        mole_rect = mole_image.get_rect(topleft=(0, 0))
        screen.blit(mole_image, mole_rect)
        def draw_grid():
            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (i * 32, 0),
                    (i * 32, 512)
                )
            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (0, i * 32),
                    (640, i * 32)
                )
        draw_grid()
        clock = pygame.time.Clock()


        running = True


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = x // 32
                col = y // 32
                a, b = mole_rect.topleft
                mole_row, mole_col = a // 32, b // 32
                if mole_row == row and mole_col == col:
                    screen.fill("light green")
                    draw_grid()
                    a, b = random.randrange(0, 20), random.randrange(0, 16)
                    a *= 32
                    b *= 32
                    screen.blit(mole_image, mole_image.get_rect(topleft=(a, b)))
                    mole_rect = mole_image.get_rect(topleft=(a, b))


            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
