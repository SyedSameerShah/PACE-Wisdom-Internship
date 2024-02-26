import tkinter as tk
import qrcode
import tkinter.colorchooser

def generate_qrcode():
    data = URL.get()
    file_name = file_names.get()

    if not data:
        result_label.config(text=f"Please enter the URL")
        return
    elif not file_name:
        result_label.config(text=f"Please enter the image name")
        return

    qr = qrcode.QRCode(
        version=4,
        box_size=20,
        border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=qr_fill_color.get(), back_color=qr_bg_color.get())
    img.save('output/' + file_name + '.png')

    result_label.config(text=f"QR Code generated and saved as {file_name}.png")


def choose_color():
    color = tkinter.colorchooser.askcolor(title='Fill color')[1]
    bg_color = tkinter.colorchooser.askcolor(title='Background color')[1]
    qr_fill_color.set(color)
    qr_bg_color.set(bg_color)


#GUI
root = tk.Tk()
root.title("QR Code Generator")


URL_lable = tk.Label(root, text="Enter URL:")
URL_lable.grid(row=2,column=0,padx=10,pady=10)

URL = tk.Entry(root,width=55)
URL.grid(row=2,column=1,padx=10,pady=10)

qr_fill_color = tk.StringVar(root)
qr_bg_color = tk.StringVar(root)
# default colors
qr_fill_color.set('#000000') 
qr_bg_color.set('#FFFFFF') 

color_label = tk.Label(root, text="Choose Colors:")
color_label.grid(row=3,column=0,padx=10,pady=10)

color_button = tk.Button(root, text="click to choose colors",width=48, command=choose_color)
color_button.grid(row=3,column=1,padx=10,pady=10)

color_fill_lable = tk.Label(root, text='Fill Color')
color_fill_lable.grid(row=4,column=0,padx=10)
color_fill_display = tk.Label(root, textvariable=qr_fill_color)
color_fill_display.grid(row=5,column=0,padx=10,pady=5)

color_bg_lable = tk.Label(root, text='Backgroung Color')
color_bg_lable.grid(row=4,column=1,padx=10)
color_bg_display = tk.Label(root, textvariable=qr_bg_color)
color_bg_display.grid(row=5,column=1,padx=10,pady=5)

file_names_lable = tk.Label(root, text="Enter image file name to be saved :")
file_names_lable.grid(row=6,column=0,padx=10,pady=10)

file_names = tk.Entry(root,width=55)
file_names.grid(row=6,column=1,padx=10,pady=10)


generate_qrcode = tk.Button(root, text="Generate QR Code",width = 50, command=generate_qrcode)
generate_qrcode.grid(row=7,column=1, padx=10,pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=8,column=1,padx=10,pady=15)

root.mainloop()