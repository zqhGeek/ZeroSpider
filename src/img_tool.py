from PIL import Image, ImageTk


def resize(w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
    w, h = pil_image.size  # 获取图像的原始大小
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


# def resize(w, h, w_box, h_box, pil_image):
#     '''
#     resize a pil_image object so it will fit into
#     a box of size w_box times h_box, but retain aspect ratio
#     对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
#     '''
#     f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
#     f2 = 1.0 * h_box / h
#     factor = min([f1, f2])
#     # print(f1, f2, factor) # test
#     # use best down-sizing filter
#     width = int(w * factor)
#     height = int(h * factor)
#     return pil_image.resize((width, height), Image.ANTIALIAS)
