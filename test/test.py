import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# Load image
image = cv2.imread('0.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

# Convert to PIL image and draw text
pil_image = Image.fromarray(image)
font = ImageFont.truetype('pricedown.ttf', 32)
draw = ImageDraw.Draw(pil_image)
draw.text((0, 0), 'GĄSKĄ IDĘ', font=font, fill=(255, 255, 255, 0))

# Convert to cv2 image
image_np = np.array(pil_image)
image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2BGR)

# Save image as output.jpg
cv2.imwrite('output.jpg', image_np)
