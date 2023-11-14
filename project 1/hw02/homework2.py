from byuimage import Image


def flipped(filename):
    original = Image(filename)
    flipped_result = Image.blank(original.width, original.height)

    for y in range(original.height):
        for x in range(original.width):
            original_pixel = original.get_pixel(x, y)
            flipped_pixel = flipped_result.get_pixel(x, original.height - y - 1)

            flipped_pixel.blue = original_pixel.blue
            flipped_pixel.green = original_pixel.green
            flipped_pixel.red = original_pixel.red

    return flipped_result


def make_borders(filename, thickness, red, green, blue):
    # read in image, make copy with new height and width
    original = Image(filename)
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

    return border_result


if __name__ == "__main__":
    flipped("test_files/landscape.png").show()
    make_borders("test_files/landscape.png", 25, 100, 0, 100).show()

    # 1.1 - setup - create file, main code block, and import statements
    # 1.2 - create flipped(filename)

    # 2.1 - create make_borders() and read the image
    # example declaration: def make_borders(filename, thickness, red, green, blue):
    # 2.2 -make new image and fill in border color
    # 2.3 - copy the original image
