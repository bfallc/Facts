from p5 import *

f = None

def setup():
        global f
        size(640, 480)
        # Create the font
        f = create_font("Arial.ttf", 20)
        text_font(f)
        
def draw():
        background(250)
        text_align("LEFT")
        fill(0)
        text('jello wyrld.', (10, 10), 30)

if __name__ == '__main__':
        run()