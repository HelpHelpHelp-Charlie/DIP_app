#Notch-Filter-for-Image-Processing from github
import pathlib
from tkinter import *
from tkinter import filedialog, messagebox
from ctypes import *
from PIL import Image, ImageTk, ImageOps
import matplotlib.pyplot as plt
import numpy as np


class MainApp:
    def __init__(self):
        self.root=Tk();
        self.root.title("main");
        self.root.geometry("820x420");

        icon=PhotoImage(file='logo.png');
        self.root.iconphoto(True,icon);
        self.root.config(background="#2f444f")
        self.left_frame = LabelFrame(text = "Original Image")
        self.left_frame.columnconfigure(0)
        self.left_frame.columnconfigure(1)
        self.left_frame.rowconfigure(0)
        self.left_frame.rowconfigure(1)
        self.left_frame.rowconfigure(2)
        self.left_frame.rowconfigure(3)
        self.left_frame.rowconfigure(4)
        self.left_frame.rowconfigure(5)
        
        self.original_img = Label(self.left_frame, image = "", text = "Load an image \n to preview it here!", padx = 150, pady = 150)
        
        
        self.btn_browse_img = Button(self.left_frame, text = "Browse Image", bg = "lightblue", command = self.browse_img)
        self.btn_apply_filter = Button(self.left_frame, text = "Apply Filter", bg = "lightblue", command = self.apply_filter)
        self.select_filter_var = StringVar(self.root)
        self.select_filter_var.set('Ideal')
        self.select_filter = OptionMenu(self.left_frame, self.select_filter_var, *{'Ideal', 'Butterworth', 'Gaussian'})
        self.number_of_points = Entry(self.left_frame)
        self.frequency = Entry(self.left_frame)
        self.butterworth_order = Entry(self.left_frame)
        self.original_img.grid(row = 0, column = 0, columnspan = 2)
        self.btn_browse_img.grid(row = 1, column = 0, sticky='nsew')
        self.btn_apply_filter.grid(row = 1, column = 1, sticky='nsew')
        Label(self.left_frame, text = "Select type of Notch Filter: ").grid(row = 2, column = 0, sticky = "nsew")
        self.select_filter.grid(row = 2, column = 1, sticky = 'nsew')
        Label(self.left_frame, text = "Number of Points: ").grid(row = 3, column = 0, sticky = 'nsew')
        self.number_of_points.grid(row = 3, column = 1, sticky = 'nsew')
        self.number_of_points.insert(END, '6')
        Label(self.left_frame, text = "Band Radius: ").grid(row = 4, column = 0, sticky = 'nsew')
        self.frequency.grid(row = 4, column = 1, sticky = 'nsew')
        self.frequency.insert(END, '121.0')
        Label(self.left_frame, text = "Order of \n Butterworth Filter").grid(row = 5, column = 0, sticky = 'nsew')
        self.butterworth_order.grid(row = 5, column = 1, sticky = 'nsew')
        self.butterworth_order.insert(END, 1)
        self.left_frame.pack(side = "left", fill = Y)
        #setting up Right side of GUI
        
        
        
        self.right_frame = LabelFrame(text = "Filtered Image")
        self.filter_img = Label(self.right_frame, image = "", text = "Apply filter to an image\nto view it here !", padx = 150, pady = 150)
        #self.btn_save_img = Button(self.right_frame, text = "Save this Image", bg = "lightblue", command = self.save_img)
        #self.btn_summary = Button(self.right_frame, text = "Show Summary",  bg = "lightblue", command = self.show_summary)
        self.info_lbl = Label(self.right_frame, text = "READY")
        self.filter_img.pack()
        #self.btn_save_img.pack(in_ = self.right_frame, fill = X)
        #self.btn_summary.pack(in_ = self.right_frame, fill = X)
        self.info_lbl.pack(in_ = self.right_frame, fill = BOTH, side = LEFT)
        self.right_frame.pack(side = "right", fill = Y) 
    def run(self):
        self.root.mainloop()
        
    def browse_img(self):
        try:
            file = filedialog.askopenfilename(title = "Load Image", filetypes=[('Images', ['*jpeg','*png','*jpg'])]) 
            file = ImageOps.grayscale((Image.open(file)))
            file.save(pathlib.Path("tmp/original_img.png"))
            file = ImageTk.PhotoImage(file)
            self.original_img.configure(text = "", image = file)
            self.original_img.text = ""
            self.original_img.image = file
        except Exception as e:
            messagebox.showerror("An error occured !", e)

    def apply_filter(self):
        try:
            self.info_lbl.configure(text = "BUSY")
            self.info_lbl.text = "BUSY"
            fshift, dft = self.get_fshift_and_save_dft()
            plt.clf()
            plt.imshow(Image.open(pathlib.Path("tmp/dft.png")), cmap = "gray")
            #set_plot_title("Click on image to choose points. (Press any key to Start)")
            plt.waitforbuttonpress()
            #set_plot_title(f'Select {self.number_of_points.get()} points with mouse click')
            points = np.asarray(plt.ginput(int(self.number_of_points.get()), timeout = -1))     
            plt.close()
            #Applying filter
            # if self.select_filter_var.get() == "Ideal":
            #     IdealNotchFilter().apply_filter(fshift, points, float(self.frequency.get()), pathlib.Path("tmp/filtered_img.png"))
            # elif self.select_filter_var.get() == "Butterworth":
            #     ButterworthNotchFilter().apply_filter(fshift, points, float(self.frequency.get()), pathlib.Path("tmp/filtered_img.png"), order = int(self.butterworth_order.get()))
            # elif self.select_filter_var.get() == "Gaussian":
            #     GaussianNotchFilter().apply_filter(fshift, points, float(self.frequency.get()), pathlib.Path("tmp/filtered_img.png"))
            self.info_lbl.configure(text = "READY")
            self.info_lbl.text = "READY"
            #Show filtered image
            filter_img = ImageTk.PhotoImage(ImageOps.grayscale((Image.open(pathlib.Path("tmp/filtered_img.png")))))
            self.filter_img.configure(image = filter_img)
            self.filter_img.image = filter_img
        except Exception as e:
            messagebox.showerror("An error occured!", e)
            
            
if __name__ == "__main__":
    MainApp().run()