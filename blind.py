from blind_watermark import WaterMark

def embed_watermark(original_image_path, watermark_content, output_image_path):
    bwm = WaterMark(password_img=1, password_wm=1)
    bwm.read_img(original_image_path)
    bwm.read_wm(watermark_content, mode='str')
    bwm.embed(output_image_path)
    len_wm = len(bwm.wm_bit)
    print('Put down the length of wm_bit: {}'.format(len_wm))
    return len_wm

def extract_watermark(embedded_image_path, wm_length):
    bwm = WaterMark(password_img=1, password_wm=1)
    wm_extract = bwm.extract(embedded_image_path, wm_shape=wm_length, mode='str')
    print(wm_extract)
    return wm_extract

# 使用示例
# 嵌入水印
#wm_length = embed_watermark('/Users/david/Desktop/Code/ATP/11.jpg', 'Keyfox', '/Users/david/Desktop/Code/ATP/11.jpg')

# 提取水印
#extracted_wm = extract_watermark('/Users/david/Desktop/Code/ATP/vulpinium_1_watermarked.png', 87)
#print(extracted_wm)
