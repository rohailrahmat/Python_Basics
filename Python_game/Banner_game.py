import pygame 
# ------------------- BannerText Class -------------------
class BannerText:
    def __init__(self, text, font, color, speed, x, y):
        self.text = text
        self.font = font
        self.color = color
        self.speed = speed
        self.x = x
        self.y = y
        self.surface = font.render(text, True, color)

    def update(self):
        self.x -= self.speed
        if self.x + self.surface.get_width() < 0:
            self.x = 800  # reset to right side

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))


# ------------------- Button Class -------------------
class Button:
    def __init__(self, x, y, width, height, color, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font
        self.text_surface = font.render(text, True, (255, 255, 222))  # white text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# ------------------- Main App Class -------------------
class BannerApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 200))
        pygame.display.set_caption("Moving Banner Text")
        self.clock = pygame.time.Clock()

        font = pygame.font.SysFont("San Sarif", 40)

        self.banner = BannerText("Welcome to the Python Banner App!", font, (0, 0, 255), 2, 800, 80)

        self.button_start = Button(150, 140, 100, 40, (0, 200, 0), "Start", font)
        self.button_stop = Button(550, 140, 100, 40, (200, 0, 0), "Stop", font)

        self.running = True
        self.moving = False  # starts in stopped state

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_start.is_clicked(mouse_pos):
                        self.moving = True
                    elif self.button_stop.is_clicked(mouse_pos):
                        self.moving = False

            self.screen.fill((255, 255, 255))  # White background

            # Draw UI elements
            self.button_start.draw(self.screen)
            self.button_stop.draw(self.screen)

            if self.moving:
                self.banner.update()

            self.banner.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        print("App closed successfully.")


# ------------------- Start the App -------------------
if __name__ == "__main__":
    app = BannerApp()
    app.run()
