from PIL import Image

def compress_image(input_path, output_path, quality):    
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=quality)

input_image_path = "foto_01.jpg"
output_image_path = "compressed_image.jpg"
compression_quality = 65

compress_image(input_image_path, output_image_path, compression_quality)
