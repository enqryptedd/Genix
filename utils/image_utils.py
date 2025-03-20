from PIL import Image, ImageDraw, ImageFont

def load_template(template_path):
    try:
        return Image.open(template_path).convert("RGBA")
    except FileNotFoundError:
        raise Exception("@enqryptedd | Put an id_template.png in the templates folder!")

def overlay_text(image, text, position, font_size=20):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw.text(position, text, font=font, fill=(0, 0, 0, 255))
    return image

def overlay_image(base_image, overlay_path, position):
    overlay = Image.open(overlay_path).convert("RGBA")
    base_image.paste(overlay, position, overlay)
    return base_image