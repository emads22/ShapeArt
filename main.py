import time
from classes import Canvas, Square, Rectangle
from constants import *



def main():
    canvas = Canvas(height=20, width=30, color=(255, 255, 255))

    a_rectangle = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
    a_rectangle.draw(canvas)

    a_square = Square(x=1, y=3, side=3, color=(0, 100, 222))
    a_square.draw(canvas)

    img_path = IMAGES / f'canvas_{int(time.time())}.png'
    canvas.make(img_path)


    # canvas = Canvas(width=200, height=100, color=(255, 255, 255))
    # rect = Rectangle(x=10, y=20, width=30, height=40, color=(255, 0, 0))
    # rect.draw(canvas)
    # square = Square(x=50, y=50, side=20, color=(0, 255, 0))
    # square.draw(canvas)
    # canvas.make(image_path=Path('shapes.png'))


if __name__ == "__main__":
    try:
        main()
        print('\n\n--- Image with the drawn shapes created and saved successfully. ---\n\n')
    except Exception as e:
        print(f'\n\n--- An error occured: "{e}" ---\n\n')
