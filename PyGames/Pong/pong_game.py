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
speed = 15

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("PONG")
clock = time.Clock()
jet = (49, 47, 47)
sienna = (224, 122, 95)


paddle_width = 10
paddle_height = 100
paddle_speed = 7
left_paddle = [50, (HEIGHT - paddle_height)/2]
right_paddle = [WIDTH - 60 - paddle_width, (HEIGHT-paddle_height)/2]
ball_pos = [(WIDTH / 2), (HEIGHT / 2)]
# ball speed [x,y]
ball_speed = [7,7]

font.init()
score_font = font.Font(None,45)


# draw.rect(surface, color, Rect) Rect=(left, top, width, height)
def draw_paddle(pos):
    draw.rect(screen, sienna,(pos[0], pos[1],paddle_width, paddle_height))


def draw_ball(pos):
    draw.circle(screen, sienna,pos, 15)

def update_ball():
    global ball_pos, ball_speed, left_score, right_score
    # list variables is where 0,1 are coming coming from. equal to each others list.
    # which then matches      x,y
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check collision with top or bottom of the screen. The Y position.
    if ball_pos[1] <= 10 or ball_pos[1] >= HEIGHT-10:
        ball_speed[1] = -ball_speed[1] #allows it to bounce


    # Check collision with top or bottom of the screen
    if (ball_pos[0] <= left_paddle[0] + paddle_width and left_paddle[1] <= ball_pos[1] <= left_paddle[1] + paddle_height) or \
       (ball_pos[0] >= right_paddle[0] and right_paddle[1] <= ball_pos[1] <= right_paddle[1] + paddle_height):
       ball_speed[0] = -ball_speed[0]

    # Check if the ball has passed the left or right edge
    if ball_pos[0] <= 0:
        right_score += 1
        reset_ball()

    elif ball_pos[0] >= WIDTH:
        left_score += 1
        reset_ball()

def reset_ball():
    global ball_pos, ball_speed
    ball_pos = [(WIDTH / 2), (HEIGHT / 2)]
    ball_speed = [7,7]



left_score = 0
right_score = 0

run = True
while run:
    screen.fill(jet)
    for e in event.get():
        if e.type == QUIT:
            run = False
            quit()

    keys = key.get_pressed()
    if keys[K_w] and left_paddle[1] > 0:
        left_paddle = (left_paddle[0], left_paddle[1] - paddle_speed)
    elif keys[K_s] and left_paddle[1] < HEIGHT -paddle_height:
        left_paddle = (left_paddle[0], left_paddle[1] + paddle_speed)

    if keys[K_UP] and right_paddle[1] > 0:
        right_paddle = (right_paddle[0], right_paddle[1] - paddle_speed)
    elif keys[K_DOWN] and right_paddle[1] < HEIGHT - paddle_height:
        right_paddle = (right_paddle[0], right_paddle[1] + paddle_speed)

    update_ball()
    screen.fill(jet)

    draw_paddle(left_paddle)
    draw_paddle(right_paddle)
    draw_ball(ball_pos)

    left_text = score_font.render(str(left_score), True, sienna)
    right_text = score_font.render(str(right_score), True, sienna)
    screen.blit(left_text,(WIDTH/4, 20))
    screen.blit(right_text,(WIDTH*3/4, 20))

    if left_score >= 5 or right_score >= 5:
        run = False


    display.update()
    clock.tick(FPS)
