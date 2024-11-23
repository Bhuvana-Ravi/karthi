from tkinter import *
from tkinter.filedialog import *
from PIL import Image

# Ask the user to select a file
file_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

# Open the selected image
img = Image.open(file_path)

# Get the size of the image
original_width, original_height = img.size

# Compress the image by reducing the size (e.g., by 50%)
new_width = int(original_width * 0.5)
new_height = int(original_height * 0.5)

# Resize the image
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Ask the user where to save the compressed image
save_path = asksaveasfilename(title="Save Compressed Image", defaultextension=".jpg", filetypes=[("JPEG Files", "*.jpg;*.jpeg"), ("PNG Files", "*.png")])

# Save the compressed image
if save_path:
    img.save(save_path)


