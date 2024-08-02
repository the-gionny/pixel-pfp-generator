from PIL import Image, ImageDraw, ImageFont
import random
import string


def generatepfp(pfplevel,imgSize):
    image = Image.new('RGB', (imgSize, imgSize), 'white')
    x = 0
    y = 0
    color1=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    new_colors = []
    if pfplevel==0:
        new_colors = [color1]
    elif pfplevel==1:
        color2 = tuple(max(0, min(255, c + random.randint(-100, 100))) for c in color1)
        color3 = tuple(max(0, min(255, c + random.randint(-100, 100))) for c in color2)
        new_colors = [color1,color2,color3]
    else: return
    for _ in range(int(imgSize*3.75)):
        x=random.randint(0, int((imgSize/2)-1))
        y=random.randint(0, imgSize-1)
        new_color=random.choice(new_colors)
        image.putpixel((x, y), new_color)
        image.putpixel(((imgSize-1)-x, y), new_color)
    chars_numbers = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(chars_numbers) for _ in range(9))

    resized_image = image.resize((800, 800), Image.NEAREST)
    resized_image.save(f'{random_string}{pfplevel}.png')
    image.close()
    resized_image.close()

generatepfp(1,16)