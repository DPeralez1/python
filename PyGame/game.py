from pygame import *

FPS = 30
WIDTH = 700
HEIGHT = 500
plane_x = 100
plane_y = 300
speed = 10

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Fly Me")
clock = time.Clock()
