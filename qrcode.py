import tkinter as tk
import pyqrcode
from tkinter import messagebox



def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = tk.BitmapImage(data = qr.xbm(scale=8))
    else:
        print('naber')
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())

a1 = "mtu"
a2 = "tom"

def show_frame(frame):
    frame.tkraise()
    
window = tk.Tk()

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

login = tk.Frame(window)
frame1 = tk.Frame(window)


for frame in (frame1, login):
    frame.grid(row=0,column=0,sticky='nsew')
    
#====================login page=================

kullanici = tk.Label(login, text="KULLANICI ADI:")
kullanici.pack(pady=10)

y= tk.StringVar()
kullanici_girisi = tk.Entry(login, textvariable=y)
kullanici_girisi.pack(pady=10)

kullanici = tk.Label(login, text="Şifre GİRİSİ:")
kullanici.pack(pady=10)

x= tk.StringVar()
kullanici_girisi = tk.Entry(login, textvariable=x)
kullanici_girisi.pack(pady=10)

doğru_yanlis = tk.Label(login, text="", font="Verdana 10 bold")
doğru_yanlis.pack(pady=10)
def giris_komut():
	kullan = y.get()
	sif = x.get()
	if kullan == a1 and sif == a2:
		show_frame(frame1)
	else:
		doğru_yanlis.config(text="YANLIŞ",fg="red")	
giris = tk.Button(login, text="Giris",command=giris_komut)
giris.pack(pady=10)
#==================Frame1===========================


lbl = tk.Label(frame1, text="Enter message or URL")
lbl.pack(pady=10)

user_input = tk.StringVar()
entry = tk.Entry(frame1,textvariable = user_input)
entry.pack(padx=10)


button = tk.Button(frame1,text = "generate_QR",width=15,command = generate_QR)
button.pack(pady=10)

img_lbl = tk.Label(frame1)
img_lbl.pack()
output = tk.Label(frame1,text="")
output.pack()

show_frame(login)
window.mainloop()
