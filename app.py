import pywebio

from pywebio.pin import put_radio, pin_wait_change, pin
from pywebio.input import file_upload
from pywebio.output import put_text, put_code, put_table, put_image, put_markdown, put_row, put_scope, use_scope

from ocr import detect, recognize
from utils import bytes_to_numpy, numpy_to_bytes


def main():
    put_markdown('# PaddleOCR PyWebIO Demo')
    uploaded_file = file_upload('请选择一张图片', accept='image/*', multiple=False, required=True)
    # 转换格式
    img = bytes_to_numpy(uploaded_file['content'])
    put_row(
        [
            put_scope('sidebar'),
            put_scope('body')
        ],
        size=r'30% 70%'
    )

    with use_scope('sidebar'):
        put_radio('task', options=[('查看原图', 'img'), ('文本检测', 'det'), ('文本识别', 'rec')], label='请选择要执行的任务')

    while True:
        pin_wait_change('task')
        with use_scope('body', clear=True):
            if pin.task == 'img':
                put_image(numpy_to_bytes(img))
            elif pin.task == 'det':
                im_show = detect(img)
                im_show = numpy_to_bytes(im_show)
                put_image(im_show)
            elif pin.task == 'rec':
                im_show, tdata, results_str = recognize(img)
                im_show = numpy_to_bytes(im_show)
                put_image(im_show)
                put_text('')
                put_code(results_str, language='tex')
                put_table(tdata)


if __name__ == '__main__':
    pywebio.start_server(main, port=8888, debug=True, reconnect_timeout=60)
