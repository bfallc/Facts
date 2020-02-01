from p5 import *

f = None

def setup():
        global f
        size(640, 360)

        # Create the font
        f = create_font("Arial.ttf", 30)
        text_font(f)
        text_align("CENTER")

def draw():
        background(102)
        text_align("RIGHT")
        drawType(width * 0.25)
        text_align("CENTER")
        drawType(width * 0.5)
        text_align("LEFT")
        drawType(width * 0.75)

def drawType(x):
        line((x, 0), (x, 65))
        line((x, 220), (x, height))
        fill(0)
        text("igggggghi", (x, 95))
        fill(51)
        text("ni", (x, 130))
        fill(204)
        text("san", (x, 165))
        fill(255)
        text("shi", (x, 210))

if __name__ == '__main__':
        run()