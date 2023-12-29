from turtle import *
import colorsys


speed(0.3)
pensize(1)
bgcolor('black')
hue = 0


for i in range(500):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.005
    circle(5-i,100)
    lt(80)
    circle(5-i, 80)
    rt(100)

    done
