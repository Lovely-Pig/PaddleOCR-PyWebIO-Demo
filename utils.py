import cv2
import numpy as np


def bytes_to_numpy(image_bytes, channels='RGB'):
    """
    图片格式转换 bytes -> numpy
    args:
        image_bytes(str): 图片的字节流
        channels(str): 图片的格式 ['BGR'|'RGB']
    return(array):
        转换后的图片
    """
    _image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image_np = cv2.imdecode(_image_np, cv2.IMREAD_COLOR)
    if channels == 'BGR':
        return image_np
    elif channels == 'RGB':
        image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
        return image_np


def numpy_to_bytes(image_np, channels='RGB'):
    """
    图片格式转换 numpy -> bytes
    args:
        image_np(array): numpy格式的图片数据
        channels(str): 图片的格式 ['BGR'|'RGB']
    return(str):
        图片的字节流
    """
    if channels == 'RGB':
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    image_bytes = np.array(cv2.imencode('.jpg', image_np)[1]).tobytes()

    return image_bytes


def numpy_to_pic(image_path, image_np, channels='BGR'):
    """
    保存图片
    args:
        image_path(str): 图片路径
        image_np(array): numpy格式的图片数据
        channels(str): 图片的格式 ['BGR'|'RGB']
    """
    if channels == 'BGR':
        cv2.imwrite(image_path, image_np)
    elif channels == 'RGB':
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        cv2.imwrite(image_path, image_np)
