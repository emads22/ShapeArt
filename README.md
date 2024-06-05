# ShapeArt: Abstract Drawing Tool

## Overview
Drawing Shapes on Canvas is a Python CLI application designed to create and save images of shapes drawn on a canvas. The application, now known as **`ShapeArt`**, allows users to draw circles, rectangles, and squares of various dimensions and colors on a canvas and save the resulting image. It leverages Object-Oriented Programming (OOP) principles for modularity and code organization.

```sh

███████╗██╗  ██╗ █████╗ ██████╗ ███████╗     █████╗ ██████╗ ████████╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔══██╗╚══██╔══╝
███████╗███████║███████║██████╔╝█████╗█████╗███████║██████╔╝   ██║   
╚════██║██╔══██║██╔══██║██╔═══╝ ██╔══╝╚════╝██╔══██║██╔══██╗   ██║   
███████║██║  ██║██║  ██║██║     ███████╗    ██║  ██║██║  ██║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                     
```

## Features
- **Canvas Creation**: Create a canvas of specified width, height, and color.
- **Draw Shapes**: Draw circles, rectangles, and squares of user-defined dimensions and colors on the canvas.
- **Save Image**: Save the canvas with drawn shapes as an image file.
- **User Input Validation**: Validate user inputs to ensure they are correctly formatted and within acceptable ranges.

## Setup
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/emads22/ShapeArt-Drawer.git
    ```
2. **Navigate to the Project Folder**:
    ```sh
    cd ShapeArt-Drawer
    ```
3. **Ensure Python 3.x is Installed**: Check your Python version using:
    ```sh
    python --version
    ```
4. **Install Required Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Script**:
    ```sh
    python main.py
    ```
2. **Enter Canvas Information**:
    - Follow the prompts to enter the canvas width, height, and color.
3. **Draw Shapes**:
    - Choose whether to draw a circle, rectangle or square.
    - Enter the position, size, and color of the shape.
4. **Save Image**:
    - Once finished drawing, the canvas with shapes will be saved as an image file.

**Note**: If you're using Python version less than 3.10, replace the `match` statement in `main.py` with equivalent `if...elif...else` statements for handling different shape types.

## Example
Here’s an example of how to use the Drawing Shapes on Canvas application:

1. **Run the script**:
    ```sh
    python main.py
    ```
2. **Input the following when prompted**:
    - **Canvas Width**: `600`
    - **Canvas Height**: `400`
    - **Canvas Color**: `blue`
    - **Shape to Draw**: `rectangle`
    - **Position (x, y)**: `100, 100`
    - **Width**: `200`
    - **Height**: `150`
    - **Color**: `green`
3. **The script will output**:
    ```sh
    --- Image with the drawn shapes created and saved successfully.
    You can find it here "path/to/image.png" ---
    ```

## Files Description
- **main.py**: The main script that runs the application and handles user input.
- **constants.py**: Defines constants used throughout the project, such as file paths.
- **app_utils.py**: Contains utility functions for validating user input (integer, color).
- **classes.py**: Defines the core classes for the application: `Canvas`, `Circle`, `Square`, and `Rectangle`.

## Dependencies
- **Pillow**: A Python Imaging Library that adds image processing capabilities to your Python interpreter.
- **webcolors**: A library to work with color names defined by the HTML and CSS specifications.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.