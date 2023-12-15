from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    # 打开图片
    image = Image.open(input_image_path)
    width, height = image.size

    # 创建一个可以在图片上绘图的对象
    draw = ImageDraw.Draw(image)

    # 设置较大的字体
    font = ImageFont.truetype("arial.ttf", 36)  # 使用Arial字体，字号为36

    # 确定文本位置（左下角）
    x = 10
    y = height - 50  # 距离底部50像素

    # 获取图片底部边缘的平均颜色
    bottom_edge = image.crop((0, height - 50, width, height))
    pixels = list(bottom_edge.getdata())
    average_color = sum(sum(pixel) / 3 for pixel in pixels) / len(pixels)

    # 根据平均颜色选择文本颜色
    text_color = (0, 0, 0) if average_color > 128 else (255, 255, 255)

    # 在图片上添加文本
    draw.text((x, y), watermark_text, font=font, fill=text_color)

    # 保存图片
    image.save(output_image_path)

# 使用示例
#add_watermark('/Users/david/Desktop/Code/ATP/vulpinium_1.jpeg', '/Users/david/Desktop/Code/ATP/vulpinium_1_new.jpeg', '© 2023 Your Name')
