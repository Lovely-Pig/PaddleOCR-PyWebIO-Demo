from paddleocr import PaddleOCR
from ocr_utils import draw_ocr, draw_ocr_box_txt, get_tdata, get_results_str

ocr = PaddleOCR(lang='ch')


def detect(image):
    """
    文本检测
    args:
        image(array): numpy格式的图片 'RGB'
    return(array):
        检测后的图片 numpy格式 'RGB'
    """
    result = ocr.ocr(image, rec=False)
    im_show = draw_ocr(image, result)

    return im_show


def recognize(image, output_mode=0):
    """
    文本识别
    args:
        image(array): numpy格式的图片 'RGB'
        output_mode(int): 图片输出模式 [0|1]
    return(array):
        识别后的图片 numpy格式 'RGB'
    """
    result = ocr.ocr(image)
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    # print('txts:', txts)
    # print('scores:', scores)
    if output_mode == 0:
        im_show = draw_ocr_box_txt(image, boxes, txts, scores)
    elif output_mode == 1:
        im_show = draw_ocr(image, boxes, txts, scores)

    tdata = get_tdata(txts, scores)
    results_str = get_results_str(txts, scores)

    return im_show, tdata, results_str
