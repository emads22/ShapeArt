import time
from classes import Canvas, Square, Rectangle
from app_utils import validate_int, validate_color, validate_shape_type
from constants import *


def main():

    # Prompt user for canvas information
    canvas_width = validate_int("\n\n>> Enter the canvas width: ")
    canvas_height = validate_int("   Enter the canvas height: ")
    canvas_color = validate_color(
        "   Enter the canvas color name (e.g., 'red'): ")

    # Create the canvas
    canvas = Canvas(width=canvas_width,
                    height=canvas_height, color=canvas_color)

    # Prompt user for shape type
    shape_type = validate_shape_type(
        "\n\n>> Enter the shape to draw (rectangle or square): ")

    # Draw the specified shape on the canvas
    if shape_type == "rectangle":
        x = validate_int(
            "\n\n>> Enter the x-coordinate of the top-left corner of the rectangle: ")
        y = validate_int(
            "   Enter the y-coordinate of the top-left corner of the rectangle: ")
        width = validate_int("   Enter the width of the rectangle: ")
        height = validate_int("   Enter the height of the rectangle: ")
        color = validate_color(
            "   Enter the color name of the rectangle (e.g., 'red'): ")
        rect = Rectangle(x=x, y=y, width=width, height=height, color=color)
        rect.draw(canvas)

    elif shape_type == "square":
        x = validate_int(
            "\n\n>> Enter the x-coordinate of the top-left corner of the square: ")
        y = validate_int(
            "   Enter the y-coordinate of the top-left corner of the square: ")
        side = validate_int(
            "   Enter the length of each side of the square: ")
        color = validate_color(
            "   Enter the color name of the square (e.g., 'red'): ")
        square = Square(x=x, y=y, side=side, color=color)
        square.draw(canvas)

    # Save the canvas as an image
    image_path = IMAGES / f'canvas_{int(time.time())}.png'
    canvas.make(image_path)

    # Return the image path
    return image_path


if __name__ == "__main__":
    try:
        main()
        print('\n\n--- Image with the drawn shapes created and saved successfully. ---\n\n')
    except Exception as e:
        print(f'\n\n--- An error occured: "{e}" ---\n\n')
