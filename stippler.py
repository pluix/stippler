from time import time
from math import floor, ceil
from PIL import Image, ImageDraw

### Custom Values ###
image_fp = "img.png"
cell_size = 31 # Needs to be odd
blend_edges = False # Makes the maximum circle size larger so that two adjacent circles will touch
black_out = True # Doesn't render a circle if the pixel is dark enough
bg_color = "#000000"
circle_color = "#ffffff"
colorize = False # Will colorize the image instead of using the above values
pixelate = False # Pixelates the image instead of rendering circles (requires colorize = True)
min_dimension = 5000 # Used to scale input image. Set to 0 for no scaling

# For colored terminal output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

start_time = time()
print(bcolors.HEADER + "\nProgram start...\n" + bcolors.ENDC)

img_color = Image.open(image_fp)
img_grey = img_color.convert("L")

if blend_edges:
    max_circ_size = ceil(cell_size / 2)
else:
    max_circ_size = floor(cell_size / 2)

width,height = img_grey.size
shortest_side = min(width,height)

# Resize the images to min_dimension if less than min_dimension
if width < min_dimension or height < min_dimension:
    scalor = round(min_dimension / shortest_side, 2)

    width = int(width*scalor)
    height = int(height*scalor)

    img_grey = img_grey.resize((width,height))

    if colorize:
        img_color = img_color.resize((width,height))

    print(bcolors.OKCYAN + f"Image scale: {scalor}x" + bcolors.ENDC)

print(bcolors.OKCYAN + f"Image dimensions: {width:,}p x {height:,}p" + bcolors.ENDC)

# Initialize a blank image
new_image = Image.new("RGB", img_grey.size, bg_color)

# Initialize a drawer
draw = ImageDraw.Draw(new_image)

dot_num = 0

# Iterates through input image and draws the new one
for x in range(0, width, cell_size):
    for y in range(0, height, cell_size):
        pixel_value = img_grey.getpixel((x-ceil(cell_size/2),y-ceil(cell_size/2)))

        brightness = pixel_value / 255

        if black_out and pixel_value < (255 / max_circ_size) / 2:
            pass
        else:
            if colorize:
                circle_color = img_color.getpixel((x,y))

            circ_size = int(brightness*max_circ_size) - 1
            if circ_size < 0:
                circ_size = 0

            if x and y != 0:
                middle = [(x-ceil(cell_size/2),y-ceil(cell_size/2)), (x-floor(cell_size/2),y-floor(cell_size/2))]
                left_top = (middle[0][0]-circ_size, middle[0][1]-circ_size)
                right_bottom = (middle[1][0]+circ_size, middle[1][1]+circ_size)

                if pixelate:
                    draw.rectangle(xy=[(x-cell_size,y-cell_size), (x,y)], fill=circle_color, width=0)
                else:
                    draw.ellipse(xy=[left_top, right_bottom], fill=circle_color, width=0)
                dot_num += 1

print(bcolors.OKCYAN + f"Dots generated: {dot_num:,}" + bcolors.ENDC)

new_image.show()

print(bcolors.WARNING + f"\nFinished in {round(time()-start_time, 3)}s\n" + bcolors.ENDC)

save = input(bcolors.HEADER + "Save? (Y/N) " + bcolors.ENDC).lower().strip()

if save == "y":
    filename = input("Enter a filename: ")+".png"

    new_image.save(filename)
    print(bcolors.OKGREEN + f"Saved {filename}\n" + bcolors.ENDC)
else:
    print(bcolors.OKGREEN + "Closed without saving\n" + bcolors.ENDC)
