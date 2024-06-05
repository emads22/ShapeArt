import numpy as np
from PIL import Image
from pathlib import Path


class Canvas:
    """
    A class representing a canvas for drawing shapes.

    Attributes:
        height (float): The height of the canvas.
        width (float): The width of the canvas.
        color (tuple): The RGB color of the canvas represented as a tuple (R, G, B).
        data (numpy.ndarray): A NumPy array representing the canvas data.

    Methods:
        make(image_path: Path) -> None:
            This method saves the canvas as an image file.
    """

    def __init__(self, height: float, width: float, color: tuple) -> None:
        """
        Initializes a Canvas instance with the specified height, width, and color.

        Parameters:
            height (float): The height of the canvas.
            width (float): The width of the canvas.
            color (tuple): The RGB color of the canvas represented as a tuple (R, G, B).
        """
        self.height = height
        self.width = width
        self.color = color

        

    def make(self, image_path: Path) -> None:
        """
        Saves the canvas as an image file.

        Parameters:
            image_path (Path): The path where the image file will be saved.
        """
        pass


class Square:
    """
    A class representing a square shape.

    Attributes:
        x (float): The x-coordinate of the square's top-left corner.
        y (float): The y-coordinate of the square's top-left corner.
        side (float): The length of each side of the square.
        color (tuple): The RGB color of the square represented as a tuple (R, G, B).

    Methods:
        draw(canvas: Canvas) -> None:
            This method draws the square on the specified canvas.
    """

    def __init__(self, x: float, y: float, side: float, color: tuple) -> None:
        """
        Initializes a Square instance with the specified position, side length, and color.

        Parameters:
            x (float): The x-coordinate of the square's top-left corner.
            y (float): The y-coordinate of the square's top-left corner.
            side (float): The length of each side of the square.
            color (tuple): The RGB color of the square represented as a tuple (R, G, B).
        """
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas: Canvas) -> None:
        """
        Draws the square on the specified canvas.

        Parameters:
            canvas (Canvas): The canvas on which the square will be drawn.
        """
        pass


class Rectangle:
    """
    A class representing a rectangle shape.

    Attributes:
        x (float): The x-coordinate of the rectangle's top-left corner.
        y (float): The y-coordinate of the rectangle's top-left corner.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        color (tuple): The RGB color of the rectangle represented as a tuple (R, G, B).

    Methods:
        draw(canvas: Canvas) -> None:
            This method draws the rectangle on the specified canvas.
    """

    def __init__(self, x: float, y: float, width: float, height: float, color: tuple) -> None:
        """
        Initializes a Rectangle instance with the specified position, width, height, and color.

        Parameters:
            x (float): The x-coordinate of the rectangle's top-left corner.
            y (float): The y-coordinate of the rectangle's top-left corner.
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
            color (tuple): The RGB color of the rectangle represented as a tuple (R, G, B).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas: Canvas) -> None:
        """
        Draws the rectangle on the specified canvas.

        Parameters:
            canvas (Canvas): The canvas on which the rectangle will be drawn.
        """
        pass
