from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

main = Tk()

#--Config--
main.title("Create Visiting Cards")
main.geometry("650x275")
main.iconbitmap('')  # Añade el path del icono aquí si tienes uno

#--Coordinates for each style--
coordinates = {
    1: {'name': (45, 85), 'email': (193, 84), 'street': (193, 99), 'phone': (193, 68)},
    2: {'name': (60, 50), 'email': (70, 120), 'street': (70, 138), 'phone': (70, 103)},
    3: {'name': (30, 57), 'email': (184, 92), 'street': (184, 112), 'phone': (184, 75)},
    4: {'name': (210, 30), 'email': (210, 128), 'street': (210, 95), 'phone': (210, 65)},
    5: {'name': (50, 90), 'email': (225, 88), 'street': (210, 142), 'phone': (210, 35)},
    6: {'name': (45, 33), 'email': (65, 88), 'street': (65, 114), 'phone': (65, 62)},
}

current_style = 1
MAX_LENGTH = 20  # Máximo número de caracteres permitidos

#--Color list for each style--
colors = {
    1: "white",
    2: "black",
    3: "white",
    4: "white",
    5: "black",  
    6: "black"
}

def load_image(image_path, coords, font_color):
    pil_image = Image.open(image_path)
    pil_image_reducida = pil_image.resize((350, 190))
    draw = ImageDraw.Draw(pil_image_reducida)
    font = ImageFont.load_default()

    draw.text(coords['name'], name_picture.get(), fill=font_color, font=font)
    draw.text(coords['email'], email_picture.get(), fill=font_color, font=font)
    draw.text(coords['street'], street_picture.get(), fill=font_color, font=font)
    draw.text(coords['phone'], phone_picture.get(), fill=font_color, font=font)

    tk_image = ImageTk.PhotoImage(pil_image_reducida)
    label.place(x=250, y=20)
    label.config(image=tk_image)
    label.image = tk_image

    return pil_image_reducida

def card_style(style_number):
    global current_style
    current_style = style_number
    image_path = f"C:\\Users\\setco\\Desktop\\VisitingCard\\style\\card_style_{style_number}.png"
    coords = coordinates[style_number]
    font_color = colors[style_number]
    load_image(image_path, coords, font_color)

def delete_image():
    label.config(image='')
    label.image = None
    name_picture.set("")
    email_picture.set("")
    street_picture.set("")
    phone_picture.set("")

def download_image():
    image_path = f"C:\\Users\\setco\\Desktop\\VisitingCard\\style\\card_style_{current_style}.png"
    coords = coordinates[current_style]
    font_color = colors[current_style]
    pil_image = load_image(image_path, coords, font_color)
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        pil_image.save(file_path)
        messagebox.showinfo("Success", "Image saved successfully")

def update_image(*args):
    image_path = f"C:\\Users\\setco\\Desktop\\VisitingCard\\style\\card_style_{current_style}.png"
    coords = coordinates[current_style]
    font_color = colors[current_style]
    load_image(image_path, coords, font_color)

def limit_size(P):
    if len(P) > MAX_LENGTH:
        return False
    return True

vcmd = (main.register(limit_size), '%P')

#--Company Name--
name = Label(main, text='Name:')
name.place(x=20, y=20)
name_picture = StringVar()
name_picture.trace_add("write", update_image)
picture_name = Entry(main, textvariable=name_picture, validate='key', validatecommand=vcmd)
picture_name.place(x=75, y=23)

#--Email--
email = Label(main, text='Email:')
email.place(x=20, y=50)
email_picture = StringVar()
email_picture.trace_add("write", update_image)
picture_email = Entry(main, textvariable=email_picture, validate='key', validatecommand=vcmd)
picture_email.place(x=75, y=53)

#--Street--
street = Label(main, text='Street:')
street.place(x=20, y=80)
street_picture = StringVar()
street_picture.trace_add("write", update_image)
picture_street = Entry(main, textvariable=street_picture, validate='key', validatecommand=vcmd)
picture_street.place(x=75, y=83)

#--Phone--
phone = Label(main, text='Phone:')
phone.place(x=20, y=110)
phone_picture = StringVar()
phone_picture.trace_add("write", update_image)
picture_phone = Entry(main, textvariable=phone_picture, validate='key', validatecommand=vcmd)
picture_phone.place(x=75, y=113)

#--Radiobutton--
opcion_seleccionada = tk.StringVar()
opcion_seleccionada.set("Style 0")  # Valor por defecto

for i in range(1, 7):
    select_style = tk.Radiobutton(main, text=f"Style {i}", variable=opcion_seleccionada, value=f"Style {i}", command=lambda i=i: card_style(i))
    x_pos = 20 + ((i-1) % 2) * 80
    y_pos = 140 + ((i-1) // 2) * 30
    select_style.place(x=x_pos, y=y_pos)

#--Button--
button_delete_image = Button(main, text='Delete', relief=GROOVE, command=delete_image, font=("Helvetica", 12))
button_delete_image.place(x=20, y=230)
button_download_image = Button(main, text='Download', relief=GROOVE, command=download_image, font=("Helvetica", 12))
button_download_image.place(x=100, y=230)

#--END--
label = tk.Label(main)
main.mainloop()
