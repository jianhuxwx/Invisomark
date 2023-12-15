import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def extract_edges(image_path):
    # 读取图片并转换为灰度图
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)  # 确保图像始终为彩色图像
    if image is None:
        raise ValueError("无法加载图像，请检查路径和文件格式。")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用Canny算法提取边缘
    edges = cv2.Canny(gray, 100, 200)

    return edges

def approximate_text_size(text, font_size):
    return (font_size // 2 * len(text), font_size)

def write_text_along_path(image_path, text, output_path, font_size=10, font_color=(255, 0, 0, 255)):  # 默认颜色现在包含透明度
    edges = extract_edges(image_path)
    image = Image.open(image_path).convert("RGBA")  # 转换为带透明度的模式
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))  # 创建透明覆盖层
    draw = ImageDraw.Draw(overlay)

    font = ImageFont.truetype("arial.ttf", font_size)

    occupied = np.zeros(edges.shape, dtype=bool)

    def can_place_text(x, y, text):
        size = approximate_text_size(text, font_size)
        if x + size[0] >= edges.shape[1] or y + size[1] >= edges.shape[0]:
            return False
        for i in range(size[1]):
            for j in range(size[0]):
                if occupied[y + i, x + j]:
                    return False
        return True

    def place_text(x, y, text):
        draw.text((x, y), text, font=font, fill=font_color)
        size = approximate_text_size(text, font_size)
        for i in range(size[1]):
            for j in range(size[0]):
                occupied[y + i, x + j] = True

    for y in range(edges.shape[0]):
        for x in range(edges.shape[1]):
            if edges[y, x] != 0 and can_place_text(x, y, text):
                place_text(x, y, text)

    combined = Image.alpha_composite(image, overlay)
    combined.save(output_path)

#write_text_along_path('/Users/david/Desktop/Code/ATP/11.jpeg', 'Keyfox', '/Users/david/Desktop/Code/ATP/111.png', font_size=8, font_color=(0, 128, 255, 50))  # 使用半透明的蓝色
