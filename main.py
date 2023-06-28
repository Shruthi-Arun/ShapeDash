import pygame
import random

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shape Dash')

player = pygame.Rect((300, 250, 50, 50))

# Border limits
border_left = 0
border_right = SCREEN_WIDTH
border_top = 0
border_bottom = SCREEN_HEIGHT

# Collectible object
collectible_radius = 15
collectible_position = pygame.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
collectible_color = (255, 255, 0)

# Game states
is_playing = False
score = 0

# Star background
stars = []
for _ in range(100):
    star_x = random.randint(0, SCREEN_WIDTH)
    star_y = random.randint(0, SCREEN_HEIGHT)
    stars.append((star_x, star_y))

# Start screen
def show_start_screen():
    screen.fill((0, 0, 0))
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), star, 1)
    font = pygame.font.Font(None, 48)
    title_text = font.render("SHAPE DASH", True, (255, 255, 255))
    instruction_text = font.render("Press SPACE to start", True, (255, 255, 255))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.update()

# Game over screen
def show_game_over_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 48)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.update()

# Finish button
def show_finish_button():
    finish_font = pygame.font.Font(None, 24)
    finish_text = finish_font.render("Finish", True, (255, 255, 255))
    finish_button = pygame.Rect(10, 10, 80, 30)
    pygame.draw.rect(screen, (0, 0, 255), finish_button)
    screen.blit(finish_text, (finish_button.x + finish_button.width // 2 - finish_text.get_width() // 2,
                              finish_button.y + finish_button.height // 2 - finish_text.get_height() // 2))
    pygame.display.update()



# Game loop
run = True
show_start_screen()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_playing:
                    is_playing = True
                    score = 0

    if is_playing:
        screen.fill((255, 102, 102))

        pygame.draw.rect(screen, (105, 190, 40), player)
        pygame.draw.circle(screen, collectible_color, (int(collectible_position.x), int(collectible_position.y)), collectible_radius)

        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.left > border_left:
            player.move_ip(-1, 0)  # moves left by 1 px

        elif key[pygame.K_d] and player.right < border_right:
            player.move_ip(1, 0)  # moves right by 1 px

        elif key[pygame.K_w] and player.top > border_top:
            player.move_ip(0, -1)  # moves up by 1 px

        elif key[pygame.K_s] and player.bottom < border_bottom:
            player.move_ip(0, 1)  # moves down by 1 px

        # Check collision with collectible object
        if player.colliderect(
                pygame.Rect(collectible_position.x - collectible_radius, collectible_position.y - collectible_radius,
                            collectible_radius * 2, collectible_radius * 2)):
            score += 1
            collectible_position = pygame.Vector2(random.randint(0, SCREEN_WIDTH),
                                                  random.randint(0, SCREEN_HEIGHT))

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    else:
        show_start_screen()

    pygame.display.update()

pygame.quit()
