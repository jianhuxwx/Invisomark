from PIL import Image
from PIL.ExifTags import TAGS

def get_reversed_tags():
    return {value: key for key, value in TAGS.items()}

def add_metadata(image_path, metadata):
    image = Image.open(image_path)
    exif_data = image.getexif()
    reversed_tags = get_reversed_tags()

    for tag, value in metadata.items():
        if tag in reversed_tags:
            exif_data[reversed_tags[tag]] = value

    image.save(image_path, exif=exif_data)

def read_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image.getexif()

    readable_exif = {TAGS[key]: value for key, value in exif_data.items() if key in TAGS}
    return readable_exif

# 使用示例
#metadata = read_metadata('/Users/david/Desktop/Code/ATP/logo 2_watermarked.png')
#print(metadata)


# 使用示例
#add_metadata('/Users/david/Desktop/Code/ATP/vulpinium_1.jpeg', {'Artist': 'Your Name', 'Software': 'Your Software'})
