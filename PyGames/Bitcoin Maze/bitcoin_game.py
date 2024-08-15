from pygame import *
from classes import *
from random import *

WALL_COLOR = (52,82,63)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 15, 15)
GREEN = (15, 255, 15)
coin_counter = 0

font.init()
font = font.Font(None, 45)
win = font.render("You win!", True, GREEN)
lose = font.render("You lose!", True, RED)
coin_text = font.render("Coins: ", True, WHITE)
coin_counter_text = font.render(str(coin_counter), True, WHITE)

mixer.init()
mixer.music.load("./PyGames/Bitcoin Maze/cave.mp3")
mixer.music.play()

coin_sound = mixer.Sound("./PyGames/Bitcoin Maze/coin_drop.mp3")
win_sound = mixer.Sound("./PyGames/Bitcoin Maze/win.wav")
lose_sound = mixer.Sound("./PyGames/Bitcoin Maze/lose.wav")

WIDTH = 700
HEIGHT = 500
FPS = 30

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Bitcoin Maze")
clock = time.Clock()
bg = transform.scale(image.load("./PyGames/Bitcoin Maze/background.jpg"), (WIDTH, HEIGHT))

player = Player("./PyGames/Bitcoin Maze/miner.png", 35, 50, 8)
ghost = Ghost("./PyGames/Bitcoin Maze/ghost.png", 600, 200, 5)
btc_wallet = Player("./PyGames/Bitcoin Maze/bitcoin.png", 625, 425, 0)

# wall = Border(color, x, y, width, height)
w1 = Border(WALL_COLOR, 100, 0, WIDTH, 10)
w2 = Border(WALL_COLOR, 100, HEIGHT-10, 450, 10)
w3 = Border(WALL_COLOR, 100, 0, 10, 400)
w4 = Border(WALL_COLOR, 175, 80, 10, 410)
w5 = Border(WALL_COLOR, 250, 300, 10, 190)
w6 = Border(WALL_COLOR, 325, 250, 200, 10)
w7 = Border(WALL_COLOR, 250, 10, 10, 195)
w8 = Border(WALL_COLOR, 550, 315, 10, 185)
w9 = Border(WALL_COLOR, 400, 10, 10, 150)
w10 = Border(WALL_COLOR, 500, 100, 10, 90)
walls = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]


coin1 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))
coin2 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))
coin3 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))
coin4 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))
coin5 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))
coin6 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))
coin7 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))
coin8 = Coin(randint(50, WIDTH-20), randint(50, HEIGHT-20))

coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8]



run = True
end = False
while run:
    for e in event.get():
        if e.type == QUIT:
            quit()
            run = False

    if end != True:
        screen.blit(bg, (0, 0))
        screen.blit(coin_text, (WIDTH-150, 35))
        screen.blit(coin_counter_text, (WIDTH-50, 35))
        player.controls()
        ghost.update()

        for w in walls:
            w.build_wall()

        for c in coins:
            c.draw_coin()
            if c.rect.colliderect(player.rect):
                coins.remove(c)
                coin_sound.play()
                c.kill()
                coin_counter += 1
                coin_counter_text = font.render(str(coin_counter), True, WHITE)

        if sprite.collide_rect(player, btc_wallet) and coin_counter == 8:
            win_sound.play()
            end = True
            screen.blit(win, (300,325))


        if sprite.collide_rect(player, ghost) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) \
            or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10):
            lose_sound.play()
            end = True
            screen.blit(lose, (300,325))
            lose_sound.play()


        player.game_end()
        ghost.game_end()
        btc_wallet.game_end()

    else:
        end = False
        coin_counter = 0
        for c in coins:
            c.kill()
        player = Player("./PyGames/Bitcoin Maze/miner.png", 35, 50, 8)
        coin_counter_text = font.render(str(coin_counter), True, WHITE)
        time.delay(3000)

    display.update()
    clock.tick(FPS)
