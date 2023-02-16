from PIL import Image

image = Image.open

print(f"Current size : {image.size}")

resized_image = image.resize((500, 500))

resized_image.save('')