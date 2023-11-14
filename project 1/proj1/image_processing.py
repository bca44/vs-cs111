import sys
from byuimage import Image


def validate_commands(argv_list):
    valid_commands = {"-d": 3, "-k": 5, "-s": 4, "-g": 4, "-b": 8, "-f": 4, "-m": 4, "-c": 8}
    command = argv_list[1]
    return len(argv_list) == valid_commands.get(command, 0)


def display(argv_list):
    # displays image file
    image_file = argv_list[0]
    Image(image_file).show()


def darken(argv_list):
    filename, save_name, percent = argv_list
    percent = float(percent)
    dark_factor = 1 - percent
    darken_solution = Image(filename)

    for y in range(darken_solution.height):
        for x in range(darken_solution.width):
            pixel = darken_solution.get_pixel(x, y)
            pixel.red = pixel.red * dark_factor
            pixel.green = pixel.green * dark_factor
            pixel.blue = pixel.blue * dark_factor

    darken_solution.save(save_name)


def sepia(argv_list):
    filename, save_name = argv_list
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
    sepia_solution.save(save_name)


def grayscale(argv_list):
    filename, save_name = argv_list
    grayscale_solution = Image(filename)

    for y in range(grayscale_solution.height):
        for x in range(grayscale_solution.width):
            pixel = grayscale_solution.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    grayscale_solution.save(save_name)


def borders(argv_list):
    input_name, save_name, thickness, red, green, blue = argv_list
    thickness, red, green, blue = [int(val) for val in [thickness, red, green, blue]]

    # read in image, make copy with new height and width
    original = Image(input_name)
    new_height, new_width = original.height + 2 * thickness, original.width + 2 * thickness
    border_result = Image.blank(new_width, new_height)

    def fill_border(y_range_start, y_range_stop, x_range_start, x_range_stop):
        for y in range(y_range_start, y_range_stop):
            for x in range(x_range_start, x_range_stop):
                border_pixel = border_result.get_pixel(x, y)
                border_pixel.red = red
                border_pixel.green = green
                border_pixel.blue = blue

    # left border
    fill_border(0, new_height, 0, thickness)

    # right border
    fill_border(0, new_height, new_width - thickness, new_width)

    # bottom border
    fill_border(new_height - thickness, new_height, 0, new_width)

    # top border
    fill_border(0, thickness, 0, new_width)

    # copy original image inside border
    for y in range(original.height):
        for x in range(original.width):
            original_pixel = original.get_pixel(x, y)
            new_pixel = border_result.get_pixel(x + thickness, y + thickness)

            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue

    border_result.save(save_name)


def flip(argv_list):
    input_name, save_name = argv_list
    original = Image(input_name)
    flipped_result = Image.blank(original.width, original.height)

    for y in range(original.height):
        for x in range(original.width):
            original_pixel = original.get_pixel(x, y)
            flipped_pixel = flipped_result.get_pixel(x, original.height - y - 1)

            flipped_pixel.blue = original_pixel.blue
            flipped_pixel.green = original_pixel.green
            flipped_pixel.red = original_pixel.red

    flipped_result.save(save_name)


def mirror(argv_list):
    input_name, output_name = argv_list
    original = Image(input_name)
    mirrored_result = Image.blank(original.width, original.height)

    for y in range(original.height):
        for x in range(original.width):
            original_pixel = original.get_pixel(x, y)
            mirrored_pixel = mirrored_result.get_pixel(original.width - x - 1, y)

            mirrored_pixel.blue = original_pixel.blue
            mirrored_pixel.green = original_pixel.green
            mirrored_pixel.red = original_pixel.red

    mirrored_result.save(output_name)


def collage(argv_list):
    input_one, input_two, input_three, input_four, save_name, thickness = argv_list
    image_one, image_two, image_three, image_four = \
        [Image(val) for val in [input_one, input_two, input_three, input_four]]
    thickness = int(thickness)

    # blank canvas
    collage_result = Image.blank((image_one.width * 2) + (thickness * 3), (image_one.height * 2) + (thickness * 3))
    collage_result.save(save_name)

    # outer borders
    borders([save_name, save_name, thickness, 0, 0, 0])
    collage_result = Image(save_name)

    # inner borders
    for y in range(thickness + image_one.height, thickness * 2 + image_one.height):
        for x in range(thickness, collage_result.width - thickness):
            pixel = collage_result.get_pixel(x, y)
            pixel.red, pixel.blue, pixel.green = 0, 0, 0
    for y in range(thickness, collage_result.height - thickness):
        for x in range(thickness + image_one.width, thickness * 2 + image_one.width):
            pixel = collage_result.get_pixel(x, y)
            pixel.red, pixel.blue, pixel.green = 0, 0, 0
    collage_result.save(save_name)

    # copy images

    # image1 - xrange(thickness, thickness + image1.width), yrange(2thickness + image1.height)
    def copy_image(original, x_increase, y_increase):
        for y in range(original.height):
            for x in range(original.width):
                original_pixel = original.get_pixel(x, y)
                new_pixel = collage_result.get_pixel(x + x_increase, y + y_increase)

                new_pixel.red = original_pixel.red
                new_pixel.green = original_pixel.green
                new_pixel.blue = original_pixel.blue

    copy_image(image_one, thickness, image_one.height + (2 * thickness))
    copy_image(image_two, image_two.width + (2 * thickness), image_two.height + (2 * thickness))
    copy_image(image_three, thickness, thickness)
    copy_image(image_four, image_four.width + (2 * thickness), thickness)
    # save image as save_name
    collage_result.save(save_name)

def main(command, argv_list):
    # 1.3 - display
    if command == "-d":
        display(argv_list)
    # part 2 - image filters
    # 2.1 - darken filter
    elif command == "-k":
        darken(argv_list)
    # 2.2 - sepia filter
    elif command == "-s":
        sepia(argv_list)
    # 2.3 - grayscale filter
    elif command == "-g":
        grayscale(argv_list)
    # 2.4 - refactor - "thinking about your design"
    # TODO can I create a make_filter() HOF to condense this?
    # part 3 - image manipulations
    # 3.1 - borders
    elif command == "-b":
        borders(argv_list)
    # 3.2 - flip
    elif command == "-f":
        flip(argv_list)
    # 3.3 - mirror
    elif command == "-m":
        mirror(argv_list)
    # 3.4 - refactor - "do you have duplication anywhere"
    # part 4 - compositing
    # 4.1 - collage
    elif command == "-c":
        collage(argv_list)


if __name__ == "__main__":
    # part 1 - receiving and validating commands
    # 1.1 - setup python file, main block, etc.
    # 1.2 - read in command line arguments and make sure they are valid, using validate_commands()
    # if valid, passes sys.argv list to main()
    if validate_commands(sys.argv):
        main(sys.argv[1], sys.argv[2:])
    else:
        print("Invalid command. Please try again.")
