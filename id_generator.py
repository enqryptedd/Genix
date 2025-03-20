from utils.barcode_gen import generate_barcode
from utils.name_gen import generate_random_name
from utils.image_utils import overlay_text, overlay_image, load_template
import os
from datetime import datetime, timedelta
import random

class FakeIDGenerator:
    def __init__(self):
        self.template_path = "templates/id_template.png"
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)

    def create_fake_id(self):
        full_name = generate_random_name()
        dob = self._random_dob()
        id_number = f"{random.randint(100000, 999999)}-{random.randint(100, 999)}"
        issue_date = datetime.now().strftime("%m/%d/%Y")
        expiry_date = (datetime.now() + timedelta(days=365 * 5)).strftime("%m/%d/%Y")

        id_image = load_template(self.template_path)

        id_image = overlay_text(id_image, full_name, (50, 50), font_size=30)
        id_image = overlay_text(id_image, f"DOB: {dob}", (50, 100), font_size=20)
        id_image = overlay_text(id_image, f"ID#: {id_number}", (50, 140), font_size=20)
        id_image = overlay_text(id_image, f"Issued: {issue_date}", (50, 180), font_size=20)
        id_image = overlay_text(id_image, f"Expires: {expiry_date}", (50, 220), font_size=20)

        barcode_path = generate_barcode(id_number)
        id_image = overlay_image(id_image, barcode_path, (300, 50))

        output_path = os.path.join(self.output_dir, f"fake_id_{id_number}.png")
        id_image.save(output_path)
        os.remove(barcode_path)

    def _random_dob(self):
        today = datetime.now()
        start_date = today - timedelta(days=365 * 30)
        random_days = random.randint(0, 365 * 10)
        dob = start_date + timedelta(days=random_days)
        return dob.strftime("%m/%d/%Y")