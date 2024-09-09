# Jucimar Jr
# Arthur Marshall 2415310048
# 2024

import pygame
import random


# Player one up keymove function
def player_upmove(move_up, position):
    # player 1 up movement
    if move_up is True:
        position -= 5
        return position
    else:
        position += 0
        return position


# Player one down keymove function
def player_downmove(move_down, position):
    # player 1 down movement
    if move_down is True:
        position += 5
        return position
    else:
        position += 0
        return position


# Score check function
def score_check():
    global ball_x, ball_y, ball_dx, ball_dy, score_1, score_2
    if ball_x < -50:
        score_2 += 1
        ball_x, ball_y = 640, 360
        ball_dx, ball_dy = random.choice([5, -5]), random.choice([5, -5])
        sad_crowd.play()
        scoring_sound_effect.play()
    elif ball_x > 1320:
        score_1 += 1
        ball_x, ball_y = 640, 360
        ball_dx, ball_dy = random.choice([5, -5]), random.choice([5, -5])
        happy_crowd.play()
        scoring_sound_effect.play()


# Player 1 collision dynamic
def collision_check(player_y, player, ai_check):
    global ball_y, ball_dy, ball_dx, ran
    if player_y < ball_y + 25 and player_y + 150 > ball_y:
        impact_position = (ball_y + ball.get_height() / 2 - player_y) / player.get_height()
        angle = (impact_position - 0.5) * 2
        ball_dx = -ball_dx
        ball_dy += angle * 3
        ball_dy = min(max(ball_dy, -10), 10)
        tense_crowd.play()
        bounce_sound_effect.play()
        if ai_check is False:
            if score_2 > score_1:
                ran = random.choice(hard_ran_ai)
            else:
                ran = random.choice(ran_ai)
        else:
            return True
    return False


pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 3

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2024-09-02")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')
tense_crowd = pygame.mixer.Sound('assets/pong_expectation.mpeg')
sad_crowd = pygame.mixer.Sound('assets/sad_crowd.mpeg')
happy_crowd = pygame.mixer.Sound('assets/happy_crowd.mpeg')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 100
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
player_2_y = 100

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5

# crowd png
crowd = pygame.image.load("assets/crowd.png")
new_width = 400
new_height = 200
resized_crowd = pygame.transform.scale(crowd, (new_width, new_height))

# score
score_1 = 0
score_2 = 0

# A.I random moveset
ran = 0

# A.I Error list

ran_ai = [0, 20, 50, 0, 100, 150, 0, 35, 0]
hard_ran_ai = [0, 0, 0, 0, 0, 50, 50, 100, 60]

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # Crowd on game
        screen.blit(resized_crowd, (450, 550))

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if ball_x < 100 and collision_check(player_1_y, player_1, False):
            ball_x = 100

        # ball collision with the player 2 's paddle
        if ball_x > 1160:
            collision_check(player_2_y, player_2, True)

        # scoring points
        score_check()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player movements
        player_1_y = player_upmove(player_1_move_up, player_1_y)
        player_1_y = player_downmove(player_1_move_down, player_1_y)

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 "Artificial Intelligence"
        player_2_y = ball_y + ran
        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
