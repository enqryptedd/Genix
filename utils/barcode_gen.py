import barcode
from barcode.writer import ImageWriter
import random

def generate_barcode(id_number):
    code128 = barcode.get_barcode_class("code128")
    barcode_instance = code128(id_number, writer=ImageWriter())
    temp_path = f"temp_barcode_{random.randint(1000, 9999)}"
    barcode_instance.save(temp_path, options={"write_text": False})
    return f"{temp_path}.png"