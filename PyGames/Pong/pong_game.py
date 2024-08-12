# Import needed modules
# Game Settings and Variables
# Create Game Functions (No classes needed)
#        draw_paddle(position) - Draws two paddles on the screen
#        draw_ball(position) - Draws a white ball on the screen
#        update_ball() - Keeps the ball moving and allows the ball to bounce
#        reset_ball() - Resets the ball to starting position
# Main Game Loop
# Events & Conditions

from pygame import *

FPS = 30
WIDTH = 800
HEIGHT = 500
speed = 10
# left_paddle = (50, HEIGHT // 2 - 25, 10, 80)
# right_paddle = (WIDTH - 60, HEIGHT // 2 - 25, 10, 80)

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("PONG")
clock = time.Clock()
background = screen.fill((0,0,0))

# draw.rect(surface, color, Rect) Rect=(left, top, width, height)
def draw_paddle():
    #left paddle
    draw.rect(screen, "white",(50, HEIGHT // 2 - 25, 10, 80))
    #right paddle
    draw.rect(screen, "white",(WIDTH - 60, HEIGHT // 2 - 25, 10, 80))


def draw_ball():
    draw.circle(screen, "white",(WIDTH // 2, HEIGHT // 2), 8 )


run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            quit()

    screen.fill((0, 0, 0))
    draw_paddle()
    draw_ball()

    keys = key.get_pressed()


    display.update()
    clock.tick(FPS)
