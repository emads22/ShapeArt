import time
from classes import Canvas, Circle, Square, Rectangle
from app_utils import validate_int, validate_color, validate_shape_type
from constants import *


def main():
    # Display logo
    print("\n\n\n\n", ASCII_ART)

    # Prompt user for canvas information
    canvas_width = validate_int("\n\n>> Enter the canvas width: ")
    canvas_height = validate_int("   Enter the canvas height: ")
    canvas_color = validate_color(
        "   Enter the canvas color name (e.g., 'red'): ")

    # Create the canvas
    canvas = Canvas(width=canvas_width,
                    height=canvas_height, color=canvas_color)

    while True:
        # Prompt user for shape type
        shape_type = validate_shape_type(
            "\n\n>> Enter the shape to draw ('circle', 'rectangle', 'square', or 'q' for exit): ")

        # Draw the specified shape on the canvas
        match shape_type:

            case 'circle':
                x = validate_int(
                    "\n\n>> Enter the x-coordinate of the center of the circle: ")
                y = validate_int(
                    "   Enter the y-coordinate of the center of the circle: ")
                radius = validate_int("   Enter the radius of the circle: ")
                color = validate_color(
                    "   Enter the color name of the circle (e.g., 'red'): ")
                circle = Circle(x=x, y=y, radius=radius, color=color)
                circle.draw(canvas)

            case 'rectangle':
                x = validate_int(
                    "\n\n>> Enter the x-coordinate of the top-left corner of the rectangle: ")
                y = validate_int(
                    "   Enter the y-coordinate of the top-left corner of the rectangle: ")
                width = validate_int("   Enter the width of the rectangle: ")
                height = validate_int("   Enter the height of the rectangle: ")
                color = validate_color(
                    "   Enter the color name of the rectangle (e.g., 'red'): ")
                rectangle = Rectangle(x=x, y=y, width=width,
                                      height=height, color=color)
                rectangle.draw(canvas)

            case 'square':
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

            case _:  # 'q'
                # Exit loop when user enters 'q'
                break

    # Save the canvas as an image
    image_path = IMAGES / f'canvas_{int(time.time())}.png'
    canvas.make(image_path)

    # Return the image path
    return image_path


if __name__ == "__main__":
    try:
        img_path = main()
        print(f'\n\n--- Image with the drawn shapes created and saved successfully.\n\n    You can find it here "{
              str(img_path)}" ---\n\n')
    except Exception as e:
        print(f'\n\n--- An error occured: "{e}" ---\n\n')
