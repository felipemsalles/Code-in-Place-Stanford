"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames():
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage('images/greenland-fire.png')
    #Code to find flames
    original_fire = SimpleImage('images/greenland-fire.png')
    highlighted_fire = SimpleImage('images/greenland-fire.png')
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is "sufficiently" red
        if pixel.red >= average:
        # If so, set value to 255 and its green and blue values to 0
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        elif pixel.red < average:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return image


def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage('images/greenland-fire.png')

    # Show the original fire
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames()
    highlighted_fire.show()

    
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
