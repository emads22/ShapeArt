from PIL import Image, ImageDraw
import numpy as np
from pathlib import Path


class Canvas:
    """
    A class representing a canvas for drawing shapes.

    Attributes:
        height (int): The height of the canvas.
        width (int): The width of the canvas.        
        color (tuple): The RGB color of the canvas represented as a tuple (R, G, B).
        data (numpy.ndarray): A NumPy array representing the canvas data.

    Methods:
        make(image_path: Path) -> None:
            This method saves the canvas as an image file.
    """

    def __init__(self, height: int, width: int, color: tuple) -> None:
        """
        Initializes a Canvas instance with the specified width, height, and color.

        Parameters:
            height (int): The height of the canvas.
            width (int): The width of the canvas.
            color (tuple): The RGB color of the canvas represented as a tuple (R, G, B).
        """
        self.height = height
        self.width = width
        self.color = color

        # Initialize canvas data as a NumPy array filled with the specified color
        self.data = np.zeros(
            shape=(int(self.height), int(self.width), 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path: Path) -> None:
        """
        Saves the canvas as an image file.

        Parameters:
            image_path (Path): The path where the image file will be saved.
        """
        # Create an image from the canvas data and save it to the specified path
        image = Image.fromarray(obj=self.data, mode='RGB')
        image.save(image_path)


class Circle:
    """
    A class representing a circle shape.

    Attributes:
        x (int): The x-coordinate of the circle's center.
        y (int): The y-coordinate of the circle's center.
        radius (int): The radius of the circle.
        color (tuple): The RGB color of the circle represented as a tuple (R, G, B).

    Methods:
        draw(canvas: Canvas) -> None:
            This method draws the circle on the specified canvas.
    """

    def __init__(self, x: int, y: int, radius: int, color: tuple) -> None:
        """
        Initializes a Circle instance with the specified position, radius, and color.

        Parameters:
            x (int): The x-coordinate of the circle's center.
            y (int): The y-coordinate of the circle's center.
            radius (int): The radius of the circle.
            color (tuple): The RGB color of the circle represented as a tuple (R, G, B).
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, canvas: Canvas) -> None:
        """
        Draws the circle on the specified canvas.

        Parameters:
            canvas (Canvas): The canvas on which the circle will be drawn.
        """
        # Assign y_center and x_center to represent the coordinates of the circle's center
        y_center, x_center = self.y, self.x
        # Pre-calculate radius squared for efficiency to avoid using `sqrt` or `**0.5` in distance formula
        radius_squared = self.radius ** 2

        # Loop over each pixel in the canvas
        for y in range(canvas.data.shape[0]):
            for x in range(canvas.data.shape[1]):
                # Calculate the squared distance from the current pixel to the circle's center
                distance_squared = (x - x_center) ** 2 + (y - y_center) ** 2

                # If the squared distance is less than or equal to the squared radius, color the pixel
                if distance_squared <= radius_squared:
                    canvas.data[y, x] = self.color


class Rectangle:
    """
    A class representing a rectangle shape.

    Attributes:
        x (int): The x-coordinate of the rectangle's top-left corner.
        y (int): The y-coordinate of the rectangle's top-left corner.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        color (tuple): The RGB color of the rectangle represented as a tuple (R, G, B).

    Methods:
        draw(canvas: Canvas) -> None:
            This method draws the rectangle on the specified canvas.
    """

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple) -> None:
        """
        Initializes a Rectangle instance with the specified position, width, height, and color.

        Parameters:
            x (int): The x-coordinate of the rectangle's top-left corner.
            y (int): The y-coordinate of the rectangle's top-left corner.
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
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
        # Calculate the coordinates of the bottom-right corner of the rectangle
        bottom_right_x = self.x + self.width
        bottom_right_y = self.y + self.height

        # Fill the specified rectangle area on the canvas with the rectangle's color
        # Note: The order in slicing is [y1:y2, x1:x2] because NumPy arrays are indexed as (row, column) which corresponds to (y, x)
        # In the context of the Canvas class and the NumPy array used to represent the canvas data,
        # x corresponds to the horizontal axis (width) => column index;
        # y corresponds to the vertical axis (height) => row index.
        canvas.data[self.y:bottom_right_y, self.x:bottom_right_x] = self.color


class Square:
    """
    A class representing a square shape.

    Attributes:
        x (int): The x-coordinate of the square's top-left corner.
        y (int): The y-coordinate of the square's top-left corner.
        side (int): The length of each side of the square.
        color (tuple): The RGB color of the square represented as a tuple (R, G, B).

    Methods:
        draw(canvas: Canvas) -> None:
            This method draws the square on the specified canvas.
    """

    def __init__(self, x: int, y: int, side: int, color: tuple) -> None:
        """
        Initializes a Square instance with the specified position, side length, and color.

        Parameters:
            x (int): The x-coordinate of the square's top-left corner.
            y (int): The y-coordinate of the square's top-left corner.
            side (int): The length of each side of the square.
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
        # Calculate the coordinates of the bottom-right corner of the square
        bottom_right_x = self.x + self.side
        bottom_right_y = self.y + self.side

        # Fill the specified rectangle area on the canvas with the rectangle's color
        # Note: The order in slicing is [y1:y2, x1:x2] because NumPy arrays are indexed as (row, column) which corresponds to (y, x)
        # In the context of the Canvas class and the NumPy array used to represent the canvas data,
        # x corresponds to the horizontal axis (width) => column index;
        # y corresponds to the vertical axis (height) => row index.
        canvas.data[self.y:bottom_right_y, self.x:bottom_right_x] = self.color
