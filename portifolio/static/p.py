# from PIL import Image

# def resize_image(input_path, output_path, size=(500, 500)):
#     with Image.open(input_path) as img:
#         # Resize the image with the LANCZOS filter
#         resized_img = img.resize(size, Image.LANCZOS)
#         # Save the resized image
#         resized_img.save(output_path)
#         print(f"Image saved to {output_path}")

# # Usage example:
# resize_image("troy.png", "resized_image.png")

from PIL import Image

def crop_image(input_path, output_path, size=(500, 500)):
    with Image.open(input_path) as img:
        # Calculate center crop box
        width, height = img.size
        left = (width - size[0]) / 2
        top = (height - size[1]) / 2
        right = (width + size[0]) / 2
        bottom = (height + size[1]) / 2
        
        # Crop and save the image
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
        print(f"Image saved to {output_path}")

# Usage example:
crop_image("troy.png", "cropped_image.png")
