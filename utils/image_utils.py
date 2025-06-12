# utils/image_utils.py

import random
import io
import urllib.request
from PIL import Image, ImageTk

male_photos = [
    "https://randomuser.me/api/portraits/men/32.jpg",
    "https://randomuser.me/api/portraits/men/44.jpg",
]

female_photos = [
    "https://randomuser.me/api/portraits/women/15.jpg",
    "https://randomuser.me/api/portraits/women/27.jpg",
]

def get_random_photo(gender):
    if gender == "Male":
        return random.choice(male_photos)
    elif gender == "Female":
        return random.choice(female_photos)
    return None

def update_photo(gender, photo_label):
    url = get_random_photo(gender)
    if url:
        try:
            with urllib.request.urlopen(url) as u:
                raw_data = u.read()
            im = Image.open(io.BytesIO(raw_data)).resize((150, 150))
            photo_img = ImageTk.PhotoImage(im)
            photo_label.config(image=photo_img)
            photo_label.image = photo_img
        except:
            photo_label.config(text="Image load failed", image='')
            photo_label.image = None
    else:
        photo_label.config(image='', text="No Photo")
        photo_label.image = None
