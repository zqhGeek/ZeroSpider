import PIL
from PIL import ImageTk
from PIL.Image import Image

from src import img_tool
from src.img_tool import resize
from src.key_work_spider import KeyWorkSpider
import tkinter as tk

is_spider = False
spider = None


def do_spider(timer):
    global is_spider
    if is_spider:
        global spider
        is_spider = False
        if isinstance(spider, KeyWorkSpider):
            spider.stop_work()
    else:
        is_spider = True
        spider = KeyWorkSpider('口罩', 30)
        spider.start_work(timer)


if __name__ == '__main__':
    # spider = KeyWorkSpider('口罩',30)
    # spider.start_work()
    window = tk.Tk()
    window.title('什么值得买--关键词监控')
    window.geometry('800x600')
    text = tk.Text(window, width=40, height=2)
    text.insert('end', '测试')
    text.place(x=160, y=40, anchor='nw')
    note = tk.Label(window, text='倒计时:', font=('Arial', 12), width=6, height=2)
    note.place(x=540, y=40, anchor='nw')
    number = tk.Label(window, text='60', font=('Arial', 20), width=4, height=2)
    number.place(x=600, y=20, anchor='nw')
    btn = tk.Button(window, text='监控', font=('Arial', 12), width=10, height=2, command=(lambda: do_spider(number)))
    btn.place(x=30, y=30, anchor='nw')
    list = tk.Listbox(window, width=80, height=24)
    list.insert(1, '1')
    list.insert(2, '2')
    list.insert(3, '3')
    list.place(x=30, y=90, anchor='nw')
    canvas = tk.Canvas(window, height=100, width=200)
    pil_image = PIL.Image.open(r'loading.png')
    pil_image_resized = resize(200, 130, pil_image)
    image_file = ImageTk.PhotoImage(pil_image_resized)
    # label = tk.Label(window, image=image_file, width=60, height=60)
    # label.pack(padx=5, pady=5)
    image = canvas.create_image(100, 0, anchor='n', image=image_file)
    canvas.place(x=800, y=120, anchor='ne')
    window.mainloop()
