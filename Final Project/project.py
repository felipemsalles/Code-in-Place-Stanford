# Geometric GIF
from PIL import Image, ImageDraw


def create_image_function(width, height, coord_x, coord_y, coord_size):
    img = Image.new('RGB', (width, height), (400, 400, 400))
    draw = ImageDraw.Draw(img)
    draw.ellipse((coord_x - 400, coord_y - 400, coord_x + coord_size, coord_y + coord_size), fill='blue')  # blue circle
    draw.rectangle((coord_x + 90, coord_y + 90, coord_x + coord_size, coord_y + coord_size), fill='green')    # green
    draw.rectangle((coord_x - 300, coord_y - 300, coord_x + coord_size, coord_y + coord_size), fill='yellow')  # yellow
    draw.rectangle((300, 200, 100, 100), fill='black')  # black square
    draw.text((145, 145), "Code in Place - 2020", fill='white')  # code in place text
    draw.text((180, 180), "Stanford", fill='red')  # stanford text
    return img


frames = []
x, y = 0, 0

for i in range(10):
    new_frame = create_image_function(400, 400, x, y, 50)
    frames.append(new_frame)
    x += 50
    y += 50

frames[0].save('geometric-gif.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100,  loop=0)
