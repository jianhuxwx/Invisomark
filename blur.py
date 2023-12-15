from PIL import Image, ImageFilter

def blur_image(input_image_path, output_image_path, blur_amount):
    # 打开图片
    image = Image.open(input_image_path)

    # 应用模糊效果
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_amount))

    # 保存模糊后的图片
    blurred_image.save(output_image_path)

# 使用示例
#blur_image('/Users/david/Desktop/Code/ATP/11_watermarked.png', '/Users/david/Desktop/Code/ATP/11_watermarked.png', 10000000)
