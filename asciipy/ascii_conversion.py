import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageChops


def image_to_ascii(image_path, max_width, max_height, charset=None):
    if charset is None:
        charset = [" ", ".", "-", ":", "*", "<", "+", "S", "#", "%", "@"]

    img = Image.open(image_path).convert("L")

    enhancer = ImageEnhance.Contrast(img)  # Apply contrast enhancement for better tonal range
    img = enhancer.enhance(2.0)

    img = img.resize((max_width, max_height), Image.NEAREST)

    edges = img.filter(ImageFilter.FIND_EDGES)  # Apply a slight edge enhancement to give some definition
    img = ImageChops.add(img, edges, scale=1.1, offset=-10)  # Combine the edges back into the image to retain detail

    gray_array = np.array(img)
    normalized_array = (gray_array / 255 * (len(charset) - 1)).astype(np.uint8)

    ascii_art = "\n".join(''.join(charset[pixel] for pixel in row) for row in normalized_array)

    return ascii_art
