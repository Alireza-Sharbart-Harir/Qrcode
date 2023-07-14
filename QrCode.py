import customtkinter as tk
from tkinter import *
import qrcode
class QrCode:
    def __init__(self):
        self.root = tk.CTk()

        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")

        self.root.title("QrCode Generator")
        self.root.iconbitmap("Icon.ico")
        self.root.configure(bg= "#FAEBD7")
        self.root.geometry("800x550")
        self.root.resizable(False, False)

        self.frame = tk.CTkFrame(master= self.root, border_width= 1, width= 700, height= 450, corner_radius= 20)
        self.frame.pack(padx= 50, pady= 50)

        self.label1 = tk.CTkLabel(master= self.frame, text= "QrCode Generator", font= ("Aerial", 26), text_color= "white")
        self.label1.place(x= 120, y= 60)

        self.text_box1 = tk.CTkEntry(master= self.frame, placeholder_text= "Title", font=("Aerial", 16), width= 120)
        self.text_box1.place(x= 25, y= 155)

        self.text_box2 = tk.CTkEntry(master= self.frame, font=("Aerial", 16), placeholder_text= "Content", width= 280)
        self.text_box2.place(x= 25, y= 200)

        self.button1 = tk.CTkButton(master= self.frame, font=("Aerial", 18), text= "Generate", width= 200, command= self.Generate)
        self.button1.place(x= 65, y= 270)

        self.button2 = tk.CTkButton(master= self.frame, font= ("Aerial", 14), text= "Clear", fg_color= "red", command= self.Clear)
        self.button2.place(x= 95, y= 310)

        self.label2 = tk.CTkLabel(master= self.frame, text= "Made By Alireza Sharbat Harir", font= ("Aerial", 8))
        self.label2.place(x= 15, y= 420)

        self.icon_view = tk.CTkLabel(master= self.frame, text= "")
        Icon = PhotoImage(file= "QrCode.png")
        self.icon_view.place(x= 25, y= 30)
        self.icon_view.configure(image= Icon)

        self.image_view = tk.CTkLabel(master= self.frame, text= "")

        self.entryerror = tk.CTkLabel(master= self.frame)

        self.root.mainloop()
    def Generate(self):
        self.title = self.text_box1.get()
        self.data = self.text_box2.get()

        if self.title == "" or self.data == "":
            self.entryerror = tk.CTkLabel(master= self.frame, text= "*You Have To Enter Title and Content.", font= ("Aerial", 12), text_color= "#DC143C")
            self.entryerror.place(x= 66, y= 233)
            return None

        self.entryerror.destroy()

        qr = qrcode.QRCode(version= 1, box_size=10, border= 2)
        qr.add_data(self.data)
        qr.make()
        img = qr.make_image()
        img.save(str(self.title) + ".png")

        global Image
        Image = PhotoImage(file= str(self.title) + ".png")
        self.image_view.place(x= 400, y= 120)
        self.image_view.configure(image= Image)
    def Clear(self):
        self.text_box1.delete("0", END)
        self.text_box2.delete("0", END)
        self.image_view.configure(image= "")
        self.entryerror.destroy()
QrCode()
