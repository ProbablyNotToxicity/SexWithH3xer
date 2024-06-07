import pygame
pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Clicker Game")
score = 0
clicks = 0
button_image = pygame.image.load("h3xer-hand.png")
background_image = pygame.image.load("h3xer.png")
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle button click
            if button_rect.collidepoint(event.pos):
                score += 1
                clicks += 1
    # Update game state
    button_rect = button_image.get_rect()
    button_rect.center = (window_width // 2, window_height // 2)
    # Draw game
    window.blit(background_image, (0, 0))
    window.blit(button_image, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(text, (10, 10))
    pygame.display.update()