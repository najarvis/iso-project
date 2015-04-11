import pygame
import random
import Handler

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    main_handler = Handler.Handler((640, 480))

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

                if event.key == pygame.K_F2:
                    pygame.image.save(screen, "screenshot.png")
        
        screen.fill((180, 120, 80))
        main_handler.render(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()
