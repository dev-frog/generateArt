#!/usr/bin/python
import random
import uuid
from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f"Process run_id: {run_id}")

image = Image.new('RGB',(2000,2000))
width,height = image.size

reactangle_width = 80
reactangle_hight = 80

number_of_squares = random.randint(10, 600)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    reactangle_x = random.randint(0, width)
    reactangle_y = random.randint(0, height)

    reactangle_shape = [
        (reactangle_x, reactangle_y),
        (reactangle_x + reactangle_width, reactangle_y + reactangle_hight)]
    draw_image.rectangle(
        reactangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 100),
            random.randint(0, 255),
        )
    )

image.save(f'./output/{run_id}.png')