import os
from PIL import Image

# replace these lines.
input_path = "from/your/folder/path"
output_path = "to/your/folder/path"


os.makedirs(output_path, exist_ok=True)

for filename in os.listdir(input_path):

    if filename.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")):
        img_path = os.path.join(input_path, filename)
        img = Image.open(img_path)
        flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)

        flipped_image.save(os.path.join(output_path, filename))
        print(f"Flipped: {filename}")

print("All files have been flipped and saved!")
