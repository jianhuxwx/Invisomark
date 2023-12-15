from PIL import Image, ImageDraw, ImageFont

def estimate_text_size(text, font_size):
    """估算文本尺寸的简化方法。"""
    average_char_width = font_size * 0.6  # 假设每个字符的平均宽度
    text_width = int(average_char_width * len(text))
    text_height = font_size
    return text_width, text_height

def add_watermark(input_image_path, output_image_path, watermark_text, font_size=20):
    # 打开图片
    original_image = Image.open(input_image_path).convert('RGBA')
    width, height = original_image.size

    # 创建一个透明的水印层
    watermark = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    watermark_draw = ImageDraw.Draw(watermark)

    # 创建字体对象
    font = ImageFont.load_default()

    # 估算文本大小
    text_width, text_height = estimate_text_size(watermark_text, font_size)

    # 在整个图片上重复添加水印
    for x in range(0, width, text_width):
        for y in range(0, height, text_height):
            watermark_draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)

    # 将水印层合并到原始图片上
    watermarked_image = Image.alpha_composite(original_image, watermark)

    # 保存添加了水印的图片
    watermarked_image.save(output_image_path, 'PNG')

# 使用示例
#add_watermark('/Users/david/Desktop/Code/ATP/vulpinium_11.jpeg', '/Users/david/Desktop/Code/ATP/vulpinium_111.jpeg', 'Your Watermark Text')
