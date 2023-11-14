from byuimage import Image


def iron_puzzle(filename):
    iron_solution = Image(filename)
    for y in range(iron_solution.height):
        for x in range(iron_solution.width):
            pixel = iron_solution.get_pixel(x, y)
            pixel.blue *= 10
            pixel.green = 0
            pixel.red = 0

    return iron_solution


def west_puzzle(filename):
    west_solution = Image(filename)
    for y in range(west_solution.height):
        for x in range(west_solution.width):
            pixel = west_solution.get_pixel(x, y)
            if pixel.blue < 16:
                pixel.blue *= 16
            elif pixel.blue >= 16:
                pixel.blue = 0
            pixel.green = 0
            pixel.red = 0

    return west_solution


def darken(filename, percent):
    dark_factor = 1 - percent
    darken_solution = Image(filename)
    for y in range(darken_solution.height):
        for x in range(darken_solution.width):
            pixel = darken_solution.get_pixel(x, y)
            pixel.red = pixel.red * dark_factor
            pixel.green = pixel.green * dark_factor
            pixel.blue = pixel.blue * dark_factor
    return darken_solution


def grayscale(filename):
    grayscale_solution = Image(filename)
    for y in range(grayscale_solution.height):
        for x in range(grayscale_solution.width):
            pixel = grayscale_solution.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return grayscale_solution


def sepia(filename):
    sepia_solution = Image(filename)
    for y in range(sepia_solution.height):
        for x in range(sepia_solution.width):
            pixel = sepia_solution.get_pixel(x, y)
            true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
            true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
            true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue
            if pixel.red > 255:
                pixel.red = 255
            else:
                pixel.red = true_red
            if pixel.green > 255:
                pixel.green = 255
            else:
                pixel.green = true_green
            if pixel.blue > 255:
                    pixel.blue = 255
            else:
                pixel.blue = true_blue
    return sepia_solution


def create_left_border(filename, weight):
    # read in Image, grab height and width
    original_image = Image(filename)
    height = original_image.height
    width = original_image.width
    new_width = width + weight

    # make new image with new width, add blue border
    border_solution = Image.blank(new_width, height)
    for y in range(border_solution.height):
        for x in range(weight):
            pixel = border_solution.get_pixel(x, y)
            pixel.blue = 255
            pixel.green = 0
            pixel.red = 0

    # copy image to appropriate space right of blue border
    for y in range(border_solution.height):
        for x in range(weight, new_width):
            new_pixel = border_solution.get_pixel(x, y)
            original_pixel = original_image.get_pixel(x - weight, y)
            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue

    return border_solution


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.


def create_stripes(filename):
    "*** YOUR CODE HERE ***"


def copper_puzzle(filename):
    "*** YOUR CODE HERE ***"


def main():
    iron_puzzle("test_files/iron.png").show()
    west_puzzle("test_files/west.png").show()
    darken("test_files/cougar.png", 0.8).show()
    grayscale("test_files/cougar.png").show()
    create_left_border("test_files/cougar.png", 25).show()


if __name__ == "__main__":
    main()
