import tkinter as tk  # graphics lib (pip3 install tkinter)
from tkinter import *
from tkinter import filedialog
from client import *  # app client
from PIL import Image, ImageTk  # graphics lib (-//- PIL)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1010x430")
        self.configure(bg='grey')
        self.panel = Label()
        self.resizable(width=False, height=False)
        self.title("Graphics Watermarking")
        self.btn1 = Button(text="Select image", background="black", foreground="red",
                           padx="115", pady="5", font="20", command=self.open_img)
        self.btn1.place(x=5, y=10)
        self.btn2 = Button(text="Make a watermark", background="black", foreground="red",
                           padx="96", pady="5", font="20", command=self.send_image)
        self.btn2.place(x=5, y=65)
        self.box = Listbox(width=55, height=17, bg='red')
        self.box.place(x=5, y=140)
        self.send_path = ''

    def open_img(self):
        try:
            if self.send_path != '':
                self.clear_label_image()
            self.box.delete(0, END)
            path = filedialog.askopenfilename(title='Open *.jpg', type=".jpg")
            print(path)
            if path:
                self.send_path = path
                img = ImageTk.PhotoImage(Image.open(path).resize((650, 400)))
                self.panel = Label(image=img)
                self.panel.image = img
                self.panel.place(x=350, y=10)
            else:
                self.send_path = ''
                self.box.insert(END, 'ERROR:    Image don\'t selected')
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))

    def clear_label_image(self):
        self.panel.destroy()

    def display(self, image):
        try:
            self.clear_label_image()
            self.panel = Label(image=image)
            self.panel.image = image
            self.panel.place(x=350, y=10)
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))

    def send_image(self):
        try:
            if self.send_path != '':
                im = get_watermark_image(self.send_path)
                # a function from the client that receives an image with a watermark
                save_image(im)
                # a function from the client that save image with a watermark
                self.box.config(fg='green')
                self.box.insert(END, '[Success] Image saved')
                self.box.config(fg='black')
                self.display(ImageTk.PhotoImage(Image.open('Processed image.png').resize((650, 400))))
            else:
                self.box.insert(END, 'ERROR:   Image don\'t select')
        except Exception as ex:
            self.box.insert(END, 'ERROR:    ' + str(ex))


app = Window()
app.mainloop()
