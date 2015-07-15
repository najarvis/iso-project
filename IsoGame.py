import pygame
import random
import Handler

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    main_handler = Handler.Handler((640, 480))

    clock = pygame.time.Clock()

    done = False
    while not done:
        time_passed_seconds = clock.tick() / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

                if event.key == pygame.K_F2:
                    pygame.image.save(screen, "screenshot.png")

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            main_handler.camera.offset.y += 100 * time_passed_seconds
        if pressed_keys[pygame.K_s]:
            main_handler.camera.offset.y -= 100 * time_passed_seconds

        if pressed_keys[pygame.K_d]:
            main_handler.camera.offset.x -= 100 * time_passed_seconds
        if pressed_keys[pygame.K_a]:
            main_handler.camera.offset.x += 100 * time_passed_seconds

        screen.fill((180, 120, 80))
        main_handler.render(screen)

        pygame.display.update()

pygame.quit()

if __name__ == "__main__":
    main()
