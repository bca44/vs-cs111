class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

    def __str__(self):
        return f"Key: '{self.key}', Pos: {self.pos}"

    def __repr__(self):
        return f"Button({self.pos}, '{self.key}')"


class Keyboard:
    def __init__(self, *args):
        self.buttons = {}  # Initialize an empty dictionary to store buttons
        for button in args:  # Iterate through the Button objects passed as arguments
            self.buttons[button.pos] = button  # Use the button's position as the dictionary key

    def __str__(self):
        buttons_str = " | ".join([str(button) for button in self.buttons.values()])
        return f"{buttons_str}"

    def __repr__(self):
        buttons_repr = ", ".join([repr(button) for button in self.buttons.values()])
        return f"Keyboard({buttons_repr})"

    def press(self, info):
        if info in self.buttons:  # Check if the position exists in the buttons dictionary
            button = self.buttons[info]  # Get the button object
            button.times_pressed += 1  # Increment the times_pressed attribute
            return button.key  # Return the key of the pressed button
        else:
            return ''  # No button at this position

    def typing(self, typing_input):
        output = ''  # Initialize an empty string to store the total output
        for pos in typing_input:  # Iterate through the list of positions
            if pos in self.buttons:  # Check if the position exists in the buttons dictionary
                button = self.buttons[pos]  # Get the button object
                button.times_pressed += 1  # Increment the times_pressed attribute
                output += button.key  # Add the key of the pressed button to the output
        return output  # Return the total output

    def add_button(self, button):
        if button.pos not in self.buttons:
            self.buttons[button.pos] = button
