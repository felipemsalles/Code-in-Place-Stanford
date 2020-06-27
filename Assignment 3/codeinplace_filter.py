"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage('images/quad.jpg')

    # Show the image before the transform
    image.show()

    # Code in Place Filter
    image = code_in_place_filter()

    # Show the image after the transform
    image.show()


def code_in_place_filter():
    image = SimpleImage('images/quad.jpg')
    for pixel in image:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0.7
        pixel.blue = pixel.blue * 1.5
    return image


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()