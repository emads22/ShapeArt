import webcolors


def validate_int(prompt):
    """
    Prompts the user to enter a int value and validates it to ensure it is positive.

    Parameters:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The validated positive int value entered by the user.

    Raises:
        ValueError: If the entered value is not a valid positive int.
    """
    while True:
        try:
            # Prompt the user to enter a int value
            value = int(input(prompt))

            # Check if the entered value is positive
            if value <= 0:
                raise ValueError("Value must be greater than 0")

            # Return the validated positive int value
            return value
        except ValueError:
            # Handle the case when the entered value is not a valid positive int
            print("\n-- Invalid input. Please enter a valid positive number. --\n")


def validate_color(prompt):
    """
    Prompts the user to enter a color name and converts it to its RGB representation.

    Parameters:
        prompt (str): The prompt to display to the user.

    Returns:
        tuple: The RGB representation of the entered color name as a tuple (red, green, blue).

    Raises:
        ValueError: If the entered color name is not recognized.
    """
    while True:
        try:
            # Prompt the user to enter a color name
            color_input = input(prompt).lower()

            # Convert the color name to its RGB representation
            rgb_value = webcolors.name_to_rgb(color_input)

            # Return the RGB representation (e.g. Red: rgb_value = IntegerRGB(red=255, green=0, blue=0)) as a tuple of integers
            # Alternatively: return (rgb_value.red, rgb_value.green, rgb_value.blue)
            return rgb_value

        except ValueError as e:
            # Handle the case when the entered color name is not recognized
            print(f'\n-- {e} --\n')


def validate_shape_type(prompt):
    """
    Prompts the user to enter a shape type (rectangle or square) and validates it.

    Parameters:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The validated shape type (rectangle or square).

    Raises:
        ValueError: If the entered shape type is neither rectangle nor square.
    """
    while True:
        try:
            # Prompt the user to enter a shape type
            shape_type = input(prompt).lower()

            # Check if the entered shape type is either rectangle or square or q
            if shape_type not in ('rectangle', 'square', 'q'):
                raise ValueError(
                    "Invalid shape type. Please enter 'rectangle', 'square', or 'q' for exit.")

            # Return the validated shape type
            return shape_type
        except ValueError as e:
            # Handle the case when the entered shape type is not valid
            print(f'\n-- {e} --\n')
